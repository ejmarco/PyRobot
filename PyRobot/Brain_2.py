from pyrobot.brain import Brain
import Pilot
reload (Pilot)
class WB(Brain):
    def setup(self):
        self.whereami = None
        self.inverse = {"right" : "left", "up" : "down", "left" : "right", "down" : "up"}
        self.actions = ['left', 'up', 'up', 'left']
        self.backtrace = ["right"]
        self.pilot = Pilot.Pilot()
        self.robot.move("reset")
    def step(self):
        if (self.robot.getItem("win") == 0):
            self.pilot.setSonar(self.robot.getItem("sonar")) #enviamos los valores del sonar a la clase piloto
            if ((self.robot.getItem("golds")) > 0):
                if self.pilot.isCrossRoad(): #isCrossRoad devuelve true si se cumple
                    self.action = self.actions.pop() #cogemos una accion de la lista
                    self.robot.move(self.action)
                else:
                    self.action = self.pilot.nextMove() #llamamos a nextmove para decidir el siguiente movimiento
                    self.whereami = self.robot.move(self.pilot.moveTo(self.action))
                if self.whereami == "gold":
                    self.robot.move("grab")
                self.backtrace.append(self.action) #agregamos la ultima accion a la lista de backtrace
            else:
                self.robot.move(self.inverse[self.backtrace.pop()]) #recorrer la lista en sentido inverso
def INIT(engine):
    return WB("WB", engine)
