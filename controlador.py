import glfw


class Controlador(object):
    def __init__(self):
        self.modelacion = None

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
            # cosas de los graficos
            print("P")

        elif (key == glfw.KEY_RIGHT) and action == glfw.PRESS:
            self.modelacion.iteracion()
            print("guardadas las estadisticas")
            for individuo in self.dibujo:
                individuo[0].mover(individuo[1].getPosicionX(), individuo[1].getPosicionY())
            print("Avanzo")
