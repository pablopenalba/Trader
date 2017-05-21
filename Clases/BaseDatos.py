import MySQLdb as Db
class BaseDatos:
    _instance = None

    def __new__(self, *args, **kargs):
        if self.instance is None:
            self.instance = object.__new__(self, *args, **kargs)
        return self.instance

    def __init__(self):
        self._Host='localhost'
        self._Pass=''
        self._User='root'
        self._Name='bolsa'
        self._Port=3307
        self._conn = Db.connect(host=self._Host,
                          user=self._User,
                          passwd=self._Pass,
                          db=self._Name,
                          port=self._Port)

    def Select(self,query,param):
        cursor = self._conn.cursor()
        cursor.execute(query,param)
        registro = cursor.fetchone()
        return registro

    def Ejecutar(self,query,param):
        cursor = self._conn.cursor()
        try:
            cursor.execute(query,param)
            self._conn.commit()
        except:
            print "Error"
            self._conn.rollback()
        return 1

    def ConsultaSoloValor(self,query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        registro = cursor.fetchone()
        return registro[0]
