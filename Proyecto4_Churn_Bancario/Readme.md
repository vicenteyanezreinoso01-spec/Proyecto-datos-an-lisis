# Proyecto1_Churn_Bancario

Predicción de **fuga de clientes (churn)** en un banco: identificar qué clientes tienen mayor probabilidad de cerrar su cuenta, para que el área comercial pueda actuar antes de perderlos.

## Problema de negocio

Retener a un cliente cuesta mucho menos que conseguir uno nuevo. Si el banco puede anticipar quién está por irse, puede enfocar sus acciones de retención (ofertas, contacto, mejoras de producto) en esos clientes, en vez de repartir el esfuerzo en toda la cartera.

El objetivo del proyecto es doble:

1. **Entender** qué características del cliente están asociadas a la fuga.
2. **Predecir** la probabilidad de churn de cada cliente con un modelo de clasificación.

## Dataset

Archivo: [`bank.csv`](./bank.csv) — 10.000 clientes, 12 columnas. Obtenido del repositorio público del curso ICS40125 ([fralfaro/ICS40125](https://github.com/fralfaro/ICS40125)).

```python
import pandas as pd

url = "https://raw.githubusercontent.com/vicenteyanezreinoso01-spec/Proyecto-datos-an-lisis/main/Proyecto1_Churn_Bancario/bank.csv"
bank_df = pd.read_csv(url)
```

### Diccionario de datos

| Columna | Descripción |
|---|---|
| `customer_id` | Identificador del cliente. |
| `credit_score` | Puntaje crediticio. |
| `country` | País del cliente. |
| `gender` | Género. |
| `age` | Edad. |
| `tenure` | Años como cliente del banco. |
| `balance` | Saldo en cuenta. |
| `products_number` | Cantidad de productos contratados. |
| `credit_card` | Tiene tarjeta de crédito (0/1). |
| `active_member` | Es cliente activo (0/1). |
| `estimated_salary` | Salario estimado. |
| `churn` | **Variable objetivo**: 1 = el cliente se fue. |

## Plan de trabajo

- [ ] Exploración y revisión de calidad de los datos.
- [ ] Análisis exploratorio: distribuciones, churn por variable y correlaciones.
- [ ] Preparación de variables: descartar identificadores, codificar variables categóricas y escalar variables numéricas cuando el modelo lo requiera.
- [ ] División en entrenamiento y prueba.
- [ ] Modelo base (regresión logística) y comparación con modelos de árboles.
- [ ] Evaluación con métricas adecuadas al problema y ajuste del umbral de decisión.
- [ ] Interpretación: qué variables pesan más y qué recomendaciones concretas se desprenden para el negocio.
