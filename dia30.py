# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

def f(diaComienzo,duracionMes):
    if diaComienzo + 29 == duracionMes:
        b = duracionMes
    else:
        b = (diaComienzo + 29)%duracionMes
    return b

signo = lambda x: x and (1,-1)[x<0]

def g(diaComienzo,duracionMes):
    """
    g establece cuál sería el día del mes solar
    correpondiente al hipotético 30 de un mes lunar
    que comenzara el día "diaComienzo" del un mes
    solar de duración "duracionMes". Para explicar
    este críptico código, sépase que g funciona igual
    que f. signo es el signo del número real argumento.
    """ 
    b = (diaComienzo + 29)%duracionMes
    return max(signo(b)*b, (not signo(b))*duracionMes)

    """
    otra posibilidad sería considerar:
        b = diaComienzo + 29 - duracionMes
    pero esto lleva al representante de menor valor
    absoluto, que sale negativo o nulo en casos como
    diaComienzo 1 ó 2. Para arreglarlo, un if
    que es lo que no queremos y por lo que % es ideal.
    """

if __name__ == "__main__":
    print(g(int(sys.argv[1]),int(sys.argv[2])))
