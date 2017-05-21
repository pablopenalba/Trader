import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.BaseDatos import *

class Inversor:

  def __init__(self):  #falta
      #obtener ultimo id
      _Id=-1
      Nombre=''
      _InversionInicial=0
      _Gananciatotal=0
      _PorcGanancia=0
      _ListOperaciones = []
      _ListAcciones = []
      #insertar registro

  def Crear(self,Nombre,InversionIni):
      Obase = BaseDatos()
      query="insert into inversor(nombre,InvInic,Total,PorcGanac) values(%s, %s , %s , 0)"
      query1="select max(id) as Id from inversor"
      param=(Nombre,InversionIni,InversionIni)
      try:
         Obase.Ejecutar(query,param)
         id=Obase.ConsultaSoloValor(query1)

      except:
          print "Error en inversor"
      self._Id=int(id)
      self.Nombre=Nombre
      self._InversionInicial=InversionIni
      self._Gananciatotal=InversionIni
      self._PorcGanancia=0

  def __del__(self):
      pass

  def MostrarDatos(self):
      print ("ID:",self._Id)
      print("Nombre:",self.Nombre)
      print("Inversion Inicial:", self._InversionInicial)
      print("Inversion Final",self._Gananciatotal)
      print("Porcentaje Ganancia", self._PorcGanancia)

  def Update(self,Nombre,Inversioninicial,InversionFinal):
      Obase=BaseDatos()
      query="UPDATE inversor SET nombre=%s,InvInic=%s,Total=%s where id=%s"
      param=(Nombre,Inversioninicial,InversionFinal,self._Id)
      Obase.Ejecutar(query,param)
      self.Nombre=Nombre
      self._InversionInicial=Inversioninicial
      self._Gananciatotal=InversionFinal
      self._PorcGanancia=InversionFinal/Inversioninicial

  def ObtenerInversorPorId(self,nombre):
      OBase=BaseDatos();
      query="SELECT * from inversor where nombre=%s ";
      param=(nombre)
      registro=OBase.Select(query,param)
      self._Id= int(registro[0])
      self.Nombre = registro[1]
      self._InversionInicial = registro[2]
      self._Gananciatotal = registro[3]
      self._PorcGanancia = registro[4]

  def EliminarInversor(self):
      Obase = BaseDatos()
      query=" DELETE FROM inversor where id= %s"
      param=(self._Id)
      Obase.Ejecutar(query,param)
      self.__del__()

  def BuyStockMarket(self,nombreccion):
       pass
       # Obtener datos de accion
       # Crear Operacion
       # Actualizar listas

  def SaleStockMarket(self,Id):
       pass
       #Obtener datos de accion
       #Crear Operacion
       #Actualizar listas

  def CalculateGain(self):
      pass

  def ShowSummary(self):
     pass
     # Accion- ValorCompra - ValorActual - Cant- Diferencia - ValorActual*Cant
      #total