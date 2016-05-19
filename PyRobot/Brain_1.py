from pyrobot.brain import Brain
class WB (Brain):
        """Classe que contindra la funcionalitat del robot"""
	def setup(self):
                """Inicialitzacio de les variables membre de la classe"""
		self.counter = 0
		"""compta el nombre de pasos del robot"""
		self.inverse = {'right':'left', 'up':'down', 'left':'right', 'down':'up'}
		"""Diccionari que conte l'accio inversa a un moviment"""
		self.actions = ['right', 'right', 'up', 'up','left','left','up','up','left','up','up','right','up','up','up','right','right','down','down','right','right','right','right','up','up','left','left']
		"""Variable que conte tots els moviments fin a arribar a l'or"""
		self.robot.move('reset')
		"""Accio perque el robot sorti des de l'inici"""
		
	def step(self):
                """Definicio dels moviments del robot"""
		if (self.robot.getItem('win') == 0):
                        """Boolea que es posara a 1 quan haguem agafat l'or i anat a la sortida"""
                        if (self.counter >= 0):
                                """Amb aquesta condicio sabrem cuan hem agafat l'or i em tornat a la posicio inicial per mitja del self.counter -= 1"""
                                if ((self.robot.getItem("golds")) > 0):
                                        """Condicional que mira si ya no queda or per agafar"""
                                        position = self.robot.move(self.actions[self.counter])
                                        """Utilitzem una variable per guardar cada accio i saber quan agafarem l'or"""
                                        if (position == "gold"):
                                                """si hem agafat l'or l'agafem"""
                                                self.robot.move("grab")
                                        else:
                                                self.counter += 1
                                        """incrementem el contador de pasos"""
                                else:
                                        """Quan ya no queda or per agafar"""
                                        self.robot.move(self.inverse[self.actions[self.counter]])
                                        self.counter -= 1
			else:
                                """com que la meta es una casella adicional que apareix afegim el moviment necesari porque surti el robot i guanyi"""
                                self.robot.move("left")
                                print "robot stole the gold :)"
					
def INIT(engine):
		return WB('WB', engine)
