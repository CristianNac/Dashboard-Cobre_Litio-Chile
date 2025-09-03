"""Módulo de configuración para el Dashboard de Minería Chilena.

Este módulo define la configuración para la carga de datos,
incluyendo rutas de archivos y nombres de archivos que se
cargan desde variables de entorno.

Autor: Cristian Orellana
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class DataSettings(BaseSettings):
    """Configuración para la carga de datos del dashboard.
    
    Attributes:
        data_path (DirectoryPath): Ruta del directorio donde se encuentran los datos.
        file_name (str): Nombre del archivo CSV con los datos procesados.
    """
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    
    data_path: DirectoryPath
    file_name: str


# Instancia global de configuración
data_settings = DataSettings()
