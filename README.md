# Proyecto Integrado V - Recolección, Enriquecimiento y Modelado de Datos Históricos de TSLA (Tesla Inc.)

Este proyecto implementa una solución automatizada para la recolección, enriquecimiento y modelado predictivo de datos históricos del indicador económico **TSLA** (Tesla Inc.), extraídos desde _Yahoo Finanzas_ mediante técnicas de web scraping.

La información se almacena en formatos _CSV_ y _SQLite_, se transforma para análisis financiero, y se entrena un modelo predictivo de precios. Todo el pipeline está integrado con _GitHub Actions_ y complementado con un _dashboard interactivo_ en Power BI.

---

## Estructura del Proyecto

```
Proyecto_integrado_v_2025/
├── .github/
│   └── workflows/
│       └── update_data.yml          # Flujo de trabajo automático en GitHub Actions
├── src/
│   └── proyecto_integrado_V/
│       ├── static/
│       │   └── data/                # Archivos TSLA_data.csv, .db, .xlsx, .pkl
│       │
│       ├── collector.py             # Recolección de datos desde Yahoo Finance
│       ├── enricher.py              # Enriquecimiento de datos y KPIs financieros
│       ├── modeller.py              # Entrenamiento del modelo predictivo
│       ├── logger.py                # Registro estructurado de eventos
│       └── main.py                  # Script principal que ejecuta todo el pipeline
├── dashboard/
│   └── TSLA_dashboard.pbix          # Dashboard Power BI con al menos 5 KPIs
├── docs/
│   └── report_entrega2.pdf          # Informe técnico completo (formato APA)
├── requirements.txt                 # Dependencias del proyecto
├── setup.py                         # Configuración opcional del paquete
└── README.md                        # Este documento
```

---

## Tecnologías Utilizadas

- **Python 3.9.2**
- `requests`: Descarga de contenido web
- `beautifulsoup4`: Parseo HTML
- `pandas`: Transformación y análisis de datos
- `sqlite3`: Almacenamiento relacional
- `scikit-learn`: Modelo predictivo
- `joblib`: Serialización de modelos
- `logging`: Registro de eventos
- **GitHub Actions**: Automatización CI/CD
- **Power BI**: Visualización interactiva de KPIs

---

## Ejecución Local

```bash
# 1. Clonar el repositorio
git clone https://github.com/usuario/proyecto_integrado_v_2025.git
cd proyecto_integrado_v_2025

# 2. Crear y activar un entorno virtual
python -m venv venv
./venv/Scripts/Activate.ps1  # En PowerShell de Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar todo el pipeline
python src/proyecto_integrado_V/main.py
```

> Se generarán automáticamente:
>
> - `TSLA_data.csv`, `TSLA_data_enriched.csv` y `TSLA_dashboard_data.xlsx`
> - Base SQLite: `tsla_data.db`
> - Modelo serializado: `model.pkl`
> - Logs en consola

---

## Automatización con GitHub Actions

El flujo `.github/workflows/update_data.yml` permite:

1. Descargar los datos desde Yahoo Finance
2. Enriquecerlos y generar KPIs
3. Entrenar y guardar un modelo de regresión
4. Versionar los resultados en GitHub automáticamente

---

## Dashboard BI

El dashboard Power BI (`dashboard/TSLA_dashboard.pbix`) incluye:

- Precio ajustado y medias móviles
- Tasa de variación diaria
- Retorno acumulado
- Volatilidad (7 días)
- Promedio de volumen semanal

---

## Documentación Técnica

Disponible en:

```
docs/report_entrega2.pdf
```

Formato **APA**: incluye resumen, introducción, metodología, análisis de resultados y capturas del dashboard.

---

## Autores

**Davinson Stiven Rincon Campos**  
**Estefania Jimenez Tabares**  
Estudiantes de Ingeniería en Desarrollo de Software y Datos  
Institución Universitaria Digital de Antioquia

---

## Última actualización

Mayo de 2025
