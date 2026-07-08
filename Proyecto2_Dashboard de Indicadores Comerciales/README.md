## Proyecto 2: Dashboard de Indicadores Comerciales

### 🎯 Objetivo
Construir un dashboard de storytelling en Python que traduzca datos relacionales de e-commerce en insights claros de ventas y comportamiento de clientes, para apoyar la toma de decisiones de negocio.

### 🧠 Habilidades a desarrollar
- Unión de tablas relacionales (`pd.merge()`) equivalente a JOIN de SQL
- Cálculo de KPIs de negocio con `groupby()` y `.agg()`
- Selección del gráfico correcto según la pregunta de negocio (storytelling visual)
- Construcción de un dashboard tipo grid con múltiples visualizaciones (subplots)
- Comunicación de hallazgos técnicos en lenguaje de negocio

### 🛠️ Tecnologías
Python, pandas, matplotlib, seaborn, numpy, Jupyter/Google Colab

### 📦 Dataset sugerido
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) — 9 tablas relacionales con información de pedidos, clientes, productos, pagos, reviews y ubicación geográfica (2016–2018).

### 🗺️ Ruta paso a paso

| Paso | Actividad |
|---|---|
| 1 | Cargar las 8 tablas y hacer inspección inicial (`.info()`, `.describe()`, `.head()`) |
| 2 | Unir las tablas clave con `pd.merge()` (orders, customers, order_items, products, payments) |
| 3 | Traducir categorías de producto al inglés usando la tabla de traducción |
| 4 | Calcular KPIs de negocio: ventas totales, ticket promedio, tendencia mensual, categorías top |
| 5 | Analizar comportamiento de clientes: ubicación geográfica, métodos de pago, satisfacción (reviews) |
| 6 | Construir visualizaciones de storytelling (matplotlib/seaborn) para cada pregunta de negocio |
| 7 | Armar el dashboard final (grid de subplots) y redactar conclusiones de negocio |

### ✅ Entregables
- [ ] Notebook con el análisis completo
- [ ] Mínimo 5 visualizaciones integradas en un dashboard
- [ ] Sección de conclusiones en lenguaje de negocio (no solo técnico)
