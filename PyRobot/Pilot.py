class Pilot(object):
    __slot__ = ['__previous', '__sonar', '__inverse', '__culdesac'];
    def __init__(self):
        self.__previous = None
        self.__sonar = {'right' : False, 'down' : False, 'left' : False, 'up' : False}
        self.__inverse = {"right" : "left", "up" : "down", "left" : "right", "down" : "up"}
        self.__culdesac = False        
    def setSonar(self, sonar):
        self.__sonar = sonar
    def isCrossRoad(self):
        return sum(self.__sonar.values()) > 2 #un valor mayor de 2 devuelve true, es un cruce
    def getCulDeSac(self):
        return self.__culdesac
    def setCulDeSac(self,culdesac):
        self.__culdesac = culdesac
    def moveTo(self, action):
        if not self.__inverse.has_key(action):
            raise NameError, "Error"
        if self.__sonar[action] == True: #comprobar que el movimiento esta disponible en el sonar
            self.__previous = action
            return action
        else:
            raise NameError, "Error"
    def nextMove(self):
        motions = dict(self.__sonar)
        if self.__previous != None:
            motions[self.__inverse[self.__previous]] = 0 #anulamos la direccion de la que venimos
        if sum(motions.values()) == 0:
            self.setCulDeSac(True)
            self.__previous = self.__inverse[self.__previous] #volver atras
            return self.__previous
        else:
            for i in motions.items():
                if i[1] == True: #comprobamos que movimiento esta disponible
                    self.__previous = i[0] #modificamos previous para que contenga el movimiento disponible
            return self.__previous
    def possibleActions(self):
        motions = dict(self.__sonar)
        if self.__previous != None:
            motions[self.__inverse[self.__previous]] = 0 #anulamos la direccion de la que venimos
        lista = [(False, self.__inverse[self.__previous])]
        for mov in motions.items():
            if mov[1] == True:
                lista.append((True, mov[0])) #crear tupla de movimiento disponible
        return lista

