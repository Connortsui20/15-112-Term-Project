from Classes.MaterialClass import *
from Classes.CubeClass import *
from Classes.LightClass import *
from Classes.PlayerClass import *
from Classes.FloorClass import *
from Classes.WallClass import *
from Classes.CeilingClass import *


from Classes.ObjectModelClass import *

#* Component loading (world building)
def loadWorld(self):
    
    self.minWorldX, self.maxWorldX = -16, 16
    self.minWorldY, self.maxWorldY = -16, 16
    
    self.portalSmall2x2Concrete = Material(self.path + "textures/portalSmall2x2Concrete", "png")
    self.portalLarge2x1Concrete = Material(self.path + "textures/portalLarge2x1Concrete", "png")
    
    self.bluePortalTexture = Material(self.path + "textures/bluePortal", "png")
    self.orangePortalTexture = Material(self.path + "textures/orangePortal", "png")
    
    self.worldComponents = []
    self.worldComponents.append(Floor(self.shader, self.portalSmall2x2Concrete, "smallFloor", [0, 0, 0], 16, 16))
    self.worldComponents.append(Ceiling(self.shader, self.portalSmall2x2Concrete, "smallFloor", [0, 0, 20], 16, 16))

        
    self.worldComponents.append(Wall(self.shader, self.portalLarge2x1Concrete, "largeWall", "west", [self.maxWorldX, 0, 10], 16, 5))
    self.worldComponents.append(Wall(self.shader, self.portalLarge2x1Concrete, "largeWall", "east", [self.minWorldX, 0, 10], 16, 5))
    self.worldComponents.append(Wall(self.shader, self.portalLarge2x1Concrete, "largeWall", "north", [0, self.maxWorldY, 10], 16, 5))
    self.worldComponents.append(Wall(self.shader, self.portalLarge2x1Concrete, "largeWall", "south", [0, self.minWorldY, 10], 16, 5))
   
    self.lights = []
    self.lights.append(Light([self.shaderBasic, self.shader], [0.8, 0.8, 0.8], [14, 14, 16], 3, len(self.lights)))
    self.lights.append(Light([self.shaderBasic, self.shader], [0.8, 0.8, 0.8], [-14, -14, 16], 3, len(self.lights)))
    self.lights.append(Light([self.shaderBasic, self.shader], [0.8, 0.8, 0.8], [-14, 14, 16], 3, len(self.lights)))
    self.lights.append(Light([self.shaderBasic, self.shader], [0.8, 0.8, 0.8], [14, -14, 16], 3, len(self.lights)))
      
    self.components = []

    #* I'm going to keep this here for archiving sake
    # self.components.append(ObjModel(self.path + "Models/monkey.obj", self.shader, self.crateTexture,
    #                                 np.array([0, 0, 0], dtype=np.float32), np.array([0, 0, np.radians(0)]), "Monkey"))
    # self.components.append(ObjModel(self.path + "Models/testOval.obj", self.shader, self.crateTexture,
    #                                 np.array([0, 0, 0], dtype=np.float32), np.array([np.radians(-90), np.radians(0), np.radians(0)]), "Oval"))
    # self.components.append(Cube(self.shader, self.crateTexture,[1, 0, 0.5]))
    # self.components.append(Cube(self.shader, self.crateTexture,[2, 0, 0.5]))
    