from logger import Logger
from collector import Collector
import pandas as pd
import os
import sqlite3
import subprocess

def main():
    logger = Logger()
    logger.info('Main', 'main', 'Inicializar clase Logger')

    collector = Collector(logger=logger)
    logger.info('Main', 'main', 'Inicializar clase Collector')

    df = collector.collector_data()

    if df.empty:
        logger.warning('Main', 'main', 'No se extrajeron datos, DataFrame vacío')
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(base_path, 'static', 'data')
        os.makedirs(output_dir, exist_ok=True)

        # CSV: Reiniciar archivo si existe
        csv_path = os.path.join(output_dir, 'TSLA_data.csv')
        if os.path.exists(csv_path):
            os.remove(csv_path)
        df.to_csv(csv_path, index=False)
        logger.info('Main', 'main', f'Datos guardados en {csv_path}')

        # SQLite
        db_path = os.path.join(output_dir, 'tsla_data.db')
        table_name = 'tsla_history'

        try:
            conn = sqlite3.connect(db_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            logger.info('Main', 'main', f'Datos guardados en base de datos SQLite: {db_path} (tabla: {table_name})')
        except Exception as e:
            logger.error('Main', 'main', f'Error al guardar en SQLite: {e}')

        # Ejecutar enricher.py
        try:
            subprocess.run(["python", os.path.join(base_path, "enricher.py")], check=True)
            logger.info('Main', 'main', 'Ejecución de enricher.py completada')
        except Exception as e:
            logger.error('Main', 'main', f'Error al ejecutar enricher.py: {e}')

        # Ejecutar modeller.py
        try:
            subprocess.run(["python", os.path.join(base_path, "modeller.py")], check=True)
            logger.info('Main', 'main', 'Ejecución de modeller.py completada')
        except Exception as e:
            logger.error('Main', 'main', f'Error al ejecutar modeller.py: {e}')

if __name__ == "__main__":
    main()
