import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.Inversor import *
from  Clases.Operacion import *


oInv=Inversor()
#oInv.Crear('pablo',10000)
oInv.ObtenerInversorPorId('juan')
#oInv.Update('juan',4000,43000)
oInv.MostrarDatos()
oper=Operacion()
oper.Create('CRES','COMPRA',100)

#Crear Inversor
#Agregar cuenta
# Comprar acciones
# Vender Acciones
#Mostrar Resumen
