"""Módulo de visualizaciones para el Dashboard de Minería Chilena.

Este módulo contiene las funciones para generar gráficos interactivos
utilizando Plotly Express:
- Gráfico de torta: Distribución por país de destino
- Gráfico de barras: Monto FOB por puerto de embarque

Autor: Cristian Orellana
"""

import plotly.express as px
import polars as pl

from .loader import load_data

# Configuración global de tema y colores para Plotly
px.defaults.template = "plotly_white"
px.defaults.color_discrete_sequence = [
    "#0F766E", "#22C55E", "#0EA5E9", "#64748B", "#F59E0B", "#EF4444"
]
px.defaults.color_continuous_scale = px.colors.sequential.Blues


def _filtrar_paises(producto: str, anio: int) -> pl.DataFrame:
    """Filtra y agrupa los datos por país de destino para un producto y año específicos.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        pl.DataFrame: DataFrame con los top 5 países por monto FOB.
    """
    df = load_data()
    filtrar_producto = df.filter((pl.col('Producto') == producto) & (pl.col('Año') == anio))
    top_paises = filtrar_producto.group_by('Pais de destino').agg(
        pl.col('Monto Fob(US$)').sum().alias('Monto Fob(US$)')).sort(
            ['Monto Fob(US$)'], descending=[True]).head()
    return top_paises

def grafico_torta(producto: str, anio: int):
    """Genera un gráfico de torta con la distribución por país de destino.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        plotly.graph_objects.Figure: Gráfico de torta interactivo.
    """
    df = _filtrar_paises(producto, anio)
    orden = df.sort("Monto Fob(US$)", descending=True)["Pais de destino"].to_list()

    fig = px.pie(data_frame=df,
                 values='Monto Fob(US$)',
                 names='Pais de destino',
                 category_orders={"Pais de destino": orden},
                 title='Distribución por país de destino')
    
    # Destacar el país con mayor monto (primer elemento tras ordenar)
    pulls = [0.08] + [0] * (len(orden) - 1)

    fig.update_traces(
        sort=False,
        textinfo="percent",
        textposition="inside",
        pull=pulls,
        hovertemplate="<b>%{label}</b><br>FOB: %{value:$,.0f}<br>%{percent}",
        insidetextorientation="auto",
    )

    fig.update_layout(
        height=340,
        margin=dict(l=12, r=12, t=48, b=8),
        legend=dict(title=None, orientation="v", y=0.5, x=1.05),
    )
    return fig

def _filtrar_puertos(producto: str, anio: int) -> pl.DataFrame:
    """Filtra y agrupa los datos por puerto de embarque para un producto y año específicos.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        pl.DataFrame: DataFrame con los top 5 puertos por monto FOB.
    """
    df = load_data()
    filtrar_producto = df.filter((pl.col('Producto') == producto) & (pl.col('Año') == anio))
    top_puertos = filtrar_producto.group_by('Puerto de embarque').agg(
        pl.col('Monto Fob(US$)').sum().alias('Monto Fob(US$)')).sort(
            ['Monto Fob(US$)'], descending=[True]).head()
    return top_puertos

def grafico_barras(producto: str, anio: int):
    """Genera un gráfico de barras horizontales con el monto FOB por puerto de embarque.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        plotly.graph_objects.Figure: Gráfico de barras interactivo.
    """
    df = _filtrar_puertos(producto, anio)

    # Crear columna en millones para mostrar ejes "limpios"
    df = df.with_columns(
        (pl.col("Monto Fob(US$)") / 1_000_000).alias("Monto (MMUS$)")
    )

    orden = df.sort("Monto (MMUS$)", descending=True)["Puerto de embarque"].to_list()

    fig = px.bar(
        data_frame=df,
        x="Monto (MMUS$)",
        y="Puerto de embarque",
        orientation="h",
        category_orders={"Puerto de embarque": orden},
        title="Monto FOB por puerto de embarque (en millones US$)",
    )

    # Etiquetas numéricas sobre las barras
    fig.update_traces(
        texttemplate="%{x:,.0f}",
        textposition="outside",
        cliponaxis=False,
        hovertemplate="<b>%{y}</b><br>Monto: $%{x:,.0f} MMUS$",
    )

    # Configuración de ejes, grilla y márgenes
    fig.update_layout(
        height=340,
        margin=dict(l=16, r=16, t=48, b=10),
        xaxis=dict(
            showgrid=True,
            gridcolor="#EEF2F6",
            title="Monto FOB (MMUS$)",
            tickformat=",.0f",
        ),
        yaxis=dict(
            showgrid=False,
            title="Puerto de embarque",
        ),
    )
    return fig