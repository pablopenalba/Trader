import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.Inversor import *
from  Clases.Operacion import *
from  Clases.StockMarket import *

oAccion=Stockmarket()
oAccion.Create('CRESUD','CRES',100)

oAccion.Update('CRESUD1','CRES',180)



#Crear Inversor
#Agregar cuenta
# Comprar acciones
# Vender Acciones
#Mostrar Resumen
