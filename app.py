#LIBRERIAS
import folium as folium
from streamlit_option_menu import option_menu
from figures import *
from web.style.style import *
import pathlib, runpy, streamlit as st
from pathlib import Path


################################################################################################                           
                                    #  STREAMLIT DESING  #
################################################################################################ 


st.set_page_config(page_title="Análisis de Delitos Sexuales en Colombia", layout="wide", initial_sidebar_state="collapsed",
                   page_icon=":bar_chart:")
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)


home_styles = """
<style>
/* Fondo general */
.stApp {
    background-color: #f4f4f4;
    background-image: url("https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/pexels-anna-nekrashevich-6801648.jpg?raw=true");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Contenedor principal */
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
    text-align: justify
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
    text-align: justify
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

################################################################################################                           
                                    #  SIDEBAR CONFIGURATION  #
################################################################################################      

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Dashboards", "About us"],
        icons=["house", "table", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    
    st.markdown(home_styles, unsafe_allow_html=True)
    st.markdown("""
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
    """, unsafe_allow_html=True)

    
elif selected == "Dashboards":
    try:
        page_file = pathlib.Path(__file__).parent / "pages" / "informe.py"
        runpy.run_path(str(page_file), run_name="__main__")
    except Exception as e:
        st.error(f"Error ejecutando informe.py: {e}")

elif selected == "About us":
        
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }
    /* GRID DEL EQUIPO */
    .team-grid {
        display: flex;
        justify-content: center;
        gap: 40px;
        flex-wrap: wrap;
        margin-top: 40px;
    }
    /* TARJETAS */
    .card {
        width: 320px;
        padding: 25px;
        border-radius: 25px;
        backdrop-filter: blur(14px) saturate(150%);
        background: rgba(255, 255, 255, 0.28);
        border: 1px solid rgba(255, 255, 255, 0.25);
        box-shadow: 0 12px 36px rgba(0, 0, 0, 0.20);
        text-align: center;
        transition: all 0.35s ease;
    }
    .card:hover {
        transform: translateY(-12px) scale(1.03);
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.30);
    }
    /* FOTOS */
    .card img {
        max-width: 160px;
        max-height: 160px;
        width: 100%;
        height: auto;
        object-fit: contain;
        border-radius: 100%;
        margin-bottom: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
    }
    /* NOMBRES */
    .card h3 {
        font-size: 22px;
        margin-bottom: 8px;
        color: #111;
    }
    /* DESCRIPCIÓN */
    .card p {
        font-size: 15px;
        text-align: justify;
        line-height: 1.55;
        color: #333;
        margin-bottom: 14px;
    }
    /* ICONOS DE CONTACTO */
    .contact-icons a {
        margin: 0px 10px;
        font-size: 22px;
        color: #007aff;
        transition: 0.25s ease;
    }
    .contact-icons a:hover {
        color: #0051a8;
        transform: scale(1.15);
    }
    </style>
    <div class="team-grid">
        <!-- Esteban -->
        <div class="card">
            <img src="resources\images\fondo_inicio.jpg" alt="Foto 1" class="card-image-top">
            <h3>Juan Esteban López Gómez</h3>
            <p>
                ........
            </p>
            <div class="contact-icons">
                <a href="mailto:juan.lopez@example.com"><i class="fa-solid fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/juanlopez/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
        <!-- Miguel -->
        <div class="card">
            <img src="https://github.com/JuanEstebanLG/ActualidadDelitosSexuales-Colombia/blob/Main/resources/images/miguel.jpg?raw=true" alt="Foto 2">
            <h3>Miguel Angel Cuervo Espinosa</h3>
            <p>
                Analista de datos con formación en ingeniería y ciencias biológicas. Con experiencia en Python, Power BI y estadística para procesar, limpiar y visualizar datos complejos. 
                Mediante análisis, automatizaciones y reportes para la toma de decisiones y proyectos de investigación aplicada.
            </p>
            <div class="contact-icons">
                <a href="mailto:milcuervo@gmail.com"><i class="fa-solid fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/miguelcuervoe/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
        <!-- Camilo -->
        <div class="card">
            <img src="https://via.placeholder.com/150" alt="Foto 3">
            <h3>Juan Camilo Loaiza</h3>
            <p>
                Administrador financiero con 15 años de experiencia como auditor en diversas empresas, 
                especializado en fortalecer controles internos, mejorar procesos y asegurar la calidad de la información financiera.
            </p>
            <div class="contact-icons">
                <a href="mailto:majoca854@gmail.com"><i class="fa-solid fa-envelope"></i></a>
                <a href="https://www.linkedin.com/in/juancamilo/" target="_blank"><i class="fa-brands fa-linkedin"></i></a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)