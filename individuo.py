import random

class Individuo(Object):
    def __init__(self,prob_contagio,prob_muerte,dias_recuperacion):
        self.vivo = True
        self.contagiado = False
        self.recuperado = False
        self.pos_x = round(random.uniform(-1, 1),3)
        self.pos_y = round(random.uniform(-1, 1), 3)
        self.dias_recuperacion = dias_recuperacion
        self.prob_muerte = prob_muerte
        self.prob_contagio = prob_contagio


    def isContagiado(self):
        return self.contagiado
    
    def isVivo(self):
        return self.vivo
    
    def isRecuperado(self):
        return self.recuperado



    def contagiado(self):
        self.contagiado = True
    
    def muerto(self):
        self.vivo = False
        
    def recuperacion(self):
        prob = random()
        if self.isContagiado() and self.isVivo() and not self.recuperado:
            if prob < self.prob_muerte:
                self.muerto()
            else:
                self.dias_recuperacion -= 1
        
        if self.dias_recuperacion <= 0:
            self.recuperado =True
        

    def getPosicion(self):
        return [self.pos_x, self.pos_y]
    def getPosicionX(self):
        return self.pos_x
    def getPosicionY(self):
        return self.pos_y
        
    def cambiarPosicion(self, x, y):
        pass

    def interseccion(self, x, y, radio):
        if (x - radio <= self.pos_x <= x + radio) and (y - radio <= self.pos_y <= y - radio):
            return True
        else:
            return False

    def contagiar(self, x, y,radio):
        prob = random()
        if self.isRecuperado() or self.isContagiado() or not self.isVivo():
            pass
        elif interseccion(x, y, radio) and prob < self.prob_contagio:
            self.contagiado()
        else:
            pass
        

