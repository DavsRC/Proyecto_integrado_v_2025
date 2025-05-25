#  Proyecto Integrado V - Recolección de Datos Históricos de TSLA (Tesla Inc.)

Este proyecto implementa una solución automatizada para la recolección continua de datos históricos del indicador económico *TSLA* desde Yahoo Finanzas, utilizando técnicas de scraping web. La información obtenida se almacena en formatos *CSV* y *SQLite*, asegurando la trazabilidad mediante logs estructurados y automatización con GitHub Actions.

---

##  Estructura del Proyecto

```
Proyecto_integrado_v_2025/
├── .github/
│   └── workflows/
│       └── update_data.yml         # Flujo de trabajo automatizado en GitHub Actions
├── src/
│   └── proyecto_integrado_V/
│       ├── static/
│       │   └── data/               # Almacenamiento de archivos CSV y SQLite
│       ├── collector.py            # Clase para extracción y persistencia de datos
│       ├── logger.py               # Clase para manejo de logs
│       └── main.py                 # Script principal ejecutable
├── docs/
│   └── report_entrega1.pdf         # Informe técnico en formato APA
├── requirements.txt                # Archivo de dependencias
├── setup.py                        # Configuración del paquete Python
└── README.md                       # Este documento
```

---

##  Tecnologías Utilizadas

- *Python 3.9.2*
- requests: Descarga de contenido web
- beautifulsoup4: Parseo HTML de la tabla
- pandas: Transformación y manejo de datos
- sqlite3: Persistencia en base de datos
- GitHub Actions: Automatización de recolección continua
- logging: Registro de ejecución por timestamp

---

##  Ejecución Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/proyecto_integrado_v_2025.git
cd proyecto_integrado_v_2025

# 2. Crear y activar un entorno virtual
python -m venv venv
.env\Scripts\Activate.ps1  # PowerShell en Windows

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Ejecutar el script principal
python src/proyecto_integrado_V/main.py


Al finalizar, se generarán automáticamente:

-  BTC_EUR_data.csv con los datos históricos (en static/data)
-  btc_eur_data.db con la base SQLite
-  Logs individuales en la carpeta logs/

---

##  Automatización en GitHub Actions

Cada vez que se hace push en la rama main, el archivo .github/workflows/update_data.yml activa el siguiente flujo:

1. Configura el entorno y dependencias.
2. Ejecuta el script principal (main.py).
3. Genera o actualiza archivos CSV y DB.
4. Agrega los nuevos archivos al repositorio.
5. Realiza commit y push automáticos.

---

## 📄 Documentación Técnica

El informe técnico del proyecto está disponible en:


docs/report_entrega1.pdf


Contiene resumen, introducción, metodología y análisis en formato *APA*.

---

##  Autores

*Davinson Stiven Rincon Campos*
*Estefania Jimenez Tabares*  
Estudiantes de Ingeniería en Desarrollo de Software y Datos  
Institución Universitaria Digital de Antioquia  

---

## 🗓 Última actualización

Mayo de 2025
