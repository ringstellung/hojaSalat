El procedimiento hasta hacer el main:

-) Entrar en "horario.py" y cambiar las últimas tres líneas según la
 necesidad. Esto generan el fichero "horario_ciudad.tex" (ciudad es
 "gr", "mt" o "sv" tras ejecutar desde consola la orden:

python3 horario.py


-) Ir al fichero "observacion.py" y cambiar los datos oportunos en
 "observacion.py" sobre la observación del último día y el pronóstico
 de avistamiento

-) Cambiar en el fichero "relleno.py" las últimas líneas según la
 necesidad y ejecutar la orden:

python3 relleno.py

esto genera el fichero .tex final "gr.tex" o "mt.tex" o "sv.tex", que
son los ficheros a compilar y sacar los pdf


Como hacer una hoja

-) Ir al fichero "observacion.py" y cambiar los datos oportunos en
 "observacion.py" sobre la observación del último día y el pronóstico
 de avistamiento

-) Ejecutar la siguiente orden en este directorio

   python3 hoja.py ciudad mesArabe mesSolar dia

   donde:
	-) ciudad debe tener uno de los siguientes valores: "gr" o
	   "mt" o "sv"
	-) mesArabe es una cifra del 1 al 12 que representa el mes
	   que queremos confeccionar. ramadan sería 9
	-) mesSolar es una cifra del 1 al 12 que representa el mes
	   en que comienza el mesArabe
	-) dia es el día del mes solar que coincide con el 1 del mes
	   árabe que vamos a confeccionar
	-) la salida es ciudad.tex, o sea, gr.tex o mt.tex o sv.tex

Ejemplo:

	python3 hoja.py "gr" 6 3 11

esto generará la hoja que ya tenemos con el nombre "gr_06_1437.tex"
