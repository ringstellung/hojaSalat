# -*- coding: utf-8 -*-

"""
  python hoja.py ciudad mesArabe mesSolar dia

● ciudad; debe tener uno de los siguientes valores: gr o mt o sv
● mesArabe; es una cifra del 1 al 12 que representa el mes que queremos confeccionar
● mesSolar; es una cifra del 1 al 12 que representa el mes en que comienza el mesArabe
● dia; es el día del mes solar que coincide con el 1 del mes árabe que vamos a confeccionar
● la salida es ciudad.tex, o sea, gr.tex o mt.tex o sv.tex

"""

import sys
from horario import *
from relleno import *

if __name__ == "__main__":

    z = mesTxtToLaTeX(sys.argv[1],int(sys.argv[3]),int(sys.argv[4]))
    rellenoPlant(sys.argv[1],
                 int(sys.argv[2]),
                 int(sys.argv[3]),
                 z)

