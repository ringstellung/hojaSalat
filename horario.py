# -*- coding: utf-8 -*-

from observacion import *
from palabras import *

class Dia(object):
    """
    Clase 'Dia' como parte del contenido del fichero 'hoja.py'
    para implementar el contenido de un día de oración.
    Autor: yahya garcía olmedo
    Fecha: 21/03/2016
    Hora: 17:29 h.
    """
    _agnadidura = 1
    _agnadiduraDuhur = 5
    
    _diasEntoSp ={'Mon':'lun',
                'Tue':'mar',
                'Wed':'mie',
                'Thu':'jue',
                'Fri':'vie',
                'Sat':'sab',
                'Sun':'dom'
                }

    _diasEntoAr ={'Mon':"\RL{al-'i_tnaynu}",
                'Tue':"\RL{a_t-_tulA_tA'u}",
                'Wed':"\RL{al-'arbi`A'u}",
                'Thu':"\RL{al-_hamIsu}",
                'Fri':"\RL{al-^gumu`aTu}",
                'Sat':"\RL{as-sabtu}",
                'Sun':"\RL{al-'a.hadu}"
                }
        
    def _msToTime (self,hours,minutes):
        """
        '_msToTime' se lee 'minutosToTime' y 
        su efecto es normalizar un hito temporal
        haciendo que minutes no supere el valor de
        59 y haya el debido acarreo.
        """
        hoursFromMinutes, minutes = divmod(minutes,60)
        hours += hoursFromMinutes     
        return hours, minutes

    def _suma2Hitos(self,hito1,hito2):
        sumar = lambda x,y: x + y
        suma = map(sumar,hito1,hito2)
        return self._msToTime(*suma)

    def _normalizacion(self,hito,n):
        signo = lambda x: x and (1,-1)[x<0]
        return self._suma2Hitos(hito,(0,signo(n)*self._agnadidura))

    def _normalizacionDuhur(self,hito):
        return self._suma2Hitos(hito,(0,self._agnadiduraDuhur))
    
    def __init__(self,dm,est,sem,f,s,z,a,m,i):
        s1 = self._normalizacion(s,-1)
        z1 = self._normalizacionDuhur(z)
        m1 = self._normalizacion(m,1)
        self.diaMesSolar = dm
        self.estacion    = est
        self.semana      = self._diasEntoSp[sem] + "&" + self._diasEntoAr[sem]
        self.fayr        = f
        self.shuruq      = s1
        self.duhur       = z1
        self.asr         = a
        self.magrib      = m1
        self.isha        = i

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8}".format(self.isha,
                                                            self.magrib,
                                                            self.asr,
                                                            self.duhur,
                                                            self.shuruq,
                                                            self.fayr,
                                                            self.semana,
                                                            self.estacion,
                                                            self.diaMesSolar)

def limpiaMes(mes):
    margenSup, margenInf = 10, 12
    with open(mes,'r') as m:
        lst = m.readlines()
        if '*' in lst[-6]:
            margenInf += 1
        lst = lst[margenSup:-margenInf]
    return lst

def capturaLineas(diaComienzo,mes0,mes1=None,mes2=None):
    dc, tomar, usado = int(diaComienzo)-1, 30, 0 
                   # para dc los días comienzan en 1 y la lista es indexada desde 0 
    lst = limpiaMes(mes0)[dc:]
    usado +=1
    tomar = 30 - len(lst)
    if tomar < 0:
        lst = lst[0:30]
    elif tomar > 0:
        mst = limpiaMes(mes1)
        lst += mst 
        tomar = 30 - len(lst)
        usado += 1
        if tomar < 0:
            lst = lst[0:30]
        elif tomar > 0:
            mst = limpiaMes(mes2)
            lst += mst
            tomar = 30 - len(lst)
            usado +=1
            if tomar < 0:
                lst = lst [0:30]
    return lst, usado

def extractDataLine(fila):
    """
    extractDataLine extrae de cada línea los valores dato
    con el formato adecuado para crear el objeto Dia
    correspondiente a esa línea
    """
    a =fila.replace(':',' ').replace('\r','').replace('\n','').split()
    if '*' in a[0]:
        a[0] = a[0][0:-1]
        a.insert(1,'*')
    else:
        a.insert(1,'')
    a = a[0:3]+[(int(a[x]), int(a[x+1])) for x in range(3,len(a),2)]
    del(a[7])   # el segundo `asr no interesa,
                # si el preferido fuese el segundo, del(a[6])
    return a

def fromTxtToDia(diaComienzo, mes0,mes1=None,mes2=None):
    """
    fromTxtToDia extrae de los meses en txt, a partir del día
    diaComienzo del primero, 30 líneas correspondientes cada
    una a un día. Seguidamente convierte cada entrada obtenida
    en objetos de la clase Dia y provee la lista de todos esos
    objetos construidos.
    El sentido de la variable booleana "sm" de la salida es dar
    respuesta a la pregunta ¿ha sido involucrado un segundo
    mes en la extración del horario? Obviamente "False"
    significa respuesta "NO".
    """
    cl,sm = capturaLineas(diaComienzo,mes0,mes1,mes2)
    x = list(map(extractDataLine,cl)) # a ver si podemos prescindir de list aquí
    return [Dia(*i) for i in x], sm

def DiaToTxt(dia,diaMesLunar):
    """
    DiaToTxt construye de una instancia de la clase Dia
    y diaMesLunar, al que vemos como su día de mes lunar
    correspondiente, la línea con el formato LaTeX que 
    corresponderá. Pone un retorno de carro al final de
    la línea.
    """
    lineaLatex = ''
    atributosNum = ['isha',
                    'magrib',
                    'asr',
                    'duhur',
                    'shuruq',
                    'fayr'
                    ]
    for i in atributosNum:
        lineaLatex += str(dia.__dict__[i][0]).rjust(2,'0') + ':' + str(dia.__dict__[i][1]).rjust(2,'0') + '&'
    lineaLatex += dia.semana.ljust(23) + '&'
    lineaLatex += str(dia.diaMesSolar).rjust(2,'0') + dia.estacion.rjust(1) + '&'
    lineaLatex += str(diaMesLunar).rjust(2,'0') + "\\\\\hline\r"
    return lineaLatex

def DiaToTxtW(dia,diaMesLunar):
    """
    El funcionamiento es idéntico al de DiaToTxt salvo que
    DiaToTxtW no pone el retorno de carro al final de
    la línea. Es imprescindible, y se usa exclusivamente, en
    la construcción de la última línea. Ello es para que
    la compilación LaTeX no dé error.
    """
    lineaLatex = ''
    atributosNum = ['isha',
                    'magrib',
                    'asr',
                    'duhur',
                    'shuruq',
                    'fayr'
                    ]
    for i in atributosNum:
        lineaLatex += str(dia.__dict__[i][0]).rjust(2,'0') + ':' + str(dia.__dict__[i][1]).rjust(2,'0') + '&'
    lineaLatex += dia.semana.ljust(23) + '&'
    lineaLatex += str(dia.diaMesSolar).rjust(2,'0') + dia.estacion.rjust(1) + '&'
    lineaLatex += str(diaMesLunar).rjust(2,'0') + "\\\\\hline"
    return lineaLatex
            
def mesTxtToLaTeX(ciudad,mes,diaComienzo):
    """
        mesTxtToLaTeX crea 30 líneas LaTeX, una con
        cada día, tomadas del diaComienzo del mes mes1 en
        adelante completando, si es necesario, con las
        primeras líneas del mes2 y mes3 en su caso. Esta
        función no tiene return, pues su función es meramente
        la creación de un fichero.
        "ciudad" es una de: "gr" o "mt" o "sv"
        "mes" es un número de 1 a 12, representa el mes
              solar en el que tiene comienzo el mes lunar
              en elaboración
        "diaComienzo" es el día del "mes" en que comienza
              el mes lunar
    El sentido de la variable entera "b" de la salida es
    contar el número de meses usados para construir la tabla.
    """
    m0, m1 = mes, mes%12 + 1
    m2 = m1%12 + 1
    horario = horarios[ciudad]
    mes0, mes1 = city[ciudad]+mesSolarEng[m0], city[ciudad]+mesSolarEng[m1]
    mes2 = city[ciudad]+mesSolarEng[m2]
    d,b = fromTxtToDia(diaComienzo,mes0,mes1,mes2)
    lst = [DiaToTxt(d[i-1],i) for i in range(1,30)]
    lst.append(DiaToTxtW(d[29],30))
    with open(horario, "w") as f:
            for i in range(30):
                f.write(lst[i])
    return b

"""
z = mesTxtToLaTeX("gr",1,31)
print(z)
"""
