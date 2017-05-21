import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from  Clases.BaseDatos import *

class Quantation:
    def __init__(self):
        self._id=0
        self._idAccion=0
        self._precio=0
        self._fecha=''
        self._apertura=0
        self._maximo=0
        self._minimo=0
        self._cierre=0
        self._volumen=0

    def Create(self):
        pass
    def Update(self):
        pass
    def Delete(self):
        pass
