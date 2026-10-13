# Pegar esta celda al final del Colab (después de entrenar y evaluar el modelo)
# y ejecutarla. Descarga modelo.json, que se sube a GitHub junto a index.html.
import json
import numpy as np
from google.colab import files
from sklearn.metrics import confusion_matrix, classification_report

y_pred = np.argmax(modelo.predict(X_test, verbose=0), axis=1)
loss_test, acc_test = modelo.evaluate(X_test, y_test, verbose=0)
W1, b1, W2, b2 = [w.tolist() for w in modelo.get_weights()]
rep = classification_report(y_test, y_pred, target_names=le.classes_,
                            zero_division=0, output_dict=True)

datos = {
    "W1": W1, "b1": b1, "W2": W2, "b2": b2,
    "numericas": numericas,
    "media": scaler.mean_.tolist(),
    "escala": scaler.scale_.tolist(),
    "rangos": {c: [float(df[c].min()), float(df[c].max()), float(df[c].median())] for c in numericas},
    "categoricas": categoricas,
    "categorias": [[str(v) for v in c] for c in encoder.categories_],
    "clases": [str(c) for c in le.classes_],
    "metricas": {"accuracy": float(acc_test), "loss": float(loss_test), "random_forest": 0.3667},
    "matriz": confusion_matrix(y_test, y_pred).tolist(),
    "reporte": {k: v for k, v in rep.items() if k != "accuracy"},
    "historial": {k: [float(x) for x in v] for k, v in historial.history.items()},
}
json.dump(datos, open("modelo.json", "w"), ensure_ascii=False, default=float)
files.download("modelo.json")
