import glfw

from grafico import Grafico

class Controlador(object):
    def __init__(self):
        self.modelacion = None
        self.dia = 1


    def setModelo(self, modelo):
        self.modelacion = modelo

    def setDibujos(self, dibujos):
        self.dibujo = dibujos

    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return

        if key == glfw.KEY_ESCAPE:
            glfw.terminate()
            sys.exit()

        elif (key == glfw.KEY_P) and action == glfw.PRESS:
            grafico = Grafico()
            grafico.graficar(self.modelacion.getEstadisticas())
            print("P")

        elif (key == glfw.KEY_R) and action == glfw.PRESS:
            self.modelacion.nuevoContagio()
            
        elif (key == glfw.KEY_E) and action == glfw.PRESS:
            self.modelacion.perdidaInmunidad()

        elif (key == glfw.KEY_RIGHT) and action == glfw.PRESS:
            self.modelacion.iteracion()
            print("Dia " + str(self.dia))
            self.dia+=1
            print("guardando las estadisticas")
            for individuo in self.dibujo:
                individuo[0].mover(individuo[1].getPosicionX(), individuo[1].getPosicionY())
            print("Avanzo")

        else:
            return    
