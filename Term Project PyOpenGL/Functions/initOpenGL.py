from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr


def initOpenGL(self):
    #* Initialize opengl
    glClearColor(self.background[0], self.background[1], self.background[2], 1)
    
    #* All credit goes to GetIntoGameDev here, for some reason replacing "colour" with "color" breaks EVERYTHING
    self.shader = createShader(self.path + "shaders/vertex.txt", self.path + "shaders/fragment.txt")
    self.shaderBasic = createShader(self.path + "shaders/simple_3d_vertex.txt", self.path + "shaders/simple_3d_fragment.txt")
    
    resetLights(self) #all lights should be black unless initialized
    
    #* Initialize shaders
    glUseProgram(self.shader) #initialize shader for components
    projection_transform = pyrr.matrix44.create_perspective_projection(100, self.aspect, self.nearBound, self.farBound, dtype=np.float32) #projection matrix
    #! Data type needs to be in 32 bit otherwise things break idk why
    glUniformMatrix4fv(glGetUniformLocation(self.shader, "projection"), 1, GL_FALSE, projection_transform) #initialize component shader
    glUniform3fv(glGetUniformLocation(self.shader, "ambient"), 1, np.array(self.background, dtype=np.float32)) #ambient lighting
    glUniform1i(glGetUniformLocation(self.shader, "material.diffuse"), 0) #? No idea
    glUniform1i(glGetUniformLocation(self.shader, "material.specular"), 1) #? No idea
    
    #########################################
    
    glUseProgram(self.shaderBasic) #initialize shader for light and solid cubes
    glUniformMatrix4fv(glGetUniformLocation(self.shaderBasic, "projection"), 1, GL_FALSE, projection_transform)

    glEnable(GL_DEPTH_TEST) # z-buffer
    
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    
    # glEnable(GL_CULL_FACE) #* You can try enabling backface culling but sometimes it breaks stuff
    # glCullFace(GL_BACK)
    
    
#? I'm not even going to pretend to know how this works
def createShader(vertexFilepath, fragmentFilepath):
    with open(vertexFilepath,'r') as f:
        vertex_src = f.readlines()
    with open(fragmentFilepath,'r') as f:
        fragment_src = f.readlines()
    shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER),
                            compileShader(fragment_src, GL_FRAGMENT_SHADER))
    return shader


#* Turn off all the lights
def resetLights(self):
    glUseProgram(self.shader)
    for i in range(8):
        glUniform1i(glGetUniformLocation(self.shader, f"lights[{i}].enabled"), 0)
