# Proyecto 3: Predicción de Precios de Vivienda

## 🎯 Objetivo

Construir un modelo de regresión lineal que prediga el precio medio de vivienda en distintas zonas de California, con foco en **entender e interpretar estadísticamente** el modelo — no solo en obtener una predicción, sino en poder explicar *por qué* el modelo predice lo que predice.

Este proyecto es el tercer eslabón del portafolio de Data Science, y el primero enfocado en **regresión** (predicción de un valor numérico continuo), sentando las bases estadísticas necesarias antes de avanzar a modelos de clasificación y clustering.

## 📊 Dataset

**California Housing Dataset** (censo de EE.UU., 1990)

- **Fuente:** integrado en `scikit-learn` (`sklearn.datasets.fetch_california_housing`)
- **Registros:** 20.640 zonas censales
- **Variables predictoras (8):** ingreso medio, antigüedad de la vivienda, promedio de habitaciones y dormitorios por hogar, población, ocupación promedio, latitud y longitud
- **Variable objetivo:** precio medio de vivienda por zona (USD)

Dataset limpio (sin valores nulos), elegido deliberadamente para poder concentrar el trabajo en el análisis estadístico y no en la limpieza de datos.

## 🗺️ Fases del proyecto

| Fase | Contenido | Estado |
|---|---|---|
| 1 | Carga y exploración de datos (EDA) 
| 2 | Regresión lineal simple con Scikit-Learn 
| 3 | Interpretación estadística con StatsModels (coeficientes, p-values, R²) 
| 4 | Diagnóstico de supuestos (residuos, homocedasticidad, multicolinealidad) 
| 5 | Evaluación del modelo (RMSE, MAE) 
| 6 | Regularización: Ridge vs Lasso 

## 📐 Conceptos estadísticos trabajados

Este proyecto pone foco explícito en fundamentos que sostienen cualquier modelo de regresión, no solo en el código:

- **Coeficientes de regresión** y su interpretación en términos de negocio
- **R² (coeficiente de determinación):** qué proporción de la variabilidad del precio explica el modelo
- **P-values y significancia estadística:** qué variables realmente aportan al modelo
- **Supuestos de la regresión lineal:** linealidad, homocedasticidad, normalidad de residuos, multicolinealidad (VIF)
- **Métricas de error:** RMSE y MAE, y cómo su relación (ratio) sirve como diagnóstico de outliers en las predicciones
- **Regularización (Ridge/Lasso):** introducción a por qué y cuándo conviene penalizar coeficientes

## 🛠️ Tecnologías

`Python` · `pandas` · `numpy` · `matplotlib` · `seaborn` · `scikit-learn` · `statsmodels`

