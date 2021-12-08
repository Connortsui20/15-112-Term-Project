from Classes.SurfaceClass import *

class Ceiling(Surface):
    def __init__(self, shader, material, materialSize, position, width, length):
        self.material = material
        self.materialSize = materialSize
        self.shader = shader
        self.position = position #position is based on the direct center of the cube
        self.angle = [0, 0, 0]
        self.rotation = np.array([0, 0, 0], dtype=np.float32)
        
        glUseProgram(self.shader)
        
        if (self.materialSize == "largeFloor"): #for 4x4
            widthTextureScale = 1/4
            lengthTextureScale = 1/4
            widthMaterialScale = 1
            lengthMaterialScale = 1
        elif (self.materialSize == "smallFloor"): #for 2x2
            widthTextureScale = 1/2
            lengthTextureScale = 1/2
            widthMaterialScale = 1
            lengthMaterialScale = 1
        elif (self.materialSize == "largeWall"): #for 2x1
            widthTextureScale = 1/2
            lengthTextureScale = 1
            widthMaterialScale = 1
            lengthMaterialScale = 2
        
        self.vertices = (
            
                 width*widthMaterialScale,  length*lengthMaterialScale,  0, width*widthTextureScale, length*lengthTextureScale, 0, 0,  -1,
                 width*widthMaterialScale, -length*lengthMaterialScale,  0, width*widthTextureScale, 0, 0, 0,  -1,
                -width*widthMaterialScale, -length*lengthMaterialScale,  0, 0, 0, 0, 0,  -1,

                -width*widthMaterialScale, -length*lengthMaterialScale,  0, 0, 0,  0, 0, -1,
                -width*widthMaterialScale,  length*lengthMaterialScale,  0, 0, length*lengthTextureScale, 0, 0,  -1,
                 width*widthMaterialScale,  length*lengthMaterialScale,  0, width*widthTextureScale, length*lengthTextureScale, 0, 0,  -1,

            )

        self.normal = np.array((0, 0, -1), dtype=np.float32)
        self.rotation[1] = -90
        
        self.glBinds()