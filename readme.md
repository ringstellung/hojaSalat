<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />

# Hoja de la Oración

## Cálculo del día 29 del mes lunar

¿Cómo calcular en que día del mes solar cae el día 29 del mes lunar,
conocido el día de comienzo y el mes?

	 python dia29.py diaComienzo duracionMes

donde `diaComienzo` es el día de comienzo del mes lunar y `duracionMes` es
la duración del mes solar en el que comienza el mes lunar.

Ejemplo 01:

	python dia29.py 3 31

indicando que el mes lunar comienza el día 3 de un mes solar de 31
días. La respuesta será 31.

Ejemplo 02:

Descubrir cuál es el día 29. Hemos de ejecutar según el ejemplo siguiente:

		python dia29.py 7 30

indicando que el mes lunar comienza el día 7 de un mes solar de 30
días; la respuesta será 5 en este ejemplo.

## Elaboración de una Hoja

Para el día 29 que se haya obtenido según lo dicho, hacer lo que
indican los siguientes pasos:

1. Ir al fichero `observacion.py` y cambiar los datos oportunos en
 `observacion.py` sobre la observación del día día 29 y el pronóstico
 de avistamiento

2. Ejecutar la siguiente orden en este directorio:

        python hoja.py ciudad mesArabe mesSolar dia

   donde:
	
	* `ciudad` debe tener uno de los siguientes valores: `gr` o bien `mt`
	   o bien `sv`

	* `mesArabe` es una cifra del 1 al 12 que representa el mes que
	   queremos confeccionar (ramadän sería 9).

	* `mesSolar` es una cifra del 1 al 12 que representa el mes en que
	   comienza el `mesArabe`
	
	* `dia` es el día del mes solar que coincide con el 1 del mes árabe
	  que vamos a elaborar
	
	* la salida es `ciudad.tex`, o sea: `gr.tex` o bien `mt.tex` o bien
      `sv.tex`.

Ejemplo 01:

	python hoja.py gr 6 3 11

esto generará la hoja `gr.tex` que coincidirá con la que ya tenemos
bajo el nombre `gr_06_1437.tex`

Ejemplo 02:

    python hoja.py sv 9 6 7

si queremos editar la hoja para Sevilla que corresponde a ramadän (mes
9 del calendario islámico), més que ese año comienza el 7 de junio. 

## Ampliación del Programa a una Nueva Ciudad

1. Hacer la plantilla `.tex`
1. Añadir la plantilla a `observacion.py`
1. Añadir la entrada en el diccionario `plantillas`, `horarios`,
   `ciudades` y `city` de `observacion.py`.

## Para los Cálculos Astronómicos

Debe descomprimir el fichero `time.zip`. En la carpeta resultante,
también de nombre `time` encontrará dos subcarpetas entre otras:
`moonc60` y `pt29`. En las mismas interesan los respectivos `.exe`,
que deben ser ejecutados desde DOSBox (Mac OS y Linux) o dosemu
(Linux), Por ejemplo la forma de instalar y habilitar DOSBox están
magnificamente explicadas en
[https://wildunix.es/dosbox/](https://wildunix.es/dosbox/).

Con `moonc60.exe` podrá calcular parámetros lunares y solares para la
observación de la creciente tras la puesta de sol que cierra el día 29
de cada mes. Con `pt29.exe` podrá calcular las horas de la oración
para un mes y una ciudad de las incluidas en el repertorio o las que
usted incluya. Al calcular un mes recuerde pedir que guarde en disco
(pulse "D" en su momento) y ante la pregunta "Do you want a custom
line of text which will appear at top of table? (Y/N)" elija la
opcción "N"; si no hace esto último nada funcionará correctamente.

Hemos incluido ficheros de prueba para las ciudades de Elche
(comienzan por "elche"), Sevilla (comienzan por "sevill") y Granada
(comienzan por "granad"). Puede prescindir de ellos o eliminarlos
simplemente. 

## El Proyecto

Los ficheros esenciales del proyecto son:

* `observacion.py`
* `palabras.py`
* `horario.py`
* `relleno.py`
* `hoja.py`

El fichero `hoja.py` es el `main` del proyecto; importa `horario.py` y
`relleno.py`. El segundo en importancia es `horario.py`, donde están
las clases y la manipulación de los ficheros de texto producidos por
el programa `pt29.exe`; importa `observación.py` y `palabras.py`. El
fichero `relleno.py` importa esos mismos ficheros; su cometido es
constituir los ficheros `.tex` que compilados con LaTeX dan la hoja
del mes en formato `.pdf`. Al instalar su LaTeX no olvide incluir
`Arabtex`, que estamos luchando porque vuelva a funcionar
correctamente (el de 2023 fue el último que lo hizo).

Los ficheros que responden al patrón `plantilla_*.tex` son las
plantillas de latex que serán rellenas cada mes por `relleno.py`.
