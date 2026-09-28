# Proyecto0_Manejo_de_tablas

Práctica de manejo de tablas (manipulación de datos) con **pandas**, usando el dataset público *Sample Superstore*. El objetivo es dominar las herramientas fundamentales de pandas para trabajar con datos tabulares — indexación, agregación, combinación de tablas y tablas dinámicas — como base previa a un análisis de datos más completo.

## Dataset

El archivo [`sample_superstore.xls`](./sample_superstore.xls) contiene tres hojas:

| Hoja | Contenido |
|---|---|
| `Orders` | ~10.000 pedidos: cliente, producto, categoría, ventas, ganancia, descuento, fechas de pedido y despacho, región, etc. |
| `Returns` | Qué pedidos fueron devueltos. |
| `People` | Gerente responsable de cada región. |

Se carga directamente desde este mismo repositorio, en formato *raw*:

```python
import pandas as pd

url = "https://raw.githubusercontent.com/vicenteyanezreinoso01-spec/Proyecto-datos-an-lisis/main/Proyecto0_Manejo_de_tablas/sample_superstore.xls"

orders_df  = pd.read_excel(url, sheet_name="Orders")
returns_df = pd.read_excel(url, sheet_name="Returns")
people_df  = pd.read_excel(url, sheet_name="People")
```

## Requisitos

- Python 3
- `pandas`
- `numpy`

Desarrollado y ejecutado en Google Colab; también corre en cualquier Jupyter Notebook estándar.

## Estructura del notebook

**Exploración de datos** — revisión inicial de las tres tablas (`head()`, `info()`, `describe()`, nulos y duplicados) antes de manipular nada.

| Sección | Tema | Contenido |
|---|---|---|
| Parte 1 | `.loc` | Filtrado de filas/columnas por etiqueta y condición — 6 ejercicios. |
| Parte 2 | `.groupby()` | Agregaciones por grupo, clasificación con `np.where`/`np.select` y filtrado posterior con `.loc` — 11 ejercicios + prueba final. |
| Parte 3 | `.merge()` | Combinación de `Orders` + `Returns` + `People` preservando todos los pedidos (`how="left"`) y manejo de nulos generados por el merge — 3 ejercicios. |
| Parte 4 | `.pivot_table()` | Tablas dinámicas de una y varias métricas, márgenes/totales, jerarquías de índice, y casos de negocio (rentabilidad por año, velocidad de despacho, impacto del descuento en el margen) — 7 ejercicios. |
| Parte 5 | `.iloc` | Indexación posicional, slicing y acceso puntual con `.iat[]` — 2 ejercicios. |
| Parte 6 | `.groupby().transform()` | Agregaciones que preservan el largo original de la tabla, para calcular proporciones de cada fila respecto a su grupo. |
| Parte 7 | `.groupby().filter()` | Filtrado de grupos completos (no filas individuales) según condiciones agregadas, combinado con `transform`, `np.where` y `pivot_table` — 6 ejercicios. |

## Metodología

A partir de la Parte 3, los ejercicios se plantean como **encargos de negocio** — un correo de un área específica (Comercial, Logística, Finanzas, Riesgo Crediticio, Control de Calidad) pidiendo un análisis concreto, sin indicar qué método usar — en vez de instrucciones técnicas paso a paso. La idea es practicar la traducción de un requerimiento de negocio real a código, no solo la sintaxis de pandas de forma aislada.

## En desarrollo

- **Parte 0 — Limpieza de datos**: auditoría y corrección de una versión intencionalmente corrupta del dataset (espacios sobrantes, mayúsculas/minúsculas inconsistentes, tipos de dato incorrectos, valores imposibles, claves de merge sucias), con reconciliación final de métricas contra el dataset original.
- `melt` (transformación de formato ancho a largo).
