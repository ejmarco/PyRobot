from pyrobot.brain import Brain
import stackAsLinkedList
reload(stackAsLinkedList)
from  stackAsLinkedList import StackAsLinkedList
import Pilot
import DesTree
reload(DesTree)
reload(Pilot)


class WB(Brain):  
    def setup(self):
        self.counter = 0
        self.backtrace = []
        self.pilot = Pilot.Pilot()          
        self.stack = StackAsLinkedList()
        self.tree = DesTree.DesTree()
        #self.tree.Build('C:\LPpracticas\Practica6/db.xml')
        self.tree.Build('C:\PracticasPython\P6/db.xml')
        #self.tree.Build('C:\Temp\P6/db.xml')
        self.newdata = []
        self.robot.move('reset')
        self.door_locations =[]
        self.door_keys = []
        
    def step(self):
        if not(self.robot.getItem('win')):

            self.pilot.setSonar(self.robot.getItem('sonar')) #enviamos los valores del sonar a la clase piloto
            if ((self.robot.getItem("golds")) >= 0):
                talk = self.robot.move("talk")
                while talk != "This thing doesn't speak!" and talk != None: #si hay una respuesta de puerta/key
                    self.door_locations.append(talk)
                    talk = self.robot.move("talk")
                    if len(self.door_locations) > 17: #comprobacion de key, responde a talk mas de 17 veces
                        self.tree.AddData(self.door_locations) #anadimos el arbol que nos dio key
                        self.door_locations = []
                
                if talk is None:
                        self.door_keys.append(self.door_locations) #anadimos el arbol resultante en un animal en la lista de keys
                        for i in self.door_keys:
                            if self.tree.GetDataClass(i) != None: #recorremos la lista de keys y respondemos con el resultado
                                self.robot.move(self.tree.GetDataClass(i))
                                self.pilot.setSonar(self.robot.getItem('sonar')) #actualizar sonar tras abrir puerta
                        self.door_locations = []
                        
                if self.pilot.isCrossRoad(): #isCrossRoad devuelve true si se cumple
                            if self.pilot.getCulDeSac() and not self.stack.getIsEmpty(): #culdesac con contenido en pila
                                self.action = self.stack.pop()
                                if self.action[0]: #si sacamos una accion posible reseteamos culdesac
                                    self.pilot.setCulDeSac(False)
                                #self.action = self.robot.move(self.pilot.moveTo(self.action[1]))
                            else:
                                if self.stack.getIsEmpty(): #resetear culdesac
                                    self.pilot.setCulDeSac(False)
                                posible_actions = self.pilot.possibleActions()
                                for ac in posible_actions:
                                    self.stack.push(ac) #anadimos al stack todas las posibles acciones del cruce
                                self.action = self.stack.pop()
                            self.action = self.pilot.moveTo(self.action[1]) #tupla de possibleActions [True/False, "Direccion"]
                else:
                        self.action = self.pilot.nextMove()
                self.lastaction = self.robot.move(self.action)
                if self.lastaction == "gold":
                        self.robot.move("grab")                  
                
            


def INIT(engine):  
	return WB('WB', engine)

