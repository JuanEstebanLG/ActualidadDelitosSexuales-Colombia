import pandas as pd
import plotly.express as px
from informes_handler import *
from pandas_handler import geo_url
import folium

figura = px.bar(informe_clasificacion_delitos_departamento, x='DP', y='CANTIDAD', title='Número de Delitos Sexuales por Departamento en Colombia (2025)',
            labels={'DP': '', 'CANTIDAD': 'Número de Delitos Sexuales'},
            color='CANTIDAD',
            color_continuous_scale='ice')


informe_clasificacion_delitos_departamento['DP'] = informe_clasificacion_delitos_departamento['DP'].replace({
    'GUAJIRA':'LA GUAJIRA',
    'SAN ANDRES':'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
    'NARINO':'NARIÑO',
    'VALLE':'VALLE DEL CAUCA',
    'BOGOTA D.C': 'SANTAFE DE BOGOTA D.C'
})



armas_mas_usadas =  px.bar(informe_armas_mas_usadas, x='ARMAS', y = 'CANTIDAD', title ='Reporte del Uso de Armas',
                      color = 'ES_MAX', #Necesario para pintar la barra más grande
                      color_discrete_map = {
                          'ARMA MAS USADA':'#0c0e36', #COLOR SELECCIONADO PARA LA COLUMNA MÁS GRANDE
                          'ARMAS SECUNDARIAS':'#59f08e'
                      },
                      text='CANTIDAD',
                      labels = {
                          'ARMAS': 'TIPO DE ARMA',
                          'CANTIDAD': 'CANTIDAD REPORTADA',
                          'ES_MAX':'MAYOR USO',
                          'MAXIMO':'TIPO DE ARMA MÁS USADA',
                          'NO_MAXIMO':'ARMÁS SECUNDARIAS'
                      },
                      hover_data={'ARMAS': True, 'CANTIDAD': True, 'ES_MAX': False} #Esto se utiliza para controlar que se muestra al hacer uso del hover de plotly
                      )

armas_mas_usadas.update_traces(
    textposition='outside',  # coloca el texto fuera de la barra (Esto antes lo tenia que hacer usando un ciclo FOR )


)

armas_mas_usadas.update_layout(
    height=700,
    width=1200,
    uniformtext_minsize=8,  # tamaño uniforme mínimo
    uniformtext_mode='hide' # oculta texto si se superpone
)



figure_pie = px.pie(informe_grupo_mas_afectado,values = 'CANTIDAD', names = 'GRE', title = 'Grupo de Edad Más Afectado',
                    color_discrete_sequence=px.colors.sequential.Aggrnyl,
                    width = 800,
                    height = 600,
                    )


figure_pie.update_traces(
    textposition='inside',
    textinfo = 'percent+label',
)

figure_pie.update_layout (
    uniformtext_minsize=16,
    uniformtext_mode='hide'
)


genero_pie = px.pie(informe_genero_mas_afectado, values='CANTIDAD', names='GENERO',
                    color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=600)

genero_pie.update_traces(
    textposition='inside',
    textinfo='percent+label',
)

genero_pie.update_legends(
    title_text='Género Reportado',
    x = 0,
)

genero_pie.update_layout(
    uniformtext_minsize=16,
    uniformtext_mode='hide'
)


def get_mapa():

    m = folium.Map(location=[4.5, -74.1], zoom_start=5)

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
        tile=None
    ).add_to(m)

    cantidad_map = dict(
        zip(
            informe_clasificacion_delitos_departamento['DP'],
            informe_clasificacion_delitos_departamento['CANTIDAD']
        )
    )

 
    for feature in choropleth.geojson.data['features']:
        nombre = feature['properties']['NOMBRE_DPT']
        feature['properties']['CANTIDAD'] = int(cantidad_map.get(nombre, 0))

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(
            fields=['NOMBRE_DPT', 'CANTIDAD'],
            aliases=['Departamento:', 'Casos reportados:'],
            localize=True,
            sticky=True,
            labels=True
        )
    )

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
