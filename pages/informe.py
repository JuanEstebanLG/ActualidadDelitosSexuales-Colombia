import streamlit as st
from streamlit_folium import st_folium
from pandas_handler import clean_df
from informes_handler import *
from web.style.style import main_estilo, columna_izquierda_estilo, descripcion_estilo, derechos, h3_boxes, metric_explanation, violencia_genero, componente_feminicidios, componente_tendencia_fem, metric_info_gen, componente_genero, componente_armas, componente_edad, componente_mapa, boxes
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
    st.markdown(componente_mapa, unsafe_allow_html=True)

st.divider()

col_armas_desc, col_armas = st.columns([0.3, 0.7], gap="small")

with col_armas_desc:
    st.markdown(componente_armas, unsafe_allow_html=True)
with col_armas:
    st.plotly_chart(armas_mas_usadas, width='stretch')

st.divider()

col_gre, col_gre_desc = st.columns([0.7, 0.3], gap="small")

with col_gre:
    st.plotly_chart(figure_pie, width='stretch')

with col_gre_desc:
    st.markdown(componente_edad, unsafe_allow_html=True)
st.divider()
################################ GÉNERO MÁS AFECTADO #################################################


col_genero_desc, col_genero = st.columns([0.3, 0.7], gap="small")


with col_genero_desc:
    st.markdown(componente_genero, unsafe_allow_html=True)
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


col_femi, col_femi_desc = st.columns([0.72, 0.28], gap="small")



with col_femi:
    st.plotly_chart(feminicidios_por_departamento, width='stretch')

with col_femi_desc:
    st.markdown(componente_feminicidios, unsafe_allow_html=True)


st.divider()

st.markdown(componente_tendencia_fem , unsafe_allow_html=True)

st.divider()
dp_fem = st.selectbox("Seleccione el Departamento para ver la tendencia de Feminicidios", informe_feminicidios_departamento_ano['DP'], index=0, key='select_fem_trend')
fem_fig = tedencias_feminicidios(dp_fem)
st.plotly_chart(fem_fig, width='stretch')
st.markdown(metric_info_gen, unsafe_allow_html=True)
st.divider()

st.title("Delitos Sexuales por Departamento - Tendencias 2010-2025")

dp = st.selectbox("Seleccione el Departamento", informe_tendencia['DP'], index=0)
fig = tendencias(dp)
st.plotly_chart(fig, width='stretch')
st.markdown(metric_info_gen, unsafe_allow_html=True)
st.markdown(derechos,unsafe_allow_html=True)
