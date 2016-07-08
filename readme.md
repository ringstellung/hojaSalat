# ¿Cómo hacer una hoja?

* Descubrir cuál es el día 29. Hemos de ejecutar según el ejemplo
siguiente: 

		python3 dia29.py 7 30

indicando que el mes lunar comienza el día 7 de un mes solar de 30
días; la respuesta será 5 en este ejemplo.

Para ese día 29 que se haya obtenido hacer lo que indican los siguientes
pasos.

* Ir al fichero `observacion.py` y cambiar los datos oportunos en
 `observacion.py` sobre la observación del día día 29 y el pronóstico
 de avistamiento

* Ejecutar la siguiente orden en este directorio

		python3 hoja.py ciudad mesArabe mesSolar dia

   donde:
	* ciudad debe tener uno de los siguientes valores: "gr" o
	   "mt" o "sv"
	* mesArabe es una cifra del 1 al 12 que representa el mes
	   que queremos confeccionar. ramadan sería 9
	* mesSolar es una cifra del 1 al 12 que representa el mes
	   en que comienza el mesArabe
	* dia es el día del mes solar que coincide con el 1 del mes
	   árabe que vamos a confeccionar
	* la salida es ciudad.tex, o sea, gr.tex o mt.tex o sv.tex

Ejemplo:

	python3 hoja.py "gr" 6 3 11

esto generará la hoja "gr.tex" que coincidirá con la que ya tenemos
bajo el nombre "gr_06_1437.tex"

Otro ejemplo:

           python3 hoja.py sv 9 6 7

si queremos editar la hoja para Sevilla que corresponde a ramadän, més que ese año comienza el 7 de junio. 

     CÁLCULO DEL DÍA 30 DEL MES LUNAR (El DÍA 29 SE CALCULA ANÁLOGAMENTE)

¿Cómo calcular en que día del mes solar cae el día 30 del mes lunar,
conocido el día de comienzo y el mes?

	 python3 dia30.py diaComienzo duracionMes

donde diaComienzo es el día de comienzo del mes lunar y duracionMes es
la duración del mes solar en el que comienza el mes lunar.

Ejemplo:

	python3 dia30.py 3 31

indicando que el mes lunar comienza el día 3 de un mes solar de 31
días. La respuesta será 1.
