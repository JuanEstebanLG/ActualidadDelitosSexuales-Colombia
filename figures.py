import pandas as pd
import plotly.express as px
import geopandas as gpd
from informes_handler import *
from pandas_handler import geo_url
import folium

figura = px.bar(informe_clasificacion_delitos_departamento, x='DP', y='CANTIDAD', title='Número de Delitos Sexuales por Departamento en Colombia (2025)',
            labels={'DP': '', 'CANTIDAD': 'Número de Delitos Sexuales'},
            color='CANTIDAD',
            color_continuous_scale='Viridis')


informe_clasificacion_delitos_departamento['DP'] = informe_clasificacion_delitos_departamento['DP'].replace({
    'GUAJIRA':'LA GUAJIRA',
    'SAN ANDRES':'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
    'NARINO':'NARIÑO',
    'VALLE':'VALLE DEL CAUCA',
    'BOGOTA D.C': 'SANTAFE DE BOGOTA D.C'
})

def get_mapa():


    m = folium.Map(location = [4.5, -74.1], zoom_start = 5)

    choropleth = folium.Choropleth(
        geo_data=geo_url,
        data=informe_clasificacion_delitos_departamento,
        columns=['DP', 'CANTIDAD'],
        key_on="feature.properties.NOMBRE_DPT",
        name='Delitos',
        fill_color="Reds",
        fill_opacity=0.7,
        line_opacity=0.3,
        legend_name="Casos registrados",
        highlight=True,
        tile = None
    ).add_to(m)

    folium.TileLayer(
        tiles='CartoDB positron',
        name='CartoDB Positron',
        attr='© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, © <a href="https://carto.com/attribution">CARTO</a>'
    ).add_to(m)

    folium.TileLayer(
        tiles='CartoDB dark_matter',
        name='CartoDB Dark Matter',
        attr='© OpenStreetMap contributors, © CARTO'
    ).add_to(m)


    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google',
        name='Google Satellite',
        overlay=False,
        control=True
    ).add_to(m)

    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
    ).add_to(m)

    folium.LayerControl().add_to(m)

    map_object = m
    return map_object
