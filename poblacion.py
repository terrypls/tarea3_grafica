import json
import random
from individuo import Individuo

class Poblacion(Object):
    def __init__(self):
        with open('virus.json') as json_file:
            data = json.load(json_file)
        self.radio = data["Radius"]
        self.prob_contagio = data["Contagious_prob"]
        self.prob_muerte = data["Death_rate"]
        self.poblacion_inicial = data["Initial_population"]
        self.dias_recuperacion = data["Days_to_heal"]
        self.poblacion = []
        self.estadisticas =[]
        self.poblacion_actual = self.poblacion_inicial

    def setNewRadio(self, radio):
        self.radio = radio
    
    def crearIndividuos(self):
        for i in range(self.poblacion_inicial-1):
            individuo = Individuo(self.prob_contagio, self.prob_muerte, self.dias_recuperacion)
            self.poblacion.append(individuo)
        individuo_contagiado = Individuo(self.prob_contagio, self.prob_muerte, self.dias_recuperacion)
        individuo_contagiado.contagiado()
        self.poblacion.append(individuo_contagiado)
        self.estadisticas.append([1,999,0])

    def cadenaDeContagios(self):

        tupla = tuple(self.poblacion)
        for i in range((len(tupla))):
            if tupla[i].isContagiado():
                posx = tupla[i].getPosicionX()
                posy = tupla[i].getPosicionY()
                for k in range((len(tupla))):
                    self.poblacion[k].contagiar(posx, posy, self.radio)
                    


                

    def recuperados(self):
        
                        
        



            
    

        

