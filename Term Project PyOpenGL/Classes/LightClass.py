from OpenGL.GL import *
import numpy as np

from Classes.BasicCubeClass import *

class Light:
    def __init__(self, shaders, color, position, strength, index):
        self.position = np.array(position, dtype=np.float32)
        self.model = BasicCube(shaders[0], self.position, 0.2, 0.2, 0.2, color[0], color[1], color[2])
        self.color = np.array(color, dtype=np.float32)
        self.shader = shaders[1]
        self.strength = strength
        self.index = index


    def update(self): #not mine
        glUseProgram(self.shader) #using fragment shader
        glUniform3fv(glGetUniformLocation(self.shader, f"lights[{self.index}].pos"), 1, self.position)
        glUniform3fv(glGetUniformLocation(self.shader, f"lights[{self.index}].color"), 1, self.color)
        glUniform1f(glGetUniformLocation(self.shader, f"lights[{self.index}].strength"), self.strength)
        glUniform1i(glGetUniformLocation(self.shader, f"lights[{self.index}].enabled"), 1)


    def draw(self):
        self.model.draw()


    def destroy(self):
        self.model.destroy()