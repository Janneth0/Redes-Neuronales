# Predicción del tipo de baja en accidentes laborales de la construcción (Argentina)

TP de Redes Neuronales · Grupo 10 · Desarrollo de Sistemas de IA

Página web que ejecuta en el navegador la red neuronal (Perceptrón Multicapa) entrenada en Colab:
el usuario completa los datos del accidente y se visualizan la predicción y los resultados del modelo.

- **Colab (entrenamiento del modelo):** [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1C41fLcTi_E_1Xaw_sCTbl-IOCqJwzUxE?usp=sharing)
- **Presentación:** https://docs.google.com/presentation/d/1u5AL64q6mvnoSWbjWGqhQ-erqgqrgnQicxnu99-C5Lg/edit?usp=sharing

## Archivos

| Archivo | Descripción |
|---|---|
| `index.html` | Página (formulario, predicción y resultados). |
| `exportar_modelo.py` | Celda para pegar en el Colab; genera `modelo.json`. |
| `modelo.json` | **Se genera desde el Colab** (pesos de la red, escalado, categorías y métricas). |

## Paso a paso

1. Abrí el Colab, ejecutá todo el notebook y pegá al final una celda con el contenido de `exportar_modelo.py`. Al ejecutarla se descarga `modelo.json`.
2. Subí `modelo.json` a este repositorio, en la misma carpeta que `index.html` (**Add file → Upload files**).
3. En [vercel.com](https://vercel.com) elegí **Add New → Project**, importá este repositorio, dejá **Framework Preset: Other**, sin comando de build, y tocá **Deploy**.

Si el Colab se vuelve a entrenar, repetí el paso 1 y reemplazá `modelo.json` en GitHub: Vercel se actualiza solo.

> Para probar en la computadora, no abras `index.html` con doble clic (el navegador bloquea la lectura de `modelo.json`). Usá `python -m http.server` en esta carpeta y entrá a http://localhost:8000.