from OpenGL.GL import *
import numpy as np
import pyrr

class Surface: #! Should not be used as an object, this is just for properties of other stuff
    
    #* Example init
    # def __init__(self, shader, material, position): #position should be a 1d list with x, y, z coords
    #     # self.material = material
    #     # self.shader = shader
    #     # self.position = position #position is based on the direct center of the cube
    #     # glUseProgram(self.shader)
    #     # self.vertices = ("x", "y", "z", "s", "t", "nx", "ny", "nz")
    #     pass
    
    def glBinds(self):
        self.vertex_count = len(self.vertices)//8 #each vertex has 8 attributes
        self.vertices = np.array(self.vertices, dtype=np.float32) #turn into array

        # Vertex Array Object, contains the VBO (thin state wrapper that tracks the pointer to the VBO)
        self.vao = glGenVertexArrays(1) #? idk what this line does, apparently it stores names
        glBindVertexArray(self.vao)
        
        # Vertex Buffer Object (contains the actual data)
        self.vbo = glGenBuffers(1) #? idk what these lines do either
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        '''
        Each number has 4 bytes, so each vertex will take up 8*4 bytes. This 32 byte chunk is caled a stride.
        Each stride has 3 attributes, xyz position, st texture, nxnynz normals.
        The last argument is a pointer to where in the stride (in terms of memory/bytes) the attribute begins.
        Yes, this is because OpenGL is written in C.
        '''
        
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8*4, ctypes.c_void_p(0*4))
        
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 8*4, ctypes.c_void_p(3*4))

        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8*4, ctypes.c_void_p((3+2)*4))
    
    
    def update(self): #! For now leave static
        glUseProgram(self.shader)

        transformMatrix = pyrr.matrix44.create_identity(dtype=np.float32)
        
        rotationMatrix = pyrr.matrix44.create_from_x_rotation(self.angle[0], dtype=np.float32)
        rotationMatrix = pyrr.matrix44.multiply(rotationMatrix, pyrr.matrix44.create_from_y_rotation(self.angle[1], dtype=np.float32))
        rotationMatrix = pyrr.matrix44.multiply(rotationMatrix, pyrr.matrix44.create_from_z_rotation(self.angle[2], dtype=np.float32))
        
        transformMatrix = pyrr.matrix44.multiply(transformMatrix, rotationMatrix)
        
        #* Perform transformations
        transformMatrix = (pyrr.matrix44.multiply(transformMatrix,
                pyrr.matrix44.create_from_translation(vec=np.array(self.position), dtype=np.float32)))
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, transformMatrix) #? No idea


    def draw(self):
        glUseProgram(self.shader)
        self.material.use() #binds everything
        
        #load in position
        transformMatrix = pyrr.matrix44.create_identity(dtype=np.float32)
        
        rotationMatrix = pyrr.matrix44.create_from_x_rotation(self.angle[0], dtype=np.float32)
        rotationMatrix = pyrr.matrix44.multiply(rotationMatrix, pyrr.matrix44.create_from_y_rotation(self.angle[1], dtype=np.float32))
        rotationMatrix = pyrr.matrix44.multiply(rotationMatrix, pyrr.matrix44.create_from_z_rotation(self.angle[2], dtype=np.float32))
        
        transformMatrix = pyrr.matrix44.multiply(transformMatrix, rotationMatrix)
        
        transformMatrix = pyrr.matrix44.multiply(transformMatrix, pyrr.matrix44.create_from_translation(vec=self.position, dtype=np.float32))
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, transformMatrix)

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, self.vertex_count) # should be 0-8
        

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))