import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.BaseDatos import *

class Quaotation:
    def __init__(self):
        self._id=0
        self._idstockmarket=0
        self._price=0
        self._date=''
        self._open=0
        self._max=0
        self._min=0
        self._close=0
        self._volume=0
        self._idtransacion=0

    def Create(self,idAccion,nameAccion,price,date,open,max,min,close,volume):
        oBase=BaseDatos()
        query="insert into quaotation(idaccion,accion,fecha,apertura,cierre,maximo,minimo,volumen,precio) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param=(idAccion,nameAccion,date,open,max,min,close,volume,price)
        print query + str(param)
        try:
            oBase.Ejecutar(query,param)
            query1 ="SELECT max(id) FROM quaotation"
            try:
                 id=oBase.ConsultaSoloValor(query1)
                 self._id = int(id)
                 self._idstockmarket = idAccion
                 self._price = price
                 self._date = date
                 self._open = open
                 self._max = max
                 self._min = min
                 self._close = close
                 self._volume = volume
                 self._idtransacion = 0
            except:
                    print "Error in get Id quaotation"
        except:
            print "Error in Create quatation"

    def Update(self,idAccion,nameAccion,price,date,open,max,min,close,volume):
        oBase=BaseDatos()
        query="insert into quaotation(idaccion,accion,fecha,apertura,cierre,maximo,minimo,volumen,precio) " \
              "values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param=(idAccion,nameAccion,date,open,max,min,close,volume,price)
        try:
            oBase.Ejecutar(query,param)
            self._idstockmarket = idAccion
            self._price = price
            self._date = date
            self._open = open
            self._max = max
            self._min = min
            self._close = close
            self._volume = volume
            self._idtransacion = 0
        except:
            print "Error in Update quatation"

    def Delete(self):
        oBase = BaseDatos()
        query="DELETE FROM quaotation WHERE id= %s"
        param= (self._id)
        try:
             oBase.Ejecutar(query,param)
        except:
             print "Error in Delete Quatation"
