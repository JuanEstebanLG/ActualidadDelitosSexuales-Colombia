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
