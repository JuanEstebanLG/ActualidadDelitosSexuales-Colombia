#LIBRERIAS
import folium as folium
from streamlit_option_menu import option_menu
from figures import *
from web.style.style import *
import pathlib, runpy, streamlit as st


#STREAMLIT APP

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
    background-image: url("resources/images/fondo_inicio.jpg");
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


with st.sidebar:
    selected = option_menu(
        menu_title="Menu Principal",
        options=["Inicio", "Información", "Sobre el Equipo"],
        icons=["house", "table", "info-circle"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Inicio":
    
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

    
elif selected == "Información":
    try:
        page_file = pathlib.Path(__file__).parent / "pages" / "informe.py"
        runpy.run_path(str(page_file), run_name="__main__")
    except Exception as e:
        st.error(f"Error ejecutando informe.py: {e}")