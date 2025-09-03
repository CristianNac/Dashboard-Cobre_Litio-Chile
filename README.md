# Dashboard Minería Chilena 🏔️⛏️

Dashboard interactivo para visualizar datos de exportaciones mineras chilenas de **Cobre** y **Litio** entre los años 2021-2024.

## 📋 Descripción

Este proyecto presenta un dashboard web desarrollado con **Dash** y **Plotly** que permite analizar las exportaciones mineras de Chile. Los usuarios pueden filtrar por producto (Cobre/Litio) y año para visualizar:

- **KPIs principales**: FOB total, Peso total, Cantidad de destinos
- **Gráfico de torta**: Distribución por país de destino
- **Gráfico de barras**: Monto FOB por puerto de embarque

## 🚀 Características

- **Interfaz interactiva** con filtros dinámicos
- **Visualizaciones responsivas** con Plotly
- **Procesamiento eficiente** de datos con Polars
- **Configuración flexible** mediante variables de entorno
- **Diseño modular** y bien documentado

## 🛠️ Tecnologías Utilizadas

- **Python 3.11.5**
- **Dash 3.2.0** - Framework web para aplicaciones analíticas
- **Plotly 6.3.0** - Biblioteca de visualización interactiva
- **Polars 1.32.3** - Procesamiento rápido de datos
- **Pydantic Settings 2.10.1** - Gestión de configuración
- **Poetry** - Gestión de dependencias

## 📁 Estructura del Proyecto

```
Dashboard-mineria/
├── data/
│   ├── processed/
│   │   └── mineria_2021-2024.csv    # Datos procesados
│   └── raw/                         # Datos originales por año
├── src/dashboard_mineria/
│   ├── assets/
│   │   └── main.css                 # Estilos CSS
│   ├── config/
│   │   └── data.py                  # Configuración de datos
│   ├── app.py                       # Aplicación principal
│   ├── callback.py                  # Callbacks de interactividad
│   ├── kpi.py                       # Cálculo de KPIs
│   ├── layout.py                    # Estructura del dashboard
│   ├── loader.py                    # Carga de datos
│   └── plotly.py                    # Generación de gráficos
├── notebook/
│   └── mineria.ipynb               # Análisis exploratorio
├── .env                            # Variables de entorno
├── pyproject.toml                  # Configuración del proyecto
└── README.md                       # Este archivo
```

## ⚙️ Instalación

### Prerrequisitos

- Python 3.11.5 o superior
- Poetry (recomendado) o pip

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone <url-del-repositorio>
cd Dashboard-mineria
```

2. **Instalar dependencias con Poetry**
```bash
poetry install
```

O con pip:
```bash
pip install -r requirements.txt
```

3. **Configurar variables de entorno**

Crear un archivo `.env` en la raíz del proyecto:
```env
DATA_PATH=data/processed
FILE_NAME=mineria_2021-2024.csv
```

4. **Ejecutar la aplicación**
```bash
poetry run python src/dashboard_mineria/app.py
```

O directamente:
```bash
python src/dashboard_mineria/app.py
```

5. **Abrir en el navegador**
```
http://127.0.0.1:8050
```

## 📊 Uso del Dashboard

### Controles Disponibles

- **Dropdown Producto**: Seleccionar entre Cobre y Litio
- **Dropdown Año**: Filtrar por año (2021-2024)

### KPIs Mostrados

1. **FOB Total**: Valor total de exportaciones en millones de USD
2. **Peso Total**: Peso total exportado en toneladas
3. **Cantidad de Destinos**: Número de puertos de embarque únicos

### Visualizaciones

1. **Gráfico de Torta**: Muestra la distribución porcentual por país de destino
2. **Gráfico de Barras**: Presenta el monto FOB por puerto de embarque

## 🏗️ Arquitectura del Código

### Módulos Principales

#### `app.py`
Punto de entrada de la aplicación. Inicializa Dash y registra los callbacks.

#### `layout.py`
Define la estructura HTML del dashboard incluyendo sidebar, header, KPIs y gráficos.

#### `callback.py`
Contiene todas las funciones de callback que manejan la interactividad:
- Actualización de KPIs
- Actualización del header
- Actualización de gráficos

#### `kpi.py`
Funciones para calcular los indicadores clave:
- `calcular_fob()`: Calcula el monto FOB total
- `calcular_peso()`: Calcula el peso total
- `calcular_destinos()`: Cuenta destinos únicos

#### `plotly.py`
Generación de visualizaciones interactivas:
- `grafico_torta()`: Gráfico de distribución por países
- `grafico_barras()`: Gráfico de montos por puertos

#### `loader.py`
Carga eficiente de datos usando Polars.

#### `config/data.py`
Configuración de rutas y archivos mediante Pydantic Settings.

## 📈 Datos

### Fuente de Datos
Los datos provienen de registros oficiales de exportaciones mineras chilenas.

### Estructura de Datos
El archivo CSV procesado contiene las siguientes columnas:
- `Producto`: Tipo de mineral (Cobre, Litio)
- `Año`: Año de la exportación (2021-2024)
- `Monto Fob(US$)`: Valor FOB en dólares estadounidenses
- `Peso (Toneladas)`: Peso de la exportación en toneladas
- `Puerto de embarque`: Puerto de origen de la exportación
- `Pais de destino`: País de destino de la exportación

## 🎨 Personalización

### Estilos CSS
Los estilos se encuentran en `src/dashboard_mineria/assets/main.css` y se cargan automáticamente.

### Colores del Dashboard
La paleta de colores está definida en `plotly.py`:
```python
px.defaults.color_discrete_sequence = [
    "#0F766E", "#22C55E", "#0EA5E9", "#64748B", "#F59E0B", "#EF4444"
]
```

### Configuración de Gráficos
Los gráficos utilizan el tema `plotly_white` para un diseño limpio y profesional.

## 🧪 Testing

Para ejecutar pruebas (cuando estén implementadas):
```bash
poetry run pytest
```

## 📝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Cristian Orellana**
- GitHub: [@CristianNac](https://github.com/CristianNac/)
- LinkedIn: [cristian-o7](https://www.linkedin.com/in/cristian-o7/)

## 🙏 Agradecimientos

- Datos proporcionados por fuentes oficiales de exportaciones mineras de Chile
- Comunidad de Dash y Plotly por las excelentes herramientas
- Polars por el procesamiento eficiente de datos

---

⭐ Si este proyecto te resulta útil, ¡no olvides darle una estrella!