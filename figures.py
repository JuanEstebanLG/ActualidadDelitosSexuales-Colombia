import pandas as pd
import plotly.express as px
from informes_handler import *
from pandas_handler import geo_url
import folium

def tendencias(departamento):

    fila = informe_tendencia[informe_tendencia['DP'] == departamento]

    fila_long = fila.melt(id_vars='DP', var_name='Año', value_name='Valor')

    fig = px.line(
        fila_long,
        x='Año',
        y='Valor',
        title=f'Evolución por año - Departamento de {departamento}',
        markers=True,
        template='plotly_dark'
    )

    fig.add_vline(
        x=2020,
        line_width=2,
        line_dash="dash",
        line_color="crimson"
    )

    fig.add_vline(
        x=2023,
        line_width=2,
        line_dash="dash",
        line_color="crimson"
    )

    fig.add_annotation(
        x=2020,
        yref="paper",   
        y=1.05,         
        text="Inicio pandemia",
        showarrow=False,
        font=dict(size=12, color="crimson")
    )

    fig.add_annotation(
        x=2023,
        yref="paper",   
        y=1.05,         
        text="Fundación: Ministerio de Igualdad y Equidad",
        showarrow=False,
        font=dict(size=12, color="crimson")
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=7)
    )

    fig.update_layout(
        title_font=dict(size=20, family="Arial"),
        xaxis_title="Año",
        yaxis_title="Valor",
        hovermode="x unified",
        xaxis=dict(
            showgrid=False,
            dtick=1,          # un año por tick
            tickangle=-45
        ),
        yaxis=dict(
            zeroline=False,
            gridcolor="rgba(0,0,0,0.1)"
        ),
        margin=dict(l=50, r=30, t=80, b=60),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig

def tedencias_feminicidios(departamento):
    fila = informe_feminicidios_departamento_ano[informe_feminicidios_departamento_ano['DP'] == departamento]

    fila_long = fila.melt(id_vars='DP', var_name='Año', value_name='Valor')

    fig = px.line(
        fila_long,
        x='Año',
        y='Valor',
        title=f'Victimas Femeninas por Año - Departamento de {departamento}',
        markers=True,
        template='plotly_dark',
        color_discrete_sequence=["#f768a1"]
    )


    fig.add_vline(
        x=2020,
        line_width=2,
        line_dash="dash",
        line_color="#ae017e"  
    )

    fig.add_vline(
        x=2023,
        line_width=2,
        line_dash="dash",
        line_color="#ae017e"
    )

    fig.add_annotation(
        x=2020,
        yref="paper",
        y=1.05,
        text="Inicio pandemia",
        showarrow=False,
        font=dict(size=12, color="#f768a1")
    )

    fig.add_annotation(
        x=2023,
        yref="paper",
        y=1.05,
        text="Fundación: Ministerio de Igualdad y Equidad",
        showarrow=False,
        font=dict(size=12, color="#f768a1")
    )

  
    fig.update_traces(
        line=dict(width=3, color="#f768a1"),
        marker=dict(size=7, color="#dd3497")
    )

    fig.update_layout(
        title_font=dict(size=20, family="Arial"),
        xaxis_title="Año",
        yaxis_title="Valor",
        hovermode="x unified",
        xaxis=dict(
            showgrid=False,
            dtick=1,
            tickangle=-45
        ),
        yaxis=dict(
            zeroline=False,
            gridcolor="rgba(0,0,0,0.1)"
        ),
        margin=dict(l=50, r=30, t=80, b=60),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig


BluesMore = [
    "rgb(222,233,255)",
    "rgb(197,217,247)",
    "rgb(173,201,239)",
    "rgb(133,184,225)",
    "rgb(92,164,219)",
    "rgb(51,136,203)",
    "rgb(18,103,186)",
    "rgb(0,71,161)",
    "rgb(0,38,112)",
]

px.colors.sequential.BluesMore = BluesMore


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
                          'ARMA MAS USADA':"#bb4244", #COLOR SELECCIONADO PARA LA COLUMNA MÁS GRANDE
                          'ARMAS SECUNDARIAS':"#463E67"
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
                    color_discrete_sequence=px.colors.sequential.YlOrBr,
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
                    color_discrete_sequence=BluesMore, width=800, height=600)

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



feminicidios_por_departamento = px.bar(informe_feminicidios_departamento, x='DP', y='CANTIDAD',
                                       title='Número de Feminicidios por Departamento en Colombia (2025)',
                                       labels={'DP': '', 'CANTIDAD': 'Número de Feminicidios'},
                                       color='CANTIDAD',
                                       color_continuous_scale='RdPu',)





############################# FEMINICIDIOS POR DEPARTAMENTO Y AÑO ############################



