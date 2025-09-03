"""Módulo de layout para el Dashboard de Minería Chilena.

Este módulo define la estructura visual completa del dashboard, incluyendo:
- Sidebar con controles de filtrado
- Header con información del producto y año seleccionado
- KPIs principales (FOB total, Peso total, Cantidad de destinos)
- Gráficos de visualización (torta y barras)

Autor: Cristian Orellana
"""

from dash import html, dcc
from dash_ag_grid import AgGrid


layout = html.Div(className='Todo',children=[

    #Sidebar
    html.Div(className='sidebar',children=[
        html.H2('Controles'),

        dcc.Dropdown(id="dropdown-producto",
                     options =[
                         {'label':'Cobre','value':'Cobre'},
                         {'label':'Litio','value':'Litio'},
                     ], value = 'Cobre',
                        className="control"),

        dcc.Dropdown(id="dropdown-anio",
                     options = [
                         {'label':2021,'value':2021},
                         {'label':2022,'value':2022},
                         {'label':2023,'value':2023},
                         {'label':2024,'value':2024}
                     ], value = 2024,
                        className='control'),
        
        html.Div(className='about-me', children=[
            html.H3('Sobre mí'),
            html.P("👨‍💻 Data Scientist enfocado en Python, SQL, Docker y GCP. "
                   "Apasionado por transformar datos en valor y construir dashboards interactivos."),
        ]),
        html.Div(className='spacer'),

        html.H3('Creado por: Cristian Orellana'),
        html.Div(className='social', children=[
            html.A('Github',href='https://github.com/CristianNac/',target='_blank'),
            html.A('Linkedin',href='https://www.linkedin.com/in/cristian-o7/',target='_blank')])
        ]),

    #Header
    html.Div(className='header',children=[
        html.H1('Dashboard Minería chilena'), 
        html.Div(className='etiquetaHeader',
            children=[html.H3(id='header-producto',children='Producto: Cobre')]), 
        html.Div(className='etiquetaHeader', 
            children=[html.H3(id='header-anio',children='Año: 2024')]),
            ]),

    #KPI
    html.Div(className='KPI',children=[
        html.Div(className='KPI1',children=[
            html.Span('FOB total',className='kpi-label'),
            html.H2(id='kpi-fob', className='kpi-value')]),
        html.Div(className='KPI2',children=[
            html.Span('Peso total',className='kpi-label'),
            html.H2(id='kpi-peso', className='kpi-value')]),
        html.Div(className='KPI3',children=[
            html.Span('Cantidad de destinos',className='kpi-label'),
            html.H2(id='kpi-destinos', className='kpi-value')])
        ]),

    #Grafico1
    html.Div(className='Graficos1',children=[
        html.Div(className='Grafico-torta',children=[dcc.Graph(id='Grafico-torta',
                                                               config = {'displayModeBar':False})]),
        html.Div(className='Grafico-barra',children=[dcc.Graph(id='Grafico-barra',
                                                               config={'displayModeBar':False})])
        
        ]),


])