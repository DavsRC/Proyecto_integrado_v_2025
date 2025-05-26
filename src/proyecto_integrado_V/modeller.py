import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

class Modelador:
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(base_path, 'static', 'models', 'model.pkl')
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

    def entrenar(self, df):
        # Selección de variables predictoras
        df = df.dropna()  # Eliminar nulos generados por rolling y pct_change
        X = df[['media_movil_7', 'media_movil_30', 'volatilidad_7d']]
        y = df['cierre_ajustado']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        y_pred = modelo.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        print(f"Modelo entrenado. RMSE: {rmse:.2f}")

        joblib.dump(modelo, self.model_path)
        print(f"Modelo guardado en: {self.model_path}")

    def predecir(self, df):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError("Modelo no entrenado. Ejecuta primero entrenar().")

        modelo = joblib.load(self.model_path)
        df = df.dropna()
        X = df[['media_movil_7', 'media_movil_30', 'volatilidad_7d']]
        predicciones = modelo.predict(X)
        return predicciones

if __name__ == "__main__":
    # Ruta al archivo enriquecido
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'static', 'data', 'TSLA_data_enriched.csv')

    # Cargar el dataset enriquecido
    df = pd.read_csv(data_path)

    modelador = Modelador()
    modelador.entrenar(df)
