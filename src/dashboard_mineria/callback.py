"""Módulo de callbacks para el Dashboard de Minería Chilena.

Este módulo contiene todas las funciones de callback que manejan
la interactividad del dashboard, incluyendo:
- Actualización de KPIs basada en filtros
- Actualización del header con producto y año seleccionado
- Actualización de gráficos según los filtros aplicados

Autor: Cristian Orellana
"""

import plotly.express as px
from dash import html
from dash.dependencies import Input, Output

from .kpi import calcular_fob, calcular_peso, calcular_destinos
from .plotly import grafico_barras, grafico_torta


def register_callbacks(app):
    """Registra todos los callbacks de la aplicación Dash.
    
    Args:
        app: Instancia de la aplicación Dash donde se registrarán los callbacks.
    """

    def _fmt_int(n):
        """Formatea números enteros con separadores de miles.
        
        Args:
            n (float): Número a formatear.
            
        Returns:
            str: Número formateado con puntos como separadores de miles.
        """
        return f"{int(round(n)):,}".replace(",", ".")

    @app.callback(
        [Output("kpi-fob", "children"),
         Output("kpi-peso", "children"),
         Output("kpi-destinos", "children")],
        [Input("dropdown-producto", "value"),
         Input("dropdown-anio", "value")]
    )
    def actualizar_kpis(producto, anio):
        """Actualiza los KPIs del dashboard basado en los filtros seleccionados.
        
        Args:
            producto (str): Producto minero seleccionado ('Cobre' o 'Litio').
            anio (int): Año seleccionado (2021-2024).
            
        Returns:
            tuple: Tupla con tres elementos (fob_children, peso_children, destinos_children)
                   cada uno conteniendo el valor formateado y su unidad.
        """
        if not producto or anio is None:
            guion = ["-", html.Small("")]
            return guion, guion, guion

        fob_total_usd = calcular_fob(producto, anio)      # en US$
        peso_total_ton = calcular_peso(producto, anio)     # en Toneladas
        destinos = calcular_destinos(producto, anio)       # entero

        # Formateos:
        # FOB en millones de USD
        fob_children = [_fmt_int(fob_total_usd / 1_000_000), html.Small("MMUS$")]
        # Peso en toneladas (entero)
        peso_children = [_fmt_int(peso_total_ton), html.Small("Toneladas")]
        # Destinos (entero)
        destinos_children = [_fmt_int(destinos), html.Small("Destinos")]

        return fob_children, peso_children, destinos_children
    
    @app.callback(
        [Output("header-producto","children"),
        Output("header-anio","children")],
        [Input("dropdown-producto","value"),
        Input("dropdown-anio","value")]
    )

    def actualizar_header(producto, anio):
        """Actualiza el header del dashboard con el producto y año seleccionados.
        
        Args:
            producto (str): Producto minero seleccionado.
            anio (int): Año seleccionado.
            
        Returns:
            tuple: Tupla con los textos formateados para el header.
        """
        return f'Producto: {producto}', f'Año: {anio}'
    
    @app.callback(
        [Output("Grafico-torta", "figure"),
         Output("Grafico-barra", "figure")],
        [Input("dropdown-producto", "value"),
         Input("dropdown-anio", "value")]
    )
    def actualizar_graficos(producto, anio):
        """Actualiza los gráficos del dashboard basado en los filtros seleccionados.
        
        Args:
            producto (str): Producto minero seleccionado.
            anio (int): Año seleccionado.
            
        Returns:
            tuple: Tupla con las figuras de Plotly (grafico_torta, grafico_barras).
        """
        if not producto or anio is None:
            # figuras vacías si aún no hay selección
            return px.pie(), px.bar()
        return grafico_torta(producto, anio), grafico_barras(producto, anio)
    
    
