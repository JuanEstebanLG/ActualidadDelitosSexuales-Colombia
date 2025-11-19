from informes_handler import *
from pandas_handler import *
import pandas as pd
import streamlit as st

informe_violencia_a_la_mujer = informe_violencia_a_la_mujer.reset_index(drop=True)


#Funcion para calcular deltas de violencia
def return_deltas_violencia_mujer():
    
    totales = []
    deltas = []


    for año in range(2018, 2025):
        if año < 2024:
            total = informe_violencia_a_la_mujer[año + 1] - informe_violencia_a_la_mujer[año]
            delta = round(total / informe_violencia_a_la_mujer[año] * 100, 2)
            totales.append(total)
            deltas.append(delta)
    return totales, deltas

