from informes_handler import *
from pandas_handler import *


informe_violencia_a_la_mujer = informe_violencia_a_la_mujer.reset_index(drop=True)


#Funcion para convertir una serie o lista de un solo elemento a una lista de escalares
def to_scalar_list(seq):
    out = []
    for x in seq:
        if hasattr(x, "iloc"):     # Series de un solo elemento
            out.append(float(x.iloc[0]))
        else:
            out.append(float(x))
    return out

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
   
    totales = to_scalar_list(totales)
    deltas = to_scalar_list(deltas)

    return totales, deltas
