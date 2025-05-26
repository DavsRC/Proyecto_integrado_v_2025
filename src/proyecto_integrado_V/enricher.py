import pandas as pd
import os

def enriquecer_datos():
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, 'static', 'data', 'TSLA_data.csv')
    output_path = os.path.join(base_path, 'static', 'data', 'TSLA_data_enriched.csv')

    # Leer el CSV original
    df = pd.read_csv(data_path)

    # Renombrar columnas largas (si aplica)
    df.rename(columns={
        'CloseClose price adjusted for splits.': 'cerrar',
        'Adj CloseAdjusted close price adjusted for splits and dividend and/or capital gain distributions.': 'cierre_ajustado'
    }, inplace=True)

    # Asegurar formato de fecha
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
    df = df.dropna(subset=['fecha'])
    df = df.sort_values('fecha')

    # Normalizar nombres de columnas
    df.columns = df.columns.str.strip().str.lower()

    # Convertir columnas numéricas
    for col in ['abrir', 'max', 'min', 'cerrar', 'cierre_ajustado', 'volumen']:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(',', '', regex=False)
            .str.replace('-', '', regex=False)
            .replace('', '0')
            .astype(float)
        )

    # Variables temporales
    df['año'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    df['dia'] = df['fecha'].dt.day
    df['dia_semana'] = df['fecha'].dt.day_name()

    # Indicadores financieros
    df['tasa_variacion'] = df['cierre_ajustado'].pct_change()
    df['media_movil_7'] = df['cierre_ajustado'].rolling(window=7).mean()
    df['media_movil_30'] = df['cierre_ajustado'].rolling(window=30).mean()
    df['retorno_acumulado'] = (1 + df['tasa_variacion']).cumprod()
    df['volatilidad_7d'] = df['tasa_variacion'].rolling(window=7).std()
    df['volumen_promedio_semanal'] = df['volumen'].rolling(window=7).mean()

    # Guardar CSV enriquecido
    df.to_csv(output_path, index=False)
    print(f"Datos enriquecidos guardados en: {output_path}")

    # Guardar archivo Excel con KPIs para Power BI
    dashboard_path = os.path.join(base_path, 'static', 'data', 'TSLA_dashboard_data.xlsx')
    df_kpi = df[[
        'fecha', 'cierre_ajustado', 'media_movil_7', 'media_movil_30',
        'tasa_variacion', 'retorno_acumulado', 'volatilidad_7d', 'volumen_promedio_semanal'
    ]]
    df_kpi.to_excel(dashboard_path, index=False)
    print(f"Archivo Excel para Power BI exportado en: {dashboard_path}")

if __name__ == "__main__":
    enriquecer_datos()
