from librerias import basic_shapes as bs
from librerias import easy_shaders as es
from librerias import scene_graph as sg
from librerias import transformations as tr
from OpenGL.GL import glClearColor

class Persona(object):
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y
                
        gpu_sano = es.toGPUShape(bs.createColorQuad(0, 1, 0))
        gpu_enfermo = es.toGPUShape(bs.createColorQuad(1, 0, 0))


        sano = sg.SceneGraphNode('Persona Sana')
        sano.transform = tr.scale(0.01, 0.01, 0)
        sano.childs = [gpu_sano]

        sanoPos = sg.SceneGraphNode('PersonaPos')
        sanoPos.transform = tr.translate(self.pos_x, self.pos_y, 0)
        sanoPos.childs=[sano]

        enfermo = sg.SceneGraphNode('Persona')
        enfermo.transform = tr.scale(0.01, 0.01, 0)
        enfermo.childs = [gpu_enfermo]

        enfermoPos = sg.SceneGraphNode('PersonaPos')
        enfermoPos.transform = tr.translate(self.pos_x, self.pos_y, 0)
        enfermoPos.childs = [enfermo]
        
        self.sano = sanoPos
        self.enfermo = enfermoPos 

    def draw(self, pipeline, sano):
        if sano:
            sg.drawSceneGraphNode(self.sano, pipeline, "transform")
        else:
            sg.drawSceneGraphNode(self.enfermo, pipeline, "transform")
