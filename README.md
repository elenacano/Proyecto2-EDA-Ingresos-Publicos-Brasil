# Análisis exploratorio sobre datos de ingresos públicos de Brasil del 2013 al 2021.
![Descripción de la imagen](imagenes/Designer.jpeg)

Este proyecto consiste en la realización de un análisis exploratorio de datos (EDA) sobre un conjunto de datos de ingresos gubernamentales de Brasil que contiene información por diferentes categorías económicas, organizaciones y años. El objetivo principal es identificar patrones de ingresos, su evolución a lo largo del tiempo y las discrepancias entre los valores previstos y recaudados.

## Objetivos del Proyecto

Los objetivos principales del análisis son:

1. **Limpieza de datos**: Se parte de nueve archivos de `csv` distintos que habrá que homogeneizar y hacer un primer limpiado para concatenarlos y generar el archivo principal sobre el cual trabajaremos.

2. **Análisis Exploratorio de Datos (EDA)**: Examinar la relación entre diferentes variables clave y explorar categorías relevantes para identificar patrones o discrepancias significativas.

3. **Visualización**: Generar gráficos que permitan identificar tendencias y patrones relevantes en los datos analizados.



## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **datos/**: Carpeta que contiene los archivos `.csv` y cualquier otro tipo de dato necesario.

- **notebooks/**: Carpeta que contiene los archivos `.ipynb` sobre los cuales hemos trabajado los datos en el siguiente orden:
  - `1-exploracion_inicial.ipynb`
  - `2-limpieza.ipynb`
  - `3-eda.ipynb`
  - `4-visualizacion.ipynb`

- **src/**: Carpeta que contiene los archivos `.py` externos usados para definir las funciones que se llaman desde los notebooks.
  - `soporte_limpieza.py`


## Instalación y Requisitos
Este proyecto usa Python 3.11 y requiere las siguientes bibliotecas:
- numpy
- pandas
- matplotlib.pyplot
- seaborn
- re

Para visualizar el proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
   ```bash
   git clone [URL del repositorio]
   
2. **Navega a la carpeta del proyecto**:
   ```bash
   cd Proyecto2-EDA-Ingresos-Publicos-Brasil/notebooks

2. **Ejecutar los archivos**:
   Deberás ejecutar cada notebook en el orden definido para poder ir viendo la evolución del estudio.