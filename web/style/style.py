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


hero_cards = """
    <div class="hero">
        <div class="hero-text">
            <h1>Informe Nacional sobre Delitos Sexuales en Colombia (2010–2025)</h1>
            <h2>Una mirada integral hacia la comprensión y prevención</h2>
            <p>
            Este informe presenta un análisis detallado de los delitos sexuales cometidos en Colombia
            durante los últimos quince años, utilizando datos oficiales y técnicas de análisis estadístico.
            Su propósito es visibilizar la magnitud de esta problemática y ofrecer insumos para la toma
            de decisiones orientadas a la prevención y la atención de las víctimas.
            </p>
            <br>
            <p>
            En el contexto colombiano, los delitos sexuales representan un fenómeno complejo que impacta
            profundamente la estructura social y el bienestar de las comunidades. La persistencia de estos
            casos exige una reflexión colectiva sobre las políticas de educación, justicia y equidad de género,
            así como una revisión constante de las estrategias institucionales de protección y denuncia.
            </p>
        </div><div class="hero-side">
            <h3>¿Por qué este estudio es importante?</h3>
            <p>
            Comprender las tendencias de los delitos sexuales permite fortalecer las políticas públicas
            y enfocar esfuerzos en la protección de las víctimas, garantizando una Colombia más segura
            y consciente del valor de la integridad y la dignidad humana.
            </p>
        </div>
    </div>
    """

close_menu = """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
"""

home_styles = """
<style>
/* Fondo general */
.stApp {
    background-color: #f4f4f4;
    background-image: url("resources/images/fondo_inicio.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.hero {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 2rem;
    align-items: center;
    margin: 4rem auto;
    padding: 3rem 4rem;
    max-width: 1100px;
    background: rgba(255, 255, 255, 0.92);
    border-radius: 25px;
    box-shadow: 0 4px 25px rgba(0, 0, 0, 0.1);
    animation: fadeIn 1.2s ease-in-out;
}

/* Texto principal */
.hero-text h1 {
    color: #0B2948;
    font-size: 2rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}

.hero-text h2 {
    color: #1b4f72;
    font-size: 1.3rem;
    margin-bottom: 1.5rem;
    font-weight: 600;
}

.hero-text p {
    color: #333;
    line-height: 1.6;
    font-size: 1rem;
}

/* Tarjeta lateral */
.hero-side {
    background: #0B2948;
    color: #fff;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(11, 41, 72, 0.2);
    transform: translateY(0);
    transition: all 0.4s ease;
}

.hero-side:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(11, 41, 72, 0.3);
}

.hero-side h3 {
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 1rem;
    color: #f1f1f1;
}

.hero-side p {
    font-size: 0.95rem;
    line-height: 1.5;
}

/* Animaciones */
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

metric_explanation = """
        <style>
        .metric-info-container {
            margin-top: 10px;
            margin-bottom: 10px;
        }

        .metric-info-box {
            background: linear-gradient(145deg, #1C1F24, #23272E);
            color: #EAEAEA;
            padding: 16px 20px;
            border-radius: 10px;
            border: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
            font-size: 0.95rem;
            line-height: 1.5;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            animation: metricFadeIn 0.6s ease-out forwards;
            transform: translateY(8px);
            opacity: 0;
            transition: transform 1s ease, box-shadow 0.25s ease;
        }

        .metric-info-box:hover {
            transform: translateY(4px);
            box-shadow: 0 14px 30px rgba(0, 0, 0, 0.2);
        }

        @keyframes metricFadeIn {
            from {
                opacity: 0;
                transform: translateY(12px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }

            
        }
        </style>

        <div class="metric-info-container">
            <div class="metric-info-box">
                Los valores positivos en las anteriores métricas indican un aumento en los casos reportados en comparación con el año anterior; por otro lado, los valores negativos indican una disminución de los casos reportados.
            </div>
        </div>
"""
