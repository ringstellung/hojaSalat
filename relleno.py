# -*- coding: utf-8 -*-
#!/usr/bin/env python

from palabras import *
from observacion import *

def rellenoPlant(ciudad,
                 mesa,
                 mes,
                 b=True):
    """
     "rellenoPlant" es la función que rellena la plantilla
        y produce el fichero .tex: gr.tex o mt.tex o sv.tex
     "ciudad" será "gr" o "mt" o "sv"
     "mesa" es el mes árabe, un número del 1 al 12
     "mes" es el mes solar en el que arranca el mes árabe,
             es un número del 1 al 12
     "b" a False cuando el mes árabe cae en un único mes solar
    """
    m1, m2 = mes, mes%12+1
    dictObs, salida = ciudades[ciudad], ciudad+".tex"
    plantilla = plantillas[ciudad]
    horario = horarios[ciudad] 
    with open(plantilla,"r") as f1:
        lee_plantilla = f1.read()
    with open(horario,"r") as f2:
        lee_horario = f2.read()
    with open(salida, "w") as f:
        cadena = lee_plantilla.replace("horario",lee_horario)
        cadena = cadena.replace("mesArabTrans",mesArabTrans[mesa])
        cadena = cadena.replace("mesArabArab",mesArabArab[mesa])
        cadena = cadena.replace("mesArabCaja",mesArabCaja[mesa])
        for key in dictObs:
            cadena = cadena.replace(key,dictObs[key])
        if b == True:
            mSA = {"mesSolarArab1":m1,"mesSolarArab2":m2}
            mSE = {"mesSolarEsp1":m1,"mesSolarEsp2":m2}
            for key in mSA:
                cadena = cadena.replace(key,mesSolarArab[mSA[key]])
            for key in mSE:
                cadena = cadena.replace(key,mesSolarEsp[mSE[key]])            
        else:
            cadena = cadena.replace("\\RL{mesSolarArab2} /\\RL{mesSolarArab1}","\\RL{mesSolarArab1}")
            cadena = cadena.replace("mesSolarArab1",mesSolarArab[m1])
            cadena = cadena.replace("mesSolarEsp1/mesSolarEsp2","mesSolarEsp1")
            cadena = cadena.replace("mesSolarEsp1",mesSolarEsp[m1])
        if mesa < 11:
            cadena = cadena.replace("mAAG",mesArabArab[mesa])
        elif mesa == 11:
            cadena = cadena.replace("mAAG",mesArabArab[23])
        else:
            cadena = cadena.replace("mAAG",mesArabArab[24])
        f.write(cadena)
        f.close
