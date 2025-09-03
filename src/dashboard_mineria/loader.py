"""Módulo de carga de datos para el Dashboard de Minería Chilena.

Este módulo se encarga de cargar los datos procesados de exportaciones
mineras desde archivos CSV utilizando Polars para un procesamiento eficiente.

Autor: Cristian Orellana
"""

import polars as pl
from pydantic import DirectoryPath

from .config import data_settings


def load_data(data_path: DirectoryPath = data_settings.data_path,
              file_name: str = data_settings.file_name) -> pl.DataFrame:
    """Carga los datos de exportaciones mineras desde un archivo CSV.
    
    Args:
        data_path (DirectoryPath): Ruta del directorio donde se encuentra el archivo.
                                  Por defecto usa la configuración global.
        file_name (str): Nombre del archivo CSV a cargar.
                        Por defecto usa la configuración global.
                        
    Returns:
        pl.DataFrame: DataFrame de Polars con los datos de exportaciones mineras.
        
    Note:
        Los datos deben contener las columnas:
        - Producto: Tipo de mineral (Cobre, Litio)
        - Año: Año de la exportación
        - Monto Fob(US$): Valor FOB en dólares
        - Peso (Toneladas): Peso de la exportación
        - Puerto de embarque: Puerto de origen
        - Pais de destino: País de destino
    """
    return pl.scan_csv(f'{data_path}/{file_name}').collect()

