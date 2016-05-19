from pyrobot.brain import Brain
from stackAsLinkedList import *
import Pilot
reload (Pilot)
class WB(Brain):
    def setup(self):
        self.stack = StackAsLinkedList()
        self.pilot = Pilot.Pilot()
        self.robot.move("reset")
    def step(self):
        if (self.robot.getItem("win") == 0):
            self.pilot.setSonar(self.robot.getItem("sonar")) #enviamos los valores del sonar a la clase piloto
            if ((self.robot.getItem("golds")) >= 0):
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
                        for ac in posible_actions: #anadimos al stack todas las posibles acciones del cruce
                            self.stack.push(ac)
                        self.action = self.stack.pop()
                    self.action = self.pilot.moveTo(self.action[1]) #tupla de possibleActions [True/False, "Direccion"]
                else:
                    self.action = self.pilot.nextMove()
                self.lastaction = self.robot.move(self.action)
                if self.lastaction == "gold":
                    self.robot.move("grab")
def INIT(engine):
    return WB("WB", engine)


