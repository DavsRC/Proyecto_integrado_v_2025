from setuptools import setup, find_packages

setup(
    name="entregables_2025",
    author="Davinson Rincon",
    version="0.0.1",
    author_email="",
    description="Colector de datos históricos de TSLA desde Yahoo Finanzas",
    packages=find_packages(),
    install_requires=[
        "pandas==2.2.3",
        "openpyxl",
        "requests==2.32.3",
        "beautifulsoup4==4.13.3"
    ]
)
