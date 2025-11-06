h3_boxes = """
<style>

.stats_container {
    display: flex;
    justify-content: space-evenly;
    align-items: center;        
    flex-wrap: wrap;
    gap: 40px;
    margin-top: 25px;
    padding: 10px;
}


.h3_boxes {
    background: transparent;    
    color: #EAEAEA;             
    text-align: center;
    font-family: "Segoe UI", Roboto, sans-serif;
    font-weight: 400;
    line-height: 1.4;
    transition: color 0.3s ease;
    padding: 0;                 
    transition: all 0.25s ease-in-out;
}


.h3_boxes strong {
    display: block;
    font-weight: 600;
    font-size: 1.05em;
    letter-spacing: 0.5px;
    color: #FFFFFF;
}


.h3_boxes span {
    display: block;
    margin-top: 4px;
    font-weight: 600;
    font-size: 1.3em;
    color: #A8D0E6;             /* azul acero */
}

.h3_boxes:hover {
    transform: translateY(-4px);             /* realce al pasar el cursor */
}
            
.h3_boxes:hover span {
    color: #C2E3F5;             /* leve realce al pasar el cursor */
    transition: color 0.3s ease;
}
</style>
"""


columna_izquierda_estilo = """
            <div style="
                color:white;
                background-color:#2F4F4F;
                text-align: center;
                border: 1px solid #1C1C1C;
                border-radius: 10px;
                padding: 10px 5px;
                margin-bottom: 15px;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.2);
            ">
                <h3 style="margin: 0;">📑 DataFrame de Delitos Sexuales en Colombia (2025)</h3>
            </div>
            """

titlo_principal_estilo =   """
        <div style="
            background: linear-gradient(90deg, #2F4F4F, #556B2F);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            color: white;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            ">
            <h2 style="margin: 0;">📊 Información General</h2>
        </div>
        """



derechos = """
            <div style="text-align:center; margin-top:10px; color: #555;">
                Fuente: <a href="https://www.policia.gov.co/" target="_blank">
                <b>Policía Nacional de Colombia</b></a>
            </div>
            """


descripcion_estilo = """
            <div style="
                background: linear-gradient(145deg, #1C1F24, #23272E);;
                border: 1px solid #1C1C1C;
                border-radius: 10px;
                padding: 20px;
                box-shadow: 0px 3px 8px rgba(0,0,0,0.15);
            ">
                <h3 style="color:white; text-align:center;">🗺️ Ánalisis Exploratorio</h3>
                <p style="text-align:justify; color:white;">
                El anterior dataframe presenta una muestra representativa de los reportes
                de delitos sexuales ocurridos en Colombia hasta el año 2025. 
                La información muestra Departamento, Municipio, Arma usada, Fecha del Hecho, entre otros datos relevantes.
                <br>
                <br>
                El análisis, gráficas, mapas y demas visualizaciones posteriores se basan en este conjunto de datos, es importante que esto
                se tenga en cuenta a la hora de interpretar los resultados, por ejemplo, abajo se encuentra la gráfica de barras correspondiente a la distribución de delitos por departamento
                </p>
            </div>
            """

def boxes(mayor, menor, mediana):
    return """
<div class="stats_container">
    <h3 class='h3_boxes'>
        Más Delitos<br><span>{departamento_mayor}</span>
    </h3>
    <h3 class='h3_boxes'>
        Menos Delitos<br><span>{departamento_menor}</span>
    </h3>
    <h3 class='h3_boxes'>
        Mediana de Delitos<br><span>{mediana}</span>
    </h3>
</div>
""".format(departamento_mayor=mayor, departamento_menor=menor, mediana=mediana)