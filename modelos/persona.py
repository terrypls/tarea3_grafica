from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph as sg
from librerias import transformations as tr
from OpenGL.GL import glClearColor

class Persona(object):
    def __init__(self):
        gpu_persona = es.toGPUShape(bs.createColorQuad(220 / 255, 30 / 255, 40 / 255))
        
        persona = sg.SceneGraphNode('Persona')
        persona.transform = tr.scale(0.01, 0.01, 0)
        persona.childs = [gpu_persona]

        self.model = persona
        self.pos_x = 0
        self.pos_y = 0

    def draw(self, pipeline):
        sg.drawSceneGraphNode(self.model, pipeline, "transform")
