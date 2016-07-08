# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys

signo = lambda x: x and (1,-1)[x<0]

def g(diaComienzo,duracionMes):
    """
    g establece cuál sería el día del mes solar
    correpondiente al 29 de un mes lunar que
    comenzara el día "diaComienzo" de un mes
    solar de duración "duracionMes". Para explicar
    este críptico código, ver algo similar en dia30.py
    """ 
    b = (diaComienzo + 28)%duracionMes
    return max(signo(b)*b, (not signo(b))*duracionMes)

if __name__ == "__main__":
    print(g(int(sys.argv[1]),int(sys.argv[2])))
