import math
import numpy as np

from GameFunctions.keyPressedReleased import *


def movePlayer(app):
    if (app.wPressed):
        app.wdx = math.sin(app.thetaY)
        app.wdz = math.cos(app.thetaY)
    else:
        app.wdx = 0
        app.wdz = 0
        
    if (app.sPressed):
        app.sdx = -math.sin(app.thetaY)
        app.sdz = -math.cos(app.thetaY)
    else:
        app.sdx = 0
        app.sdz = 0
        
    if (app.aPressed):
        app.adx = -math.cos(app.thetaY)
        app.adz = math.sin(app.thetaY)
    else:
        app.adx = 0
        app.adz = 0
        
    if (app.dPressed):
        app.ddx = math.cos(app.thetaY)
        app.ddz = -math.sin(app.thetaY)
    else:
        app.ddx = 0
        app.ddz = 0
    
    app.dx = approachVelocity(app.dx, (app.wdx + app.sdx + app.adx + app.ddx))
    app.dz = approachVelocity(app.dz, (app.wdz + app.sdz + app.adz + app.ddz))
    
    checkCollisions(app)


#* Linear interpolation of movement (smooth movement)
#! Sort of not working at very small deltas, weird movement
def approachVelocity(currV, goalV, delta=5/12):
    
    difference = goalV - currV
    if (difference > delta):
        newV = currV + delta
    elif (difference < -delta):
        newV = currV - delta
    else:
        newV = goalV
    return newV



def checkCollisions(app):
    
    startPosX = app.posX
    startPosZ = app.posZ
    
    app.posX += app.dx*app.translationScale #move to new position
    app.posZ += app.dz*app.translationScale #only scale after normalized lerp or bad things happen
    
    # if one of these is within the bounds of a component, then move back
    result = findCollisionsXZ(app)
    if (result[0]):
        app.posX = startPosX
        app.posZ = startPosZ
    app.minHeight = result[1]

    positionY(app) #handles jumping and gravity
    
  
   
def findCollisionsXZ(app):
    
    xMin = app.posX-app.bodyWidth
    xMax = app.posX+app.bodyWidth
    zMin = app.posZ-app.bodyWidth
    zMax = app.posZ+app.bodyWidth
    
    found = False
    onTopOfObject = False
    minHeight = app.minHeight #store for later
    
    for component in app.components: #check legal move
        if  (  (( ((xMin + app.dx) > component.coord0[0]) and ((xMin + app.dx) < component.coord1[0]) ) or
                ( ((xMax + app.dx) > component.coord0[0]) and ((xMax + app.dx) < component.coord1[0]) ) ) and
               (( ((zMin + app.dz) > component.coord0[2]) and ((zMin + app.dz) < component.coord1[2]) ) or
                ( ((zMax + app.dz) > component.coord0[2]) and ((zMax + app.dz) < component.coord1[2]) ) )   ):
            
            if (app.crouch):
                if ( (app.posY-app.playerHeight) < component.coord1[1]-app.crouchAmount):
                    found = True
                    return (found, minHeight)
            else:
                if ( (app.posY-app.playerHeight) < component.coord1[1]):
                    found = True
                    return (found, minHeight)
            
            minHeight = component.coord1[1]
            onTopOfObject = True
                
    if (not onTopOfObject): #move back
        minHeight = app.floorHeight
    
    return (found, minHeight)
    
    
    
def positionY(app): #handles jump and gravity
    
    app.posY += app.dy
    app.dy -= app.gravity
    if (app.crouch): #? probably a better way to do this but no idea
        if (app.posY < app.playerHeight+app.minHeight-app.crouchAmount):
            app.posY = app.playerHeight+app.minHeight-app.crouchAmount
            app.dy = 0
    else:
        if (app.posY < app.playerHeight+app.minHeight):
            app.posY = app.playerHeight+app.minHeight
            app.dy = 0
    
    
    

    
    
    
    
    