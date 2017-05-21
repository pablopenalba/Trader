import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.BaseDatos import *
import time

class Operacion:
    def __init__(self):
        self._Id
        self._DateTime
        self._TypeOperation
        self._IdAccion
        self._Quantity
        self._Price
        self._Commission

    def Create(self,stockmarketname,type,quantity):
        oBase = BaseDatos()
        self._DateTime= time.strftime("%c")
        self._TypeOperation=type
        try:
            query="SELECT id FROM accion WHERE nombre= %s"
            param=(stockmarketname)
            self._IdAccion= oBase.ConsultaSoloValor(query,param)
        except:
            print "Error al crear la operacion"
        try:
            query1="SELECT max(id) FROM accion"
            id=oBase.ConsultaSoloValor(query1)
            self._Id=id
        except:
              print "Error trying to get id"

        self._Quantity=quantity
        self._price=  100       #conectarse con mercado


    def Delete(self):
        oBase = BaseDatos()
        try:
            query="DELETE FROM operacion where id= %s"
            param=(self._Id)
            oBase.Ejecutar(query,param)
        except:
            print "Error al crear la operacion"

    def Get(self):
        oBase = BaseDatos()
        query="SELECT * FROM operacion where id= %s"
        param=(self._Id)
        try:
            registro=oBase.Select(query,param)
        except:
            print "Error in select of operation"
        self._IdAccion= registro[0]
        self._DateTime= registro[1]
        self._TypeOperation= registro[2]
        self._IdAccion= registro[3]
        self._Quantity= registro[6]
        self._Price= registro[4]
        self._Commission= registro[5]

    def Update(self,date,type,idAccion,quantity,price,com):
        oBase = BaseDatos()
        query = "UPDATE operacion(fecha,tipo,idAccion,precio,comision) values() where id= %s"
        param = (date,type,idAccion,quantity,price,self._Id)
        try:
            oBase.Ejecutar(query,param)
        except:
             print "Error in Update operation "