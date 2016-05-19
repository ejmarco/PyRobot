from BinarySearch import *
from sortedSequenceAsArray import *
reload
class Alumne(object):
    criteri=0 # 0 = NIU, 1 = Cognom
    __slots__ = ["__nom","__cognom","__niu"]
    def __init__(self, no, co, ni=None):
        self.__nom = no
        self.__cognom = co
        self.__niu = ni 
    def getNom(self):
        return self.__nom
    def setNom(self,no):
        self.__nom = no
    def getCognom(self):
        return self.__cognom
    def setCognom(self,co):
        self.__cognom = co
    def getNiu(self):
        return self.__niu
    def setNiu(self,ni):
        self.__niu = ni
    #def setCriteri(self,cri):
    #    self.__criteri = cri
    #def getCriteri(self):
    #    return self.__criteri
    def __str__(self):
        return str(self.getNom()) + " " + str(self.getCognom()) + ", " + str(self.getNiu())
    def __eq__(self, alumne): #igual que
        if Alumne.criteri is 0:
            return self.__niu == alumne.getNiu()
        else:
            return self.__cognom == alumne.getCognom()
    def __le__(self, alumne): # menor o igual que
        if Alumne.criteri is 0:
            return self.__niu <= alumne.getNiu()
        else:
            return self.__cognom <= alumne.getCognom()
    def __ge__(self, alumne): # mayor o igual que
        if Alumne.criteri is 0:
            return self.__niu >= alumne.getNiu()
        else:
            return self.__cognom >= alumne.getCognom()
    def __lt__(self, alumne): # menor que
        if alumne is None:
            return False
        if Alumne.criteri is 0:
            return self.__niu < alumne.getNiu()
        else:
            return self.__cognom < alumne.getCognom()
    def __gt__(self, alumne): # mayor que
        if Alumne.criteri is 0:
            return self.__niu > alumne.getNiu()
        else:
            return self.__cognom > alumne.getCognom()
        
    @staticmethod
    def test(*argv):
        print "Creando instancias de la clase alumno..."
        a0 = Alumne("Trolius", "Maximus", 1134567)
        a1 = Alumne("Andrew", "Faker", 2345671)
        a2 = Alumne("Cafe", "Relaxing", 3456712)
        a3 = Alumne("Mister", "Te", 4567123)
        a4 = Alumne("Nipek", "Innipokon", 7234561)
        a5 = Alumne("Bob", "Builder", 1634527)
        a6 = Alumne("Doge", "Cate", 1254367)
        a7 = Alumne("Fast", "Gottago", 8234467)
        a8 = Alumne("Irene", "Keyerror", 1236667)
        a9 = Alumne("Selphy", "Dotbar", 1242267)
        print "//---Insertando instancias en un array con criterio de ordenacion NIU---//"
        Alumne.criteri = 0
        alumnos = SortedSequenceAsArray(10)
        for i in range(10):
            alumnos.insert(eval("a"+str(i)))
        print alumnos
        print "//----Busqueda con BinarySearch----//"
        for i in range(10):
            result = binarySearch(alumnos, eval("a"+str(i)))
            print eval("a"+str(i)), result
        print
        print "//---Insertando instancias en un array con criterio de ordenacion Cognom---//"
        Alumne.criteri = 1
        alumnos = SortedSequenceAsArray(10)
        for i in range(10):
            alumnos.insert(eval("a"+str(i)))
        print alumnos
        print "//----Busqueda con BinarySearch----//"
        for i in range(10):
            result = binarySearch(alumnos, eval("a"+str(i)))
            print eval("a"+str(i)), result
            
if __name__ == "__main__":
        Alumne.test()
