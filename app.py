import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import folium as folium
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
from pandas_handler import clean_df
from informes_handler import informe_clasificacion_delitos_departamento
from figures import *
from web.style.style import *



#STREAMLIT APP

st.set_page_config(page_title="Análisis de Delitos Sexuales en Colombia", layout="wide", initial_sidebar_state="collapsed",
                   page_icon=":bar_chart:")


#ESPACIO PARA ESTILOS

#Estilo para Cajas de Texto h3
st.markdown(h3_boxes, unsafe_allow_html=True)



with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Inicio", "Información", "Sobre el Equipo"],
        icons=["house", "table", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Inicio":

    st.set_page_config(layout='centered')
    st.image('resources/images/fondo_inicio.jpg', width='content')
    st.title("Página de Inicio", width='content')

    


    numero_1 = st.number_input('ingrese un Numero', key='num1')
    numero_2 = st.number_input('ingrese un Numero', key='num2')

    try:
        resultado = numero_1 + numero_2
        st.text(f'El resultado de la suma es: {resultado}')
    except Exception as e:  
        st.text(f'Ocurrio un error: {e}')

    st.divider()


    st.text('Con botones:')


    numero_2 = st.number_input('ingrese un Numero', key='num3')
    numero_3 = st.number_input('ingrese un Numero', key='num4')


    if st.button('Sumar'):
        try:
            resultado = numero_2 + numero_3
            st.text(f'El resultado de la suma es: {resultado}')
        except Exception as e:  
            st.text(f'Ocurrio un error: {e}')

    st.divider()
elif selected == "Información":
    # Título principal estilizado
    st.markdown(titlo_principal_estilo, unsafe_allow_html=True
    )

    # Separación visual
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Columna izquierda — DataFrame
    with col1:
        st.markdown(columna_izquierda_estilo, unsafe_allow_html=True)

        st.dataframe(clean_df, use_container_width=True)


    st.markdown(derechos,unsafe_allow_html=True
        )

    # Columna derecha — Descripcion
    with col2:
        st.markdown(descripcion_estilo, unsafe_allow_html=True)
    departamento_mayor = informe_clasificacion_delitos_departamento.iloc[0]['DP']
    departamento_menor = informe_clasificacion_delitos_departamento.iloc[-1]['DP']
    mediana = informe_clasificacion_delitos_departamento['CANTIDAD'].median()

    st.markdown(boxes(departamento_mayor, departamento_menor, mediana), unsafe_allow_html=True)
    st.plotly_chart(figura, width='stretch')


    #Mapa

    mapa = get_mapa()
    st_folium(mapa, width='stretch', key='mapa_delitos', returned_objects=[])
