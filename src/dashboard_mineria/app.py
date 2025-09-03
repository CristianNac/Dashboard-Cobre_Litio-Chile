"""Aplicación principal del Dashboard de Minería Chilena.

Este módulo inicializa la aplicación Dash, configura el layout
y registra los callbacks para la interactividad del dashboard.

El dashboard permite visualizar datos de exportaciones mineras
chilenas de Cobre y Litio entre 2021-2024.

Autor: Cristian Orellana
"""

from dash import Dash

from .callback import register_callbacks
from .layout import layout

# Inicializar aplicación Dash
app = Dash(__name__)

# Configurar layout y callbacks
app.layout = layout
register_callbacks(app)

server = app.server

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=False)