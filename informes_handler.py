import plotly.express as px
import pandas as pd
import geopandas as gpd
from pandas_handler import clean_df


df_informe = clean_df

df_informe['DP'] = (
    df_informe['DP']
    .str.upper()
    .str.normalize('NFKD')
    .str.encode('ascii', errors='ignore')
    .str.decode('utf-8')
)

df_informe['MUNICIPIO'] = (
    df_informe['MUNICIPIO']
    .str.upper()
    .str.normalize('NFKD')
    .str.encode('ascii', errors='ignore')
    .str.decode('utf-8')
    .str.strip()
)



df_informe.loc[df_informe['MUNICIPIO'] == 'BOGOTA D.C. (CT)', 'DP'] = 'BOGOTA D.C'



informe_clasificacion_delitos_departamento = df_informe.groupby('DP')['CANTIDAD'].sum().sort_values(ascending = False).reset_index(drop=False)


informe_escopolamina_por_departamento = df_informe[df_informe['ARMAS'] == 'ESCOPOLAMINA'].groupby('DP')['ARMAS'].count().sort_values(ascending = False).reset_index(drop=False)


informe_escopolamina_por_departamento['DP'] = informe_escopolamina_por_departamento['DP'].replace({
    'GUAJIRA':'LA GUAJIRA',
    'SAN ANDRES':'ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA',
    'NARINO':'NARIÑO',
    'VALLE':'VALLE DEL CAUCA',
    'BOGOTA D.C': 'SANTAFE DE BOGOTA D.C'
})

informe_armas_mas_usadas = df_informe[df_informe['ARMAS'] != 'NO REPORTADO'].groupby('ARMAS')['CANTIDAD'].sum().sort_values(ascending= False)

informe_armas_mas_usadas = informe_armas_mas_usadas.reset_index(drop= False)

max_cantidad = informe_armas_mas_usadas['CANTIDAD'].max()

informe_armas_mas_usadas['ES_MAX'] = informe_armas_mas_usadas['CANTIDAD'].apply(
    lambda x: 'ARMA MAS USADA' if x == max_cantidad else 'ARMAS SECUNDARIAS'
)

#Aca se crea la visualización, para colorear simplemente usemos la bandera anterior como parametro
figure_armas = px.bar(informe_armas_mas_usadas, x='ARMAS', y = 'CANTIDAD', title ='Reporte del Uso de Armas',
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

figure_armas.update_traces(
    textposition='outside',  # coloca el texto fuera de la barra (Esto antes lo tenia que hacer usando un ciclo FOR )


)

figure_armas.update_layout(
    height=700,
    width=1200,
    uniformtext_minsize=8,  # tamaño uniforme mínimo
    uniformtext_mode='hide' # oculta texto si se superpone
)

############################ ARMAS MÁS USADAS ############################
informe_armas_mas_usadas = df_informe[df_informe['ARMAS'] != 'NO REPORTADO'].groupby('ARMAS')['CANTIDAD'].sum().sort_values(ascending= False).reset_index(drop= False)
max_cantidad = informe_armas_mas_usadas['CANTIDAD'].max()
informe_armas_mas_usadas['ES_MAX'] = informe_armas_mas_usadas['CANTIDAD'].apply(
    lambda x: 'ARMA MAS USADA' if x == max_cantidad else 'ARMAS SECUNDARIAS'
)

############################ GRUPO DE EDAD MÁS AFECTADO ############################
informe_grupo_mas_afectado = df_informe[df_informe['GRE'] != 'NO REPORTADO'].groupby('GRE')['CANTIDAD'].sum().sort_values(ascending=False)
informe_grupo_mas_afectado = informe_grupo_mas_afectado.reset_index(drop = False)


############################# VIOLENCIA A LA MUJER ############################

#------------------------------ FEMENINO VS MASCULINO ------------------------------ (Motivación de la proxima consulta)


informe_genero_mas_afectado = df_informe[(df_informe['GENERO'] != 'NO REPORTADO')  & (df_informe['GENERO'] != 'NO REPORTA')].groupby('GENERO')['CANTIDAD'].sum().sort_values(ascending=False).reset_index(drop = False)


informe_violencia_a_la_mujer = df_informe[df_informe['GENERO' \
''] == 'FEMENINO'].pivot_table(
    index='GENERO',
    columns='AÑO',
    values='CANTIDAD',
    aggfunc='sum',
).reset_index(drop=False)

informe_violencia_a_la_mujer = df_informe[df_informe['GENERO'] == 'FEMENINO'].pivot_table(
    index='GENERO',
    columns='AÑO',
    values='CANTIDAD',
    aggfunc='sum',
).reset_index(drop=False)


informe_tendencia = df_informe.pivot_table(
    index='DP',
    columns='AÑO',
    values='CANTIDAD',
    aggfunc='sum'
).reset_index(drop=False)

def tendencias(departamento):

    fila = informe_tendencia[informe_tendencia['DP'] == departamento]

    fila_long = fila.melt(id_vars='DP', var_name='Año', value_name='Valor')

    fig = px.line(
        fila_long,
        x='Año',
        y='Valor',
        title=f'Evolución por año - Departamento de {departamento}',
        markers=True
    )

    return fig