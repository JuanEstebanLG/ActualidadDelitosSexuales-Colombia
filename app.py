#LIBRERIAS
import folium as folium
from streamlit_option_menu import option_menu
from figures import *
from web.style.style import *
from web.style.style import hero_cards, home_styles, close_menu, info_team
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



################################################################################################                           
                                    #  SIDEBAR CONFIGURATION  #
################################################################################################      
st.markdown(close_menu, unsafe_allow_html=True)

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
    st.markdown(hero_cards,unsafe_allow_html=True)

    
elif selected == "Dashboards":
    try:
        page_file = pathlib.Path(__file__).parent / "pages" / "informe.py"
        runpy.run_path(str(page_file), run_name="__main__")
    except Exception as e:
        st.error(f"Error ejecutando informe.py: {e}")

elif selected == "About us":
        
    st.markdown(info_team, unsafe_allow_html=True)