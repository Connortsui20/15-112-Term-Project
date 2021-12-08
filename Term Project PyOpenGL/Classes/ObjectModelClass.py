from OpenGL.GL import *
import numpy as np

from Classes.SurfaceClass import *

#! I take absolutely 0 credit for this function, takes an object file and converts to a single array
#! Only thing I implemented was the last function call and the rotation matrix and naming

#! This is not actually used right now, it is only for the sake of testing, but you can add an object model into components

class ObjModel(Surface):
    def __init__(self, path, shader, material, position, angle, name):
        self.shader = shader
        self.material = material
        self.position = position
        self.angle = angle
        
        # np.array((np.sin(np.radians(0)), 0, 0))
        self.name = name
        glUseProgram(shader)
        v = []
        vt = []
        vn = []
        self.vertices = []

        #open the obj file and read the data
        with open(f"{path}",'r') as f:
            line = f.readline()
            while line:
                firstSpace = line.find(" ")
                flag = line[0:firstSpace]
                if flag=="mtllib":
                    #declaration of material file
                    pass
                elif flag=="v":
                    #vertex
                    line = line.replace("v ","")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    v.append(l)
                    #print(v)
                elif flag=="vt":
                    #texture coordinate
                    line = line.replace("vt ","")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    vt.append(l)
                elif flag=="vn":
                    #normal
                    line = line.replace("vn ","")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    vn.append(l)
                elif flag=="f":
                    #face, four vertices in v/vt/vn form
                    line = line.replace("f ","")
                    line = line.replace("\n","")
                    line = line.split(" ")
                    theseVertices = []
                    theseTextures = []
                    theseNormals = []
                    for vertex in line:
                        l = vertex.split("/")
                        position = int(l[0]) - 1 #index correction of the index
                        theseVertices.append(v[position])
                        texture = int(l[1]) - 1
                        theseTextures.append(vt[texture])
                        normal = int(l[2]) - 1
                        theseNormals.append(vn[normal])
                    # obj file uses triangle fan format for each face individually.
                    # unpack each face
                    triangles_in_face = len(line) - 2

                    vertex_order = []
                    for i in range(triangles_in_face):
                        vertex_order.append(0)
                        vertex_order.append(i+1)
                        vertex_order.append(i+2)
                    for i in vertex_order:
                        for x in theseVertices[i]:
                            self.vertices.append(x)
                        for x in theseTextures[i]:
                            self.vertices.append(x)
                        for x in theseNormals[i]:
                            self.vertices.append(x)
                    
                line = f.readline() #end on empty string
                
        self.vertices = np.array(self.vertices,dtype=np.float32)
      
        self.glBinds()

