import streamlit as st
from supabase import create_client
import google.generativeai as genai
import tempfile, os, json, time
from datetime import date

SUPABASE_URL = "https://kbboziprfwsfuryoebtw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtiYm96aXByZndzZnVyeW9lYnR3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzkwNjQ1NzksImV4cCI6MjA5NDY0MDU3OX0.OaTJrGJSF-vX1SpiLezoQteJ-cVFBLTagF6xUazNmAY"
GEMINI_KEY  = "AIzaSyBQZjTDvH_XqTYCQJCq3cOUqAqjhlKzpiw"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
genai.configure(api_key=GEMINI_KEY)

st.set_page_config(page_title="Pólizas al Día", page_icon="🛡️", layout="wide")

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], .main { background-color: #080d18 !important; color: #e2e8f0; }
[data-testid="stSidebar"] { background: #0a0f1e !important; border-right: 1px solid #1a2744; }
.stTextInput>div>div>input { background-color: #0f1829 !important; color: #e2e8f0 !important; border: 1px solid #1e3058 !important; border-radius: 10px !important; }
.stSelectbox>div>div>div { background-color: #0f1829 !important; color: #e2e8f0 !important; border: 1px solid #1e3058 !important; }
.stButton>button { background: linear-gradient(135deg,#1d4ed8,#2563eb) !important; color:white !important; border-radius:10px !important; border:none !important; width:100%; padding:10px !important; font-weight:600; }
.stExpander { background-color:#0c1526 !important; border:1px solid #1a2f52 !important; border-radius:14px !important; margin-bottom:10px !important; }
hr { border-color: #1a2744 !important; }
.metric-card { background:#0c1526; border:1px solid #1a2f52; border-radius:14px; padding:20px; text-align:center; }
.metric-num { font-size:32px; font-weight:700; color:#3b82f6; }
.metric-label { font-size:11px; color:#64748b; margin-top:4px; letter-spacing:0.5px; text-transform:uppercase; }
.badge-auto  { background:#1e3a5f; color:#60a5fa; padding:3px 10px; border-radius:20px; font-size:11px; font-weight:600; }
.badge-hogar { background:#1a3d2e; color:#4ade80; padding:3px 10px; border-radius:20px; font-size:11px; font-weight:600; }
.badge-vida  { background:#3d1a2e; color:#f472b6; padding:3px 10px; border-radius:20px; font-size:11px; font-weight:600; }
@keyframes float  { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-10px)} }
@keyframes blink  { 0%,88%,100%{transform:scaleY(1)} 93%{transform:scaleY(0.08)} }
@keyframes wave   { 0%{transform:rotate(-10deg)} 30%{transform:rotate(-40deg)} 60%{transform:rotate(-10deg)} 80%{transform:rotate(-30deg)} 100%{transform:rotate(-10deg)} }
@keyframes pulse  { 0%{transform:scale(0.9);opacity:0.5} 100%{transform:scale(1.55);opacity:0} }
@keyframes fadein { from{opacity:0;transform:translateY(6px)} to{opacity:1;transform:translateY(0)} }
.r-float{animation:float 2.4s ease-in-out infinite}
.r-eye-l{animation:blink 3.5s ease-in-out infinite;transform-origin:47px 53px}
.r-eye-r{animation:blink 3.5s ease-in-out 0.2s infinite;transform-origin:83px 53px}
.r-arm-r{animation:wave 1.2s ease-in-out infinite;transform-origin:110px 96px}
.r-pulse{animation:pulse 1.8s ease-out infinite;transform-origin:65px 90px}
.r-msg{animation:fadein 0.4s ease;font-size:17px;font-weight:700;color:#3b82f6;text-align:center;margin-top:16px}
.r-sub{font-size:12px;color:#475569;text-align:center;margin-top:3px}
.r-wrap{display:flex;flex-direction:column;align-items:center;padding:30px 0 10px}
</style>
""", unsafe_allow_html=True)

MENSAJES = [
    ("📄 Leyendo el documento PDF...",      "Cargando páginas de la póliza"),
    ("🔍 Identificando al asegurado...",     "Buscando nombre y RUT"),
    ("🚗 Detectando tipo de cobertura...",   "Automotriz, Hogar o Vida/Salud"),
    ("💰 Calculando prima total...",         "Extrayendo valor en UF"),
    ("📅 Verificando fechas de vigencia...", "Inicio y vencimiento"),
    ("🧠 Procesando con IA...",              "Gemini analizando el contenido"),
    ("💾 Guardando en la base de datos...", "Registrando en Supabase"),
    ("✅ ¡Casi listo!",                      "Finalizando el proceso"),
]

def mostrar_robot(msg, sub):
    st.markdown(f"""
    <div class="r-wrap">
      <svg class="r-float" width="130" height="168" viewBox="0 0 130 168" xmlns="http://www.w3.org/2000/svg">
        <circle class="r-pulse" cx="65" cy="90" r="48" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.4"/>
        <line x1="65" y1="13" x2="65" y2="30" stroke="#475569" stroke-width="3" stroke-linecap="round"/>
        <circle cx="65" cy="8" r="5.5" fill="#3b82f6"/>
        <rect x="28" y="30" width="74" height="54" rx="14" fill="#0f172a" stroke="#3b82f6" stroke-width="1.8"/>
        <g class="r-eye-l"><rect x="38" y="46" width="18" height="13" rx="5" fill="#3b82f6" opacity="0.9"/><circle cx="47" cy="52" r="4" fill="#080d18"/><circle cx="49" cy="49" r="1.5" fill="white" opacity="0.9"/></g>
        <g class="r-eye-r"><rect x="74" y="46" width="18" height="13" rx="5" fill="#3b82f6" opacity="0.9"/><circle cx="83" cy="52" r="4" fill="#080d18"/><circle cx="85" cy="49" r="1.5" fill="white" opacity="0.9"/></g>
        <path d="M48 73 Q65 82 82 73" stroke="#3b82f6" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <rect x="22" y="92" width="86" height="54" rx="13" fill="#0f172a" stroke="#3b82f6" stroke-width="1.8"/>
        <rect x="38" y="102" width="54" height="30" rx="7" fill="#080d18" stroke="#1e3a5f" stroke-width="1"/>
        <circle cx="54" cy="113" r="5" fill="#3b82f6" opacity="0.85"/>
        <circle cx="65" cy="113" r="5" fill="#818cf8" opacity="0.7"/>
        <circle cx="76" cy="113" r="5" fill="#38bdf8" opacity="0.7"/>
        <rect x="46" y="122" width="38" height="4" rx="2" fill="#1e3a5f"/>
        <rect x="46" y="122" width="24" height="4" rx="2" fill="#3b82f6" opacity="0.8"/>
        <rect x="4" y="96" width="16" height="34" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
        <circle cx="12" cy="134" r="6.5" fill="#080d18" stroke="#3b82f6" stroke-width="1.5"/>
        <g class="r-arm-r">
          <rect x="110" y="96" width="16" height="34" rx="8" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
          <circle cx="118" cy="134" r="6.5" fill="#080d18" stroke="#3b82f6" stroke-width="1.5"/>
        </g>
        <rect x="38" y="148" width="17" height="16" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
        <rect x="75" y="148" width="17" height="16" rx="6" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
      </svg>
      <div class="r-msg">{msg}</div>
      <div class="r-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    _, col, _ = st.columns([1, 1.2, 1])
    with col:
        st.write("#")
        st.write("#")
        st.markdown("<div style='text-align:center;font-size:52px;'>🛡️</div>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align:center;color:#f8fafc;font-size:36px;font-weight:800;'>Pólizas <span style='color:#3b82f6;'>al Día</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;color:#475569;font-size:13px;margin-bottom:24px;letter-spacing:1px;'>PORTAL INTERNO · GESTIÓN DE SEGUROS</p>", unsafe_allow_html=True)
        st.write("---")
        usuario    = st.text_input("Usuario", placeholder="luis.yanez")
        contraseña = st.text_input("Contraseña", type="password")
        st.write("")
        if st.button("Iniciar Sesión →", use_container_width=True):
            if usuario == "luis.yanez" and contraseña == "Luis2026":
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")
        st.markdown("<p style='text-align:center;font-size:11px;color:#1e3058;margin-top:16px;'>© 2024 Pólizas al Día · Acceso restringido</p>", unsafe_allow_html=True)

else:
    with st.sidebar:
        st.markdown("<div style='padding:20px 16px 8px;font-size:20px;font-weight:800;color:#f8fafc;'>🛡️ Pólizas <span style='color:#3b82f6;'>al Día</span></div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:10px;color:#475569;padding:0 16px 8px;letter-spacing:1px;'>CRM DE SEGUROS</div>", unsafe_allow_html=True)
        st.write("---")
        menu = st.radio("", ["👥  Clientes", "📤  Subir Póliza"], index=0)
        st.write("---")
        st.markdown("<div style='font-size:11px;color:#475569;padding:0 4px;'>Conectado como</div>", unsafe_allow_html=True)
        st.markdown("<div style='font-size:13px;font-weight:600;color:#94a3b8;padding:0 4px;'>luis.yanez</div>", unsafe_allow_html=True)
        st.write("")
        if st.button("Cerrar Sesión"):
            st.session_state.autenticado = False
            st.rerun()

    if menu == "👥  Clientes":
        try:
            resp = supabase.table("polizas").select("*").order("created_at", desc=True).execute()
            clientes = resp.data
        except Exception as e:
            st.error(f"Error Supabase: {e}")
            clientes = []

        total     = len(clientes)
        autos     = sum(1 for c in clientes if c.get("tipo") == "Automotriz")
        hogares   = sum(1 for c in clientes if c.get("tipo") == "Hogar / Copropiedad")
        vidas     = sum(1 for c in clientes if c.get("tipo") == "Vida / Salud")
        prima_tot = sum(c.get("prima") or 0 for c in clientes)

        st.markdown("<h2 style='color:#f8fafc;font-weight:800;font-size:26px;margin-bottom:4px;'>Mis Clientes</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#475569;font-size:13px;margin-bottom:20px;'>Resumen del portafolio de pólizas</div>", unsafe_allow_html=True)

        c1,c2,c3,c4,c5 = st.columns(5)
        for col, num, label in [
            (c1, total,              "Total clientes"),
            (c2, autos,              "Automotriz"),
            (c3, hogares,            "Hogar"),
            (c4, vidas,              "Vida / Salud"),
            (c5, f"{prima_tot:.1f}", "UF en primas"),
        ]:
            with col:
                st.markdown(f"<div class='metric-card'><div class='metric-num'>{num}</div><div class='metric-label'>{label}</div></div>", unsafe_allow_html=True)

        st.write("")
        st.write("---")

        col_bus, col_fil = st.columns([3, 1])
        with col_bus:
            busqueda = st.text_input("", placeholder="🔍  Buscar por nombre, RUT o palabra clave...", label_visibility="collapsed")
        with col_fil:
            with st.expander("🎛️  Filtros"):
                tipo_filtro = st.selectbox("Tipo", ["Todos", "Automotriz", "Hogar / Copropiedad", "Vida / Salud"])
                rango_costo = st.selectbox("Prima", ["Cualquier monto", "Hasta 2 UF", "2–5 UF", "Más de 5 UF"])

        col_r, _ = st.columns([1, 5])
        with col_r:
            if st.button("🔄  Actualizar"):
                st.rerun()

        st.write("---")

        if busqueda:
            clientes = [c for c in clientes if busqueda.lower() in (c.get("nombre") or "").lower() or busqueda in (c.get("rut") or "")]
        if tipo_filtro != "Todos":
            clientes = [c for c in clientes if c.get("tipo") == tipo_filtro]
        if rango_costo == "Hasta 2 UF":
            clientes = [c for c in clientes if (c.get("prima") or 0) <= 2]
        elif rango_costo == "2–5 UF":
            clientes = [c for c in clientes if 2 < (c.get("prima") or 0) <= 5]
        elif rango_costo == "Más de 5 UF":
            clientes = [c for c in clientes if (c.get("prima") or 0) > 5]

        if not clientes:
            st.markdown("<div style='text-align:center;padding:70px 0;'><div style='font-size:52px;'>📂</div><p style='font-size:18px;margin-top:14px;color:#475569;'>No hay clientes registrados.</p><p style='font-size:13px;color:#334155;'>Sube una póliza para comenzar.</p></div>", unsafe_allow_html=True)
        else:
            for c in clientes:
                tipo = c.get("tipo", "—")
                if tipo == "Automotriz":
                    icono, badge = "🚗", "<span class='badge-auto'>Automotriz</span>"
                elif tipo == "Hogar / Copropiedad":
                    icono, badge = "🏠", "<span class='badge-hogar'>Hogar</span>"
                else:
                    icono, badge = "❤️", "<span class='badge-vida'>Vida / Salud</span>"
                prima_str = f"{c.get('prima',0):.2f}" if c.get("prima") else "—"
                header = f"{icono} **{c.get('nombre','—')}** · RUT {c.get('rut','—')} · {prima_str} UF · 📅 {c.get('fecha_registro','—')}"
                with st.expander(header):
                    st.markdown(badge, unsafe_allow_html=True)
                    st.write("")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Asegurado:** {c.get('nombre','—')}")
                        st.markdown(f"**RUT:** {c.get('rut','—')}")
                        st.markdown(f"**Tipo:** {tipo}")
                        st.markdown(f"**Prima Total:** {prima_str} UF")
                    with col2:
                        st.markdown(f"**Fecha Registro:** {c.get('fecha_registro','—')}")
                        st.markdown(f"**Vigencia:** {c.get('vigencia','—')}")
                        st.markdown(f"**Detalle:** {c.get('detalle','—')}")
                    if c.get("pdf_url"):
                        st.write("")
                        st.markdown(f"[📥 Descargar PDF Original]({c['pdf_url']})")

    elif menu == "📤  Subir Póliza":
        st.markdown("<h2 style='color:#f8fafc;font-weight:800;font-size:26px;margin-bottom:4px;'>Analizar Nueva Póliza</h2>", unsafe_allow_html=True)
        st.markdown("<div style='color:#475569;font-size:13px;margin-bottom:20px;'>Sube el PDF y Gemini extraerá los datos automáticamente</div>", unsafe_allow_html=True)
        st.write("---")

        archivo_pdf = st.file_uploader("Arrastra o selecciona el documento PDF", type=["pdf"])

        if archivo_pdf is not None:
            st.success("✅ Archivo cargado. Listo para procesar.")
            st.write("")
            if st.button("✨ Procesar e Inyectar Póliza con Gemini"):
                robot_ph = st.empty()
                try:
                    with robot_ph.container():
                        mostrar_robot(*MENSAJES[0])
                    time.sleep(1.2)

                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                        tmp.write(archivo_pdf.read())
                        tmp_path = tmp.name

                    with robot_ph.container():
                        mostrar_robot(*MENSAJES[1])
                    time.sleep(0.8)

                    file_name = f"{date.today()}_{int(time.time())}_{archivo_pdf.name.replace(' ','_')}"
                    with open(tmp_path, "rb") as f:
                        supabase.storage.from_("polizas-pdf").upload(
                            file_name, f, {"content-type": "application/pdf"}
                        )
                    pdf_url = f"{SUPABASE_URL}/storage/v1/object/public/polizas-pdf/{file_name}"

                    with robot_ph.container():
                        mostrar_robot(*MENSAJES[5])

                    gemini_file = genai.upload_file(tmp_path, mime_type="application/pdf")
                    model = genai.GenerativeModel("gemini-3.1-flash-lite")

                    prompt = """Analiza esta póliza de seguro chilena y extrae los datos.
Responde ÚNICAMENTE con un JSON válido, sin markdown, sin explicaciones, sin bloques de código.
Usa exactamente estos campos:
{
  "nombre": "nombre completo del asegurado",
  "rut": "RUT del asegurado formato XX.XXX.XXX-X",
  "tipo": "Automotriz o Hogar / Copropiedad o Vida / Salud",
  "prima": 0.0,
  "vigencia": "fecha de vencimiento como texto",
  "detalle": "resumen en una línea: vehículo/propiedad/cobertura principal"
}
Si no encuentras algún valor usa null."""

                    response = model.generate_content([gemini_file, prompt])
                    raw = response.text.strip()
                    if raw.startswith("```"):
                        raw = raw.split("```")[1]
                        if raw.startswith("json"):
                            raw = raw[4:]
                    datos = json.loads(raw.strip())

                    with robot_ph.container():
                        mostrar_robot(*MENSAJES[6])
                    time.sleep(1.0)

                    supabase.table("polizas").insert({
                        "nombre":         datos.get("nombre"),
                        "rut":            datos.get("rut"),
                        "tipo":           datos.get("tipo"),
                        "prima":          datos.get("prima"),
                        "vigencia":       datos.get("vigencia"),
                        "detalle":        datos.get("detalle"),
                        "pdf_url":        pdf_url,
                        "fecha_registro": str(date.today())
                    }).execute()

                    os.remove(tmp_path)

                    with robot_ph.container():
                        mostrar_robot(*MENSAJES[7])
                    time.sleep(1.0)
                    robot_ph.empty()

                    st.balloons()
                    st.success(f"✅ Póliza de **{datos.get('nombre','cliente')}** guardada correctamente.")
                    st.markdown("👈 Ve a **Mis Clientes** para verla.")
                    st.json(datos)

                except json.JSONDecodeError:
                    robot_ph.empty()
                    st.error("⚠️ Gemini no pudo extraer datos en JSON.")
                    st.code(response.text)
                except Exception as e:
                    robot_ph.empty()
                    st.error(f"❌ Error: {e}")
