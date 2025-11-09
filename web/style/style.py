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

/* ===== Tarjetas ===== */
.h3_boxes {
    position: relative;
    background: #1f1f22;               /* fondo oscuro elegante */
    color: #EAEAEA;
    text-align: center;
    font-family: "Segoe UI", Roboto, sans-serif;
    font-weight: 400;
    line-height: 1.4;
    border-radius: 14px;
    padding: 25px 45px;
    min-width: 240px;                  /* mayor ancho */
    box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    transition: all 0.35s ease;
    animation: fadeIn 1s ease-in-out;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.06);
}

/* ===== Contenido ===== */
.h3_boxes strong {
    display: block;
    font-weight: 600;
    font-size: 1.1em;
    letter-spacing: 0.4px;
    color: #FFFFFF;
    position: relative;
    z-index: 1;
}

.h3_boxes span {
    display: block;
    margin-top: 6px;
    font-weight: 600;
    font-size: 1.35em;
    color: #A8D0E6;                     /* azul acero */
    position: relative;
    z-index: 1;
}


/* ===== Animaciones ===== */

/* Línea de enfoque (entra suavemente desde abajo) */
.h3_boxes::after {
    content: "";
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%) scaleX(0);
    width: 80%;
    height: 2px;
    background: linear-gradient(90deg, #5dade2, #a8d0e6);
    transition: transform 0.4s ease;
    transform-origin: center;
    opacity: 0.8;
}

/* Hover general */
.h3_boxes:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.45);
    border-color: rgba(168,208,230,0.2);
}

/* Hover animación línea */
.h3_boxes:hover::after {
    transform: translateX(-50%) scaleX(1);
}

/* Hover color del número */
.h3_boxes:hover span {
    color: #C2E3F5;
    transition: color 0.3s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
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
            background: #020024;
            background: linear-gradient(90deg,rgba(2, 0, 36, 1) 41%, rgba(9, 9, 121, 0.99) 100%, rgba(0, 212, 255, 0.58) 100%);
            padding: 10px;
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
            <div class="descripcion-hero">
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
            <style>
            .descripcion-hero{
            background: linear-gradient(145deg, #1C1F24, #23272E);
            border: 1px solid #1C1C1C;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 3px 8px rgba(0,0,0,0.15);
            animation: fadeIn 1s ease-in-out;
            }

            @keyframes fadeIn {
            from { opacity: 0; transform: translateY(40px); }
            to { opacity: 1; transform: translateY(0);}
            }
        
        </style>
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