import pandas as pd
import geopandas as gpd

url = 'https://github.com/JuanEstebanLG/AnalisisDatos/raw/refs/heads/main/Reporte_Delitos_Sexuales_Policia_Nacional_2025.gzip'
geo_url = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/3aadedf47badbdac823b00dbe259f6bc6d9e1899/colombia.geo.json'


df = pd.read_parquet(url)
gdf = gpd.read_file(geo_url)


#Limpieza de datos

clean_df = df

old_columns = clean_df.columns
new_columns = ['DP','MUNICIPIO', 'DANE', 'ARMAS','FECHA_DEL_HECHO', 'GENERO', 'GRE', 'CANTIDAD', 'DELITO']
clean_df = clean_df.rename(columns = dict(zip(old_columns, new_columns)))

#Limpieza de la columna DELITO y Agregación de columna AÑO
clean_df['DELITO'] = clean_df['DELITO'].str.extract(r'\.\s*(.*)')


clean_df['AÑO'] = clean_df['FECHA_DEL_HECHO'].str.extract(r'.*/([^/]+)$')
clean_df['AÑO'] = clean_df['AÑO'].astype(int)

clean_df = clean_df.drop_duplicates()




