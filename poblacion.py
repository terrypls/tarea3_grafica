import json
import random
from individuo import Individuo


class Poblacion(object):
    def __init__(self,nombre):
        with open(nombre) as json_file:
            data = json.load(json_file)
        data = data[0]
        self.radio = data["Radius"]
        self.prob_contagio = data["Contagious_prob"]
        self.prob_muerte = data["Death_rate"]
        self.poblacion_inicial = data["Initial_population"]
        self.dias_recuperacion = data["Days_to_heal"]
        self.poblacion = []
        self.estadisticas = []

    def getPoblacion(self):
        return self.poblacion_inicial

    def getEstadisticas(self):
        return self.estadisticas

    def setNewRadio(self, radio):
        self.radio = radio

    def getIndividuos(self):
        return self.poblacion

    def crearIndividuos(self):
        for i in range(self.poblacion_inicial - 1):
            individuo = Individuo(self.prob_contagio, self.prob_muerte, self.dias_recuperacion)
            self.poblacion.append(individuo)
        individuo_contagiado = Individuo(self.prob_contagio, self.prob_muerte, self.dias_recuperacion)
        individuo_contagiado.setContagiado()
        self.poblacion.append(individuo_contagiado)
        self.estadisticas.append([1, self.poblacion_inicial - 1, 0])  # enfermos, vivos, muertos

    def cadenaDeContagios(self):
        tupla = tuple(self.poblacion)
        for i in range((len(tupla))):
            if tupla[i].isContagiado():
                posx = tupla[i].getPosicionX()
                posy = tupla[i].getPosicionY()
                for k in range((len(tupla))):
                    self.poblacion[k].contagiar(posx, posy, self.radio)

    def recuperados(self):
        for ind in self.poblacion:
            ind.recuperacion()

    def crearEstadistica(self):
        muertos = 0
        vivos = 0
        enfermos = 0
        for ind in self.poblacion:
            if not ind.isVivo():
                muertos += 1
            elif ind.isContagiado():
                enfermos += 1
            else:
                vivos += 1
            ind.cambiarPosicion()
        total = muertos + vivos + enfermos

        if total != len(self.poblacion):
            print("ERRRRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOR " + str(total))
        else:
            self.estadisticas.append([enfermos, vivos, muertos])

    def nuevoContagio(self):
        contador = 0
        for ind in self.poblacion:
            if ind.isVivo() and not ind.isContagiado() and not ind.isRecuperado():
                ind.setContagiado()
                contador += 1
            if contador == 3:
                print("se contagio a 3 personas al azar")
                break
        if contador!=3:
            print("Todos eran inmunes :O")   

    def perdidaInmunidad(self):
        dias = random.randint(1, 5)
        modulo = random.randint(2, 6)
        contador = 0
        for i in range(len(self.poblacion)):
            if i % modulo == 0 and self.poblacion[i].isRecuperado():
                self.poblacion[i].perdidaInmunidad(dias)
                contador+=1
        print("Personas no inmunes =" +str(contador))
                
    def iteracion(self):
        self.cadenaDeContagios()
        self.recuperados()
        self.crearEstadistica()
        print(self.getEstadisticas()[-1])
