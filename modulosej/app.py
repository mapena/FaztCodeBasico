# importo librerias de terceros
#----------------------------
from colorama import Fore, Back, Style,init
init()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
# importo librerias de python
#----------------------------
import datetime
print(datetime.date.today()) # nos da le fecha

#importo mi libreria (si la libreria esta en el misma carpeta que este programa)
#-------------------
#opcion1:
#import fmathsum 
#print(fmathsum.sumar(2,3)) # invoco la libreria sumar

#opcion2: (si la libreria esta en el misma carpeta que este programa)
#from fmathsum import sumar    #-- de la libreria fmathsum traigo la funcion sumar, no trae la funcion sumar2
#from fmathsum import *         #-- de la libreria fmathsum traigo todas las funciones

#opcion3: (si la libreria esta en otra carpeta que este programa)
#     nombre de la carpeta
#     |       nombre de la libreria
#     V        V
from libreria.fmathsum import *         #-- de la libreria fmathsum traigo todas las funciones
print(sumar(2,3)) # invoco la libreria sumar
print(sumar2(2,3))
#     nombre de la carpeta
#     |       nombre de la sub carpeta
#     |        |       nombre de la libreria
#     V        V       V
from libreria.libresta.fmathres import *         #-- de la libreria fmathsum traigo todas las funciones
print(restar(10,5))            # invoco la libreria restar
