import numpy as np

from Classes.WallClass import *
from Classes.FloorClass import *
from Classes.CeilingClass import *
from Classes.SurfaceClass import *

from Classes.ObjectModelClass import *


def createPortal(self, color):
    portalWidth = 3
    portalHeight = 5
    portalPos, normal, rotation = getPortalPosition(self.player.position, self.player.forwardVector,
                                          self.worldComponents, portalWidth, portalHeight)
    
    if (portalPos): #prevent None
        if (color == "blue"):
            self.bluePortal = Portal(self.shader, self.bluePortalTexture, portalPos, rotation, normal, portalWidth, portalHeight)
        elif (color == "orange"):
            self.orangePortal = Portal(self.shader, self.orangePortalTexture, portalPos, rotation, normal, portalWidth, portalHeight)



def getPortalPosition(position, lookVector, worldComponents, portalWidth, portalHeight): #TODO dont hardcode 16, 20 and 0
  
    for worldComponent in worldComponents:
        if (isinstance(worldComponent, Wall)):
            wall = worldComponent.side
            dot = np.dot(lookVector, worldComponent.normal) #make sure nothing behind happens
            if (dot < 0):
                if (wall == "west"): #* math is fun, good luck! This is just point slope formula
                    y = (lookVector[1]/lookVector[0])*((16-(portalWidth/2)) - position[0]) + position[1]
                    z = (lookVector[2]/lookVector[0])*((16-(portalWidth/2)) - position[0]) + position[2]
                    if (y < (16-(portalWidth/2)) and y > -(16-(portalWidth/2)) and z < (20-(portalHeight/2)) and z > (portalHeight/2)):
                        return ((16, y, z), worldComponent.normal, worldComponent.rotation)
                elif (wall == "east"):
                    y = (lookVector[1]/lookVector[0])*(-(16-(portalWidth/2)) - position[0]) + position[1]
                    z = (lookVector[2]/lookVector[0])*(-(16-(portalWidth/2)) - position[0]) + position[2]
                    if (y < (16-(portalWidth/2)) and y > -(16-(portalWidth/2)) and z < (20-(portalHeight/2)) and z > (portalHeight/2)):
                        return ((-16, y, z), worldComponent.normal, worldComponent.rotation)
                elif (wall == "north"):
                    x = (lookVector[0]/lookVector[1])*((16-(portalWidth/2)) - position[1]) + position[0]
                    z = (lookVector[2]/lookVector[1])*((16-(portalWidth/2)) - position[1]) + position[2]
                    if (x < (16-(portalWidth/2)) and x > -(16-(portalWidth/2)) and z < (20-(portalHeight/2)) and z > (portalHeight/2)):
                        return ((x, 16, z), worldComponent.normal, worldComponent.rotation)
                elif (wall == "south"):
                    x = (lookVector[0]/lookVector[1])*(-(16-(portalWidth/2)) - position[1]) + position[0]
                    z = (lookVector[2]/lookVector[1])*(-(16-(portalWidth/2)) - position[1]) + position[2]
                    if (x < (16-(portalWidth/2)) and x > -(16-(portalWidth/2)) and z < (20-(portalHeight/2)) and z > (portalHeight/2)):
                        return ((x, -16, z), worldComponent.normal, worldComponent.rotation)
                    
        elif (isinstance(worldComponent, Floor)):
            dot = np.dot(lookVector, worldComponent.normal) #make sure nothing behind happens
            if (dot < 0):
                x = (lookVector[0]/lookVector[2])*(0 - position[2]) + position[0]
                y = (lookVector[1]/lookVector[2])*(0 - position[2]) + position[1]
                if (x < (16-(portalWidth/2)) and x > -(16-(portalWidth/2)) and y < (16-(portalWidth/2)) and y > -(16-(portalWidth/2))):
                    return ((x, y, 0), worldComponent.normal, worldComponent.rotation)
                
        elif (isinstance(worldComponent, Ceiling)):
            dot = np.dot(lookVector, worldComponent.normal) #make sure nothing behind happens
            if (dot < 0):
                x = (lookVector[0]/lookVector[2])*((20-(portalHeight/2)) - position[2]) + position[0]
                y = (lookVector[1]/lookVector[2])*((20-(portalHeight/2)) - position[2]) + position[1]
                if (x < (16-(portalWidth/2)) and x > -(16-(portalWidth/2)) and y < (16-(portalWidth/2)) and y > -(16-(portalWidth/2))):
                    return ((x, y, 20), worldComponent.normal, worldComponent.rotation)
    
    return None, None, None #idk lmao


class Portal(Surface):
    def __init__(self, shader, material, position, rotation, normal, width, height):
        self.shader = shader
        self.material = material #! will figure it out someday probably hopefully
        
        self.position = position
        self.normal = normal
        
        self.rotation = rotation
        self.angle = np.radians(self.rotation)
        
        glUseProgram(self.shader)
        
        self.width = width
        self.height = height
        self.thickness = 0.01
        
        self.vertices = (
                -self.thickness, -self.width/2, -self.height/2,   0, 0, 0, 0, -1,
                 self.thickness, -self.width/2, -self.height/2,   1, 0, 0, 0, -1,
                 self.thickness,  self.width/2, -self.height/2,   1, 1, 0, 0, -1,

                 self.thickness,  self.width/2, -self.height/2,   1, 1, 0, 0, -1,
                -self.thickness,  self.width/2, -self.height/2,   0, 1, 0, 0, -1,
                -self.thickness, -self.width/2, -self.height/2,   0, 0, 0, 0, -1,

                -self.thickness, -self.width/2,  self.height/2,   0, 0, 0, 0,  1,
                 self.thickness, -self.width/2,  self.height/2,   1, 0, 0, 0,  1,
                 self.thickness,  self.width/2,  self.height/2,   1, 1, 0, 0,  1,

                 self.thickness,  self.width/2,  self.height/2,   1, 1, 0, 0,  1,
                -self.thickness,  self.width/2,  self.height/2,   0, 1, 0, 0,  1,
                -self.thickness, -self.width/2,  self.height/2,   0, 0, 0, 0,  1,

                -self.thickness,  self.width/2,  self.height/2,   1, 0, -1, 0,  0,
                -self.thickness,  self.width/2, -self.height/2,   1, 1, -1, 0,  0,
                -self.thickness, -self.width/2, -self.height/2,   0, 1, -1, 0,  0,

                -self.thickness, -self.width/2, -self.height/2,   0, 1, -1, 0,  0,
                -self.thickness, -self.width/2,  self.height/2,   0, 0, -1, 0,  0,
                -self.thickness,  self.width/2,  self.height/2,   1, 0, -1, 0,  0,

                 self.thickness,  self.width/2,  self.height/2,   1, 0, 1, 0,  0,
                 self.thickness,  self.width/2, -self.height/2,   1, 1, 1, 0,  0,
                 self.thickness, -self.width/2, -self.height/2,   0, 1, 1, 0,  0,

                 self.thickness, -self.width/2, -self.height/2,    0, 1, 1, 0,  0,
                 self.thickness, -self.width/2,  self.height/2,    0, 0, 1, 0,  0,
                 self.thickness,  self.width/2,  self.height/2,    1, 0, 1, 0,  0,

                -self.thickness, -self.width/2, -self.height/2,    0, 1, 0, -1,  0,
                 self.thickness, -self.width/2, -self.height/2,    1, 1, 0, -1,  0,
                 self.thickness, -self.width/2,  self.height/2,    1, 0, 0, -1,  0,

                 self.thickness, -self.width/2,  self.height/2,    1, 0, 0, -1,  0,
                -self.thickness, -self.width/2,  self.height/2,    0, 0, 0, -1,  0,
                -self.thickness, -self.width/2, -self.height/2,    0, 1, 0, -1,  0,

                -self.thickness,  self.width/2, -self.height/2,    0, 1, 0, 1,  0,
                 self.thickness,  self.width/2, -self.height/2,    1, 1, 0, 1,  0,
                 self.thickness,  self.width/2,  self.height/2,    1, 0, 0, 1,  0,

                 self.thickness,  self.width/2,  self.height/2,    1, 0, 0, 1,  0,
                -self.thickness,  self.width/2,  self.height/2,    0, 0, 0, 1,  0,
                -self.thickness,  self.width/2, -self.height/2,    0, 1, 0, 1,  0
            )
                
        self.glBinds()