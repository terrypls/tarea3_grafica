import glfw
from OpenGL.GL import *
import sys
from math import pi

from poblacion import Poblacion
from modelos.persona import Persona
from librerias import easy_shaders as es
from controlador import Controlador


def crearPersonas(poblacion):
    poblacion.crearIndividuos()
    return poblacion.getIndividuos()


def crearObjetosDibujo(individuo):
    dibujitos = []
    for ind in individuo:
        aux = [Persona(ind.getPosicionX(), ind.getPosicionY()), ind]
        dibujitos.append(aux)
    return dibujitos


def Simulador():
    # Initialize glfw
    if not glfw.init():
        sys.exit()

    width = 700
    height = 700

    window = glfw.create_window(width, height, 'Simulador de contagios', None, None)

    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    controlador = Controlador()

    # Connecting the callback function 'on_key' to handle keyboard events
    glfw.set_key_callback(window, controlador.on_key)

    # Assembling the shader program (pipeline) with both shaders
    pipeline = es.SimpleTransformShaderProgram()
    pipeline_texturas = es.SimpleTextureTransformShaderProgram()

    # Setting up the clear screen color
    glClearColor(245 / 255, 222 / 255, 179 / 255, 1.0)

    # Our shapes here are always fully painted
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    # magia para que no se vea negro el png
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    poblacion_modelo = Poblacion()
    individuos = crearPersonas(poblacion_modelo)

    personitas = crearObjetosDibujo(individuos)
    controlador.setModelo(poblacion_modelo)
    controlador.setDibujos(personitas)

    print(personitas[1][1].getPosicion())

    t0 = 0

    while not glfw.window_should_close(window):  # Dibujando --> 1. obtener el input
        # Using GLFW to check for input events
        glfw.poll_events()  # OBTIENE EL INPUT --> CONTROLADOR --> MODELOS

        # Clearing the screen in both, color and depth
        glClear(GL_COLOR_BUFFER_BIT)

        # Reconocer la logica

        # DIBUJAR LOS MODELOS

        glUseProgram(pipeline.shaderProgram)
        for dibujo in personitas:
            if dibujo[1].isVivo():
                dibujo[0].draw(pipeline, dibujo[1].isContagiado())

        # Calculamos el dt
        ti = glfw.get_time()
        margen = 1
        dt = ti - t0
        if dt > margen:
            t0 = glfw.get_time()

        # Once the render is done, buffers are swapped, showing only the complete scene.
        glfw.swap_buffers(window)

    glfw.terminate()
