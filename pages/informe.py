import streamlit as st
from streamlit_folium import st_folium
from pandas_handler import clean_df
from informes_handler import *
from web.style.style import titlo_principal_estilo, columna_izquierda_estilo, descripcion_estilo, derechos, h3_boxes, metric_explanation, boxes
from figures import *
from tools.data_frame_functions import return_deltas_violencia_mujer


st.markdown("""
    <style>
        body{
            background-color: #0e1117;
            color: #EAEAEA;
        }""", unsafe_allow_html=True)



# Título principal estilizado
st.markdown(titlo_principal_estilo, unsafe_allow_html=True
)

#estilo cajas
st.markdown(h3_boxes, unsafe_allow_html=True)

# Separación visual
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([0.65, 0.35], gap="small")

# Columna izquierda — DataFrame
with col1:
    st.markdown(columna_izquierda_estilo, unsafe_allow_html=True)

    st.dataframe(clean_df.head(7), width='stretch')




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

#Metricas - Pruebas

st.markdown("""<h2 style='text-align: center;'>Tendencia de Violencia contra la Mujer</h2>""", unsafe_allow_html=True)
totales, deltas = return_deltas_violencia_mujer()


n_cols = len(totales)

for i in range(0, len(totales), n_cols):
    cols = st.columns(n_cols)
    for j, col in enumerate(cols):
        idx = i + j
        if idx < len(totales):
            año = 2021 + idx  
            col.metric(f"Año {año}", round(totales[idx], 2), f"{int(deltas[idx])}%", border=True)



st.text_area('El ')

dp = st.selectbox("Seleccione el Departamento", informe_tendencia['DP'], index=0)
fig = tendencias(dp)

st.plotly_chart(fig, use_container_width=True)
st.markdown(metric_explanation, unsafe_allow_html=True)
st.markdown(derechos,unsafe_allow_html=True)
