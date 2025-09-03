"""Módulo de cálculo de KPIs para el Dashboard de Minería Chilena.

Este módulo contiene las funciones para calcular los indicadores
clave de rendimiento (KPIs) del dashboard:
- FOB total en dólares estadounidenses
- Peso total en toneladas
- Cantidad de destinos únicos

Autor: Cristian Orellana
"""

import polars as pl

from .loader import load_data


def _filtrar_producto(producto: str, anio: int):
    """Filtra los datos por producto y año especificados.
    
    Args:
        producto (str): Nombre del producto minero ('Cobre' o 'Litio').
        anio (int): Año de los datos (2021-2024).
        
    Returns:
        pl.DataFrame: DataFrame filtrado con los datos del producto y año especificados.
    """
    df = load_data()
    filtrar_producto = df.filter((pl.col('Producto') == producto) & (pl.col('Año') == anio))
    return filtrar_producto


def calcular_fob(producto: str, anio: int) -> float:
    """Calcula el monto FOB total para un producto y año específicos.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        float: Monto FOB total en dólares estadounidenses.
    """
    df = _filtrar_producto(producto, anio)

    if df.is_empty():
        return 0.0
    
    fob_anual = (df.select(pl.col('Monto Fob(US$)').sum().alias(
        'fob_total')).to_series(0).item())
        
    return float(fob_anual)


def calcular_peso(producto: str, anio: int) -> float:
    """Calcula el peso total para un producto y año específicos.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        float: Peso total en toneladas.
    """
    df = _filtrar_producto(producto, anio)
    peso_total = (df.select(pl.col('Peso (Toneladas)').sum().alias('peso_total')).to_series(0).item())
   
    return peso_total


def calcular_destinos(producto: str, anio: int) -> int:
    """Calcula la cantidad de destinos únicos para un producto y año específicos.
    
    Args:
        producto (str): Nombre del producto minero.
        anio (int): Año de los datos.
        
    Returns:
        int: Número de puertos de embarque únicos.
    """
    df = _filtrar_producto(producto, anio)
    total_destinos = df.select(pl.col('Puerto de embarque').n_unique()).item()
    return total_destinos

