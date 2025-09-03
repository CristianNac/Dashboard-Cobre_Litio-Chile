# Changelog

Todos los cambios notables de este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-12-19

### Añadido
- Dashboard interactivo inicial con Dash y Plotly
- Filtros por producto (Cobre/Litio) y año (2021-2024)
- KPIs principales: FOB total, Peso total, Cantidad de destinos
- Gráfico de torta para distribución por país de destino
- Gráfico de barras para monto FOB por puerto de embarque
- Procesamiento de datos con Polars
- Configuración mediante variables de entorno con Pydantic
- Estructura modular del código
- Documentación completa con docstrings
- Estilos CSS personalizados
- Información del autor en el sidebar

### Técnico
- Implementación de callbacks para interactividad
- Carga eficiente de datos CSV
- Formateo de números con separadores de miles
- Configuración de tema y colores para gráficos
- Manejo de casos edge (datos vacíos)
- Arquitectura modular y escalable