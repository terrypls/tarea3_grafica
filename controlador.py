import glfw

class Controlador(object):
    def __init__(self):
        self.modelacion = None

    def setModelo(self, modelo):
        self.modelacion = modelo
        
    def on_key(self, window, key, scancode, action, mods):
        if not (action == glfw.PRESS or action == glfw.RELEASE):
            return

        if key == glfw.KEY_ESCAPE:
            glfw.terminate()
            sys.exit()

        elif (key == glfw.KEY_P) and action == glfw.PRESS:
            #cosas de los graficos
            print("P")
        
        elif (key == glfw.KEY_RIGHT) and action == glfw.PRESS:
            self.modelacion.iteracion()
            print("Avanzo")