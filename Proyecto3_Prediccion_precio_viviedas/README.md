# Proyecto 3: Predicción de Precios de Vivienda

## 🎯 Objetivo

Construir un modelo de regresión lineal que prediga el precio mediano de vivienda en distintas zonas de California, con foco en **entender e interpretar estadísticamente** el modelo — no solo en obtener una predicción, sino en poder explicar *por qué* el modelo predice lo que predice.

Este proyecto es el tercer eslabón del portafolio de Data Science, y el primero enfocado en **regresión** (predicción de un valor numérico continuo), sentando las bases estadísticas necesarias antes de avanzar a modelos de clasificación y clustering.

## 📊 Dataset

**California Housing Dataset** (censo de EE.UU., 1990)

- **Fuente:** versión de Kaggle en formato CSV
- **Registros:** 20.640 zonas censales
- **Variables predictoras (9):** ingreso mediano, antigüedad mediana de la vivienda, totales de habitaciones, dormitorios, población y hogares por zona, latitud, longitud y proximidad al océano (categórica, 5 niveles)
- **Variable objetivo:** precio mediano de vivienda por zona (USD)

A diferencia de la versión incluida en scikit-learn, este dataset **no viene limpio**: contiene 207 registros con valores nulos, una variable categórica que requiere codificación (dummies) y — el hallazgo más interesante del proyecto — **958 zonas con el precio censurado (topado) en \$500.001**, detectadas durante el diagnóstico de residuos y eliminadas para entrenar solo con precios reales.

## 🗺️ Fases del proyecto

| Fase | Contenido |
|---|---|
| 1 | Carga y exploración de datos (EDA), tratamiento de nulos y codificación de variables categóricas |
| 2 | Regresión lineal con Scikit-Learn |
| 3 | Interpretación estadística con StatsModels (coeficientes, p-values, R²) |
| 4 | Diagnóstico de multicolinealidad (VIF) y *feature engineering*: de totales por zona a ratios por hogar |
| 5 | Diagnóstico de residuos: detección de datos censurados en \$500.001 y reentrenamiento |
| 6 | Verificación de supuestos: heterocedasticidad (Breusch-Pagan) y normalidad de residuos (Jarque-Bera) |
| 7 | Evaluación en datos de prueba (RMSE, MAE, R²) |
| 8 | Regularización: Ridge vs Lasso con búsqueda de `alpha` por validación cruzada |

## 📈 Resultados

- **R² = 0.584** en el conjunto de prueba, con **RMSE de \$63.447** y **MAE de \$46.751**, usando únicamente variables demográficas y estructurales de zona.
- El **ingreso mediano** es el predictor dominante; la ubicación interior (INLAND) descuenta ~\$59.000 frente a zonas cercanas al océano.
- **Ridge y Lasso no superaron a la regresión lineal base**: con ~15.500 observaciones y solo 9 variables, la regularización no aporta. Lasso eliminó exactamente la variable que el análisis de VIF ya señalaba como redundante (`rooms_per_household`), validando el diagnóstico previo.
- Limitaciones identificadas y cuantificadas: heterocedasticidad (el error absoluto crece con el precio de la zona) y residuos con asimetría positiva. Próxima iteración: transformación logarítmica del precio y reincorporación de variables geográficas derivadas de latitud/longitud.

## 📐 Conceptos estadísticos trabajados

Este proyecto pone foco explícito en fundamentos que sostienen cualquier modelo de regresión, no solo en el código:

- **Coeficientes de regresión** y su interpretación en términos de negocio
- **R² (coeficiente de determinación):** qué proporción de la variabilidad del precio explica el modelo
- **P-values y significancia estadística:** qué variables realmente aportan al modelo
- **Multicolinealidad (VIF)** y cómo el *feature engineering* la reduce (de VIF > 30 a menos de 8)
- **Datos censurados:** cómo un tope artificial en la variable objetivo distorsiona el modelo y cómo detectarlo en los residuos
- **Supuestos de la regresión lineal:** homocedasticidad (Breusch-Pagan) y normalidad de residuos (Jarque-Bera)
- **Métricas de error:** RMSE y MAE, y cómo su relación (ratio) sirve como diagnóstico de outliers en las predicciones
- **Regularización (Ridge/Lasso):** optimización de `alpha` por validación cruzada, y por qué con muchos datos y pocas variables no aporta mejoras

## 🛠️ Tecnologías

`Python` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `statsmodels`