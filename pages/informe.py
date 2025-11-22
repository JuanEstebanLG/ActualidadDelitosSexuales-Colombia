import streamlit as st
from streamlit_folium import st_folium
from pandas_handler import clean_df
from informes_handler import *
from web.style.style import  main_estilo, columna_izquierda_estilo, descripcion_estilo, derechos, h3_boxes, metric_explanation, violencia_genero, boxes
from figures import *
from tools.data_frame_functions import return_deltas_violencia_mujer


# Hero Principal
st.markdown(main_estilo, unsafe_allow_html=True, width='stretch')

#estilo cajas
st.markdown(h3_boxes, unsafe_allow_html=True)

# Separación visual
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([0.65, 0.35], gap="small")

# Columna izquierda — DataFrame
with col1:
    st.markdown(columna_izquierda_estilo, unsafe_allow_html=True)

    st.dataframe(clean_df.head(6), width='stretch')




# Columna derecha — Descripcion
with col2:
    st.markdown(descripcion_estilo, unsafe_allow_html=True)


departamento_mayor = informe_clasificacion_delitos_departamento.iloc[0]['DP']
departamento_menor = informe_clasificacion_delitos_departamento.iloc[-1]['DP']
mediana = informe_clasificacion_delitos_departamento['CANTIDAD'].median()


st.markdown(boxes(departamento_mayor, departamento_menor, mediana), unsafe_allow_html=True)
st.plotly_chart(figura, width='stretch')



########################################################## MAPA ##########################################################

st.divider()

col_mapa, col_mapa_desc = st.columns([0.7, 0.3], gap="small")

with col_mapa:
#Mapa - Prueba Folium
    mapa = get_mapa()
    st_folium(mapa, width='stretch', height=600, key='mapa_delitos', returned_objects=[])

with col_mapa_desc:
    st.title("🗺️ Mapa de Delitos Sexuales en Colombia")
    st.write("""Distribución geográfica de los delitos sexuales reportados en colombia hasta mayo de 2025. 
             En el mapa, los departamentos coloreados en rojo indican un mayor reporte de estos delitos, la escala baja atenuando el color hasta el blanco """)

st.divider()

col_armas_desc, col_armas = st.columns([0.3, 0.7], gap="small")

with col_armas_desc:
    st.title("Uso de Armas")
    st.write("""Análisis de las armas más utilizadas en la comisión de delitos sexuales en Colombia. 
             El gráfico de barras destaca el arma más empleada en comparación con otras armas secundarias, proporcionando una visión clara de las tendencias en el uso de armas en estos delitos.""")
    
with col_armas:
    st.plotly_chart(armas_mas_usadas, width='stretch')

st.divider()

col_gre, col_gre_desc = st.columns([0.7, 0.3], gap="small")

with col_gre:
    st.plotly_chart(figure_pie, width='stretch')

with col_gre_desc:
    st.title("Grupo de Edad Más Afectado")
    st.write("""Distribución de los delitos sexuales en Colombia según el grupo de edad de las víctimas. Este gráfico circular muestra qué rangos etarios concentran la mayor carga de casos, evidenciando qué grupos poblacionales se encuentran en mayor situación de vulnerabilidad. 
             La visualización permite identificar tendencias demográficas críticas, como la afectación en niñas, niños, adolescentes, personas adultas o personas mayores, y aporta insumos esenciales para el diseño de acciones preventivas, programas de protección focalizada y políticas públicas que respondan a las necesidades específicas de cada etapa del ciclo de vida.""")    

st.divider()
################################ GÉNERO MÁS AFECTADO #################################################


col_genero_desc, col_genero = st.columns([0.3, 0.7], gap="small")


with col_genero_desc:
    st.title("Delitos Sexuales por Género")
    st.write("""Análisis de la distribución de delitos sexuales en Colombia según el género de las víctimas. Este gráfico circular permite identificar con claridad qué géneros concentran la mayor proporción de casos reportados, visibilizando posibles desigualdades y patrones de victimización diferenciada. Al observar estas proporciones, se facilita la comprensión de cómo el género se relaciona con la incidencia de los delitos sexuales, lo que resulta clave para orientar estrategias de prevención, atención integral y formulación de políticas públicas con enfoque de género.""")

with col_genero:
    st.plotly_chart(genero_pie, width='stretch')


st.divider()
################################ TENDENCIA VIOLENCIA CONTRA LA MUJER #################################################


st.markdown(violencia_genero, unsafe_allow_html=True)

st.markdown("""<br></br><h2 style='text-align: center;'>Tendencia de Violencia contra la Mujer</h2>""", unsafe_allow_html=True)
totales, deltas = return_deltas_violencia_mujer()

tendencias_mostrar = st.checkbox("Mostrar Métricas de Violencia contra la Mujer", value=True, key='toggle_metrics')

if tendencias_mostrar:

    
    n_cols = len(totales)

    for i in range(0, len(totales), n_cols):
        cols = st.columns(n_cols)
        for j, col in enumerate(cols):
            idx = i + j
            if idx < len(totales):
                año = 2019 + idx  
                col.metric(f"Año {año}", round(totales[idx]), f"{int(deltas[idx])}%", border=True)

    st.markdown(metric_explanation, unsafe_allow_html=True)

st.divider()
st.title("Delitos Sexuales por Departamento - Tendencias 2010-2025")

dp = st.selectbox("Seleccione el Departamento", informe_tendencia['DP'], index=0)
fig = tendencias(dp)

st.plotly_chart(fig, width='stretch')

st.markdown(derechos,unsafe_allow_html=True)
