import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.BaseDatos import *

class Stockmarket:
    def __init__(self):
        self._Id=-1
        self._description=''
        self._initials=''
        self._lastquantation=0

    def Get(self,nombre):
        oBase = BaseDatos()
        query ="SELECT * FROM StockMarket"
        registro=oBase.FUNCION
        self._Id = int(registro[0])
        self._description = registro[1]
        self._initials = registro[3]
        self._lastquantation = registro[2]

    def Update(self,description,initials,price):
        oBase = BaseDatos()
        query="UPDATE stockmarket set description=%s,initials=%s,lastquantation=%s where id=%s"
        param= (description,initials,price,self._Id)
        try:
             oBase.Ejecutar(query,param)
             self._description=description
             self._lastquantation=price
             self._initials=initials
        except:
             print "Error in Update StockMarket"

    def Create(self,description,initials,price):
        oBase=BaseDatos()
        query="insert into StockMarket(description,initials,lastquantation) values (%s,%s,%s)"
        param=(description,initials,price)
        try:
            oBase.Ejecutar(query,param)
            query1 ="SELECT max(id) FROM StockMarket"
            try:
                 id=oBase.ConsultaSoloValor(query1)
                 self._Id=int(id)
                 self._description=description
                 self._initials=initials
                 self._lastquantation=price
            except:
                    print "Error in get Id StockMarket"
        except:
            print "Error in Create StockMarket"

    def Delete(self):
        oBase = BaseDatos()
        query="DELETE FROM StockMarket WHERE id= %s"
        param= (self._Id)
        try:
             oBase.Ejecutar(query,param)
        except:
             print "Error in Delete StockMarket"
