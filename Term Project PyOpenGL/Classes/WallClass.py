from Classes.SurfaceClass import *

class Wall(Surface):
    def __init__(self, shader, material, materialSize, side, position, width, length):
        self.material = material
        self.materialSize = materialSize
        self.shader = shader
        self.position = position #position is based on the direct center of the cube
        self.side = side
        self.angle = [0, 0, 0] #placeholder
        self.rotation = np.array([0, 0, 0], dtype=np.float32) #initialize
        
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
        
        if (self.side == "north"):
            self.vertices = (
                -width*widthMaterialScale, 0,  length*lengthMaterialScale,  width*widthTextureScale, 0, 0, -1,  0,
                -width*widthMaterialScale, 0, -length*lengthMaterialScale, width*widthTextureScale, length*lengthTextureScale, 0, -1, 0,
                width*widthMaterialScale, 0, -length*lengthMaterialScale,  0, length*lengthTextureScale, 0, -1,  0,

                width*widthMaterialScale, 0, -length*lengthMaterialScale,  0, length*lengthTextureScale, 0, -1,  0,
                width*widthMaterialScale, 0, length*lengthMaterialScale,  0, 0, 0, -1,  0,
                -width*widthMaterialScale, 0, length*lengthMaterialScale,   width*widthTextureScale, 0,  0, -1, 0,
                )

            self.normal = np.array((0, -1, 0), dtype=np.float32)
            self.rotation[2] = 90
        
        elif (self.side == "south"):
            self.vertices = (
                width*widthMaterialScale, 0, -length*lengthMaterialScale,  0, length*lengthTextureScale, 0, 1,  0,
                -width*widthMaterialScale, 0, -length*lengthMaterialScale, width*widthTextureScale, length*lengthTextureScale, 0, 1, 0,
                -width*widthMaterialScale, 0,  length*lengthMaterialScale,  width*widthTextureScale, 0, 0, 1,  0,

                -width*widthMaterialScale, 0, length*lengthMaterialScale,   width*widthTextureScale, 0,  0, 1, 0,
                width*widthMaterialScale, 0, length*lengthMaterialScale,  0, 0, 0, 1,  0,
                width*widthMaterialScale, 0, -length*lengthMaterialScale,  0, length*lengthTextureScale, 0, 1,  0,
                )
            
            self.normal = np.array((0, 1, 0), dtype=np.float32)
            self.rotation[2] = -90
            
            
        elif (self.side == "west"):
            self.vertices = (
                0, width*widthMaterialScale, -length*lengthMaterialScale,  0, length*lengthTextureScale, -1, 0,  0,
                0, -width*widthMaterialScale, -length*lengthMaterialScale, width*widthTextureScale, length*lengthTextureScale, -1, 0, 0,
                0, -width*widthMaterialScale, length*lengthMaterialScale,  width*widthTextureScale, 0, -1, 0,  0,

                0, -width*widthMaterialScale, length*lengthMaterialScale,   width*widthTextureScale, 0,  -1, 0, 0,
                0, width*widthMaterialScale, length*lengthMaterialScale,  0, 0, -1, 0,  0,
                0, width*widthMaterialScale, -length*lengthMaterialScale,  0, length*lengthTextureScale, -1, 0,  0,
                )
            
            self.normal = np.array((-1, 0, 0), dtype=np.float32)
            self.rotation[2] = 0
            
        elif (self.side == "east"):
            self.vertices = (
                0, -width*widthMaterialScale, length*lengthMaterialScale,  width*widthTextureScale, 0, 1, 0,  0,
                0, -width*widthMaterialScale, -length*lengthMaterialScale, width*widthTextureScale, length*lengthTextureScale, 1, 0, 0,
                0, width*widthMaterialScale, -length*lengthMaterialScale,  0, length*lengthTextureScale, 1, 0,  0,

                0, width*widthMaterialScale, -length*lengthMaterialScale,  0, length*lengthTextureScale, 1, 0,  0,
                0, width*widthMaterialScale, length*lengthMaterialScale,  0, 0, 1, 0,  0,
                0, -width*widthMaterialScale, length*lengthMaterialScale,   width*widthTextureScale, 0,  1, 0, 0,
                )
            
            self.normal = np.array((1, 0, 0), dtype=np.float32)
            self.rotation[2] = 180
        
    
        #self.angle = np.arcsin(self.normal)
        
        self.glBinds()