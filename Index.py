import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.Inversor import *
from  Clases.Operacion import *
from  Clases.StockMarket import *
from  Clases.Quaotation import *

oAccion=Stockmarket()
#oAccion.Create('CRESUD','CRES',100)
#oAccion.Get('CRES')
#oAccion.Update('CRESUD1','CRES',180)
oCotiz=Quaotation()
oCotiz.Create(23,'CRES',100,'',100,100,100,100,100)
oCotiz.Update(23,'CRES',100,'',110,120,100,50,100)
#oCotiz.Delete()

#Crear Inversor
#Agregar cuenta
# Comprar acciones
# Vender Acciones
#Mostrar Resumen
