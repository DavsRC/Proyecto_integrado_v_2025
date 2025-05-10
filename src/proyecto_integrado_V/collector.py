import requests
import pandas as pd
from bs4 import BeautifulSoup
import os

class Collector:
    def __init__(self, logger):
        self.url = 'https://finance.yahoo.com/quote/TSLA/history/?frequency=1d&period1=1672531200&period2=1746837813'
        self.logger = logger

        base_path = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(base_path, 'static', 'data')
        os.makedirs(self.data_path, exist_ok=True)

    def collector_data(self):
        try:
            df = pd.DataFrame()
            headers = {
                'User-Agent': 'Mozilla/5.0'
            }

            response = requests.get(self.url, headers=headers)
            if response.status_code != 200:
                self.logger.error('Collector', 'collector_data', f"Error al consultar la url: {response.status_code}")
                return df

            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.select_one('div[data-testid="history-table"] table')
            if not table:
                self.logger.error('Collector', 'collector_data', "No se encontró la tabla de datos.")
                return df

            headerss = [th.get_text(strip=True) for th in table.thead.find_all('th')]
            rows = []
            for tr in table.tbody.find_all('tr'):
                columns = [td.get_text(strip=True) for td in tr.find_all('td')]
                if len(columns) == len(headerss):
                    rows.append(columns)

            df = pd.DataFrame(rows, columns=headerss).rename(columns={
                'Date': 'fecha',
                'Open': 'abrir',
                'High': 'max',
                'Low': 'min',
                'Close*': 'cerrar',
                'Adj Close**': 'cierre_ajustado',
                'Volume': 'volumen'
            })

            self.logger.info('Collector', 'collector_data', f"Datos obtenidos exitosamente {df.shape}")
            return df

        except Exception as error:
            self.logger.error('Collector', 'collector_data', f"Error al obtener los datos: {error}")
            return pd.DataFrame()
