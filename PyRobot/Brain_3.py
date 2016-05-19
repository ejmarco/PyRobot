from pyrobot.brain import Brain
from queueAsLinkedList import *
import Pilot
reload (Pilot)

class WB(Brain):
    def setup(self):
        self.lastaction = None
        self.inverse = {"right" : "left", "up" : "down", "left" : "right", "down" : "up"}
        self.counter = 0
        self.actions = QueueAsLinkedList()
        self.backtrace = ["right"]
        self.pilot = Pilot.Pilot()
        self.robot.move("reset")
    def step(self):
        if (self.robot.getItem("win") == 0):
            self.pilot.setSonar(self.robot.getItem("sonar")) #enviamos los valores del sonar a la clase piloto
            if ((self.robot.getItem("golds")) > 0):
                if self.pilot.isCrossRoad(): #isCrossRoad devuelve true si se cumple
                    talk = self.robot.move("talk")
                    if self.lastaction == "wumpus" and talk != "This thing doesn't speak!":
                        #hablar con el wumpus
                        self.actions.enqueue(talk) #metemos en la cola la accion que dice wumpus
                    else:
                        self.action = self.actions.dequeue() #cogemos una accion de la lista
                        self.robot.move(self.action)
                        self.backtrace.append(self.action)
                else:
                    self.action = self.pilot.nextMove() #llamamos a nextmove para decidir el siguiente movimiento
                    self.lastaction = self.robot.move(self.pilot.moveTo(self.action)) #movemos y guardamos el resultado de moverse
                    if self.lastaction == "gold":
                        self.robot.move("grab")
                    self.backtrace.append(self.action) #agregamos la ultima accion a la lista de backtrace
            else:
                self.robot.move(self.inverse[self.backtrace.pop()]) #recorrer la lista en sentido inverso
def INIT(engine):
    return WB("WB", engine)
