import math

from GameFunctions.worldComponents import *

def initGame(app): #TODO add arguments here
    
    app.timerDelay = 0
    app.time = 0
    
    #* "Global" Constants
    #app.fps = 90 #! assume for now
    app.gravity = (app.gravitySet*100)/(10*app.fps) #! Tune later !!
    app.jumpSpeed = app.jumpSpeedSet/app.fps
    app.translationScale = app.translationScaleSet/app.fps
    app.rotationScale = 150/app.fps
    app.slowed = 2
    app.playerHeight = 170
    app.crouch = False
    app.crouchAmount = app.playerHeight/2
    
    #* Screen settings
    app.aspectRatio = app.width/app.height
    #app.fov = 100
    app.nearBound = 20 #* Consider this the face of the user?
    app.bodyWidth = app.nearBound + app.playerHeight/10 #* make this bigger to make it easier, bug with really big width
    app.farBound = 2000
    
    #* Camera (player) settings
    app.startPosition = (0, app.playerHeight+400, -250)  #avg height of human is 170 cm
    app.posX, app.posY, app.posZ = app.startPosition
    app.thetaX, app.thetaY, app.thetaZ = 0, math.radians(0), 0
    app.dx, app.dy, app.dz = 0, 0, 0
    app.wdx, app.sdx, app.adx, app.ddx = 0, 0, 0, 0
    app.wdz, app.sdz, app.adz, app.ddz = 0, 0, 0, 0
    app.ddy = 0
    app.dThetaX, app.dThetaY, app.dThetaZ = 0, 0, 0
    
    app.levelEndMinX = -300
    app.levelEndMaxX = 300
    app.levelEndMinZ = 1300
    app.levelEndMaxZ = 1500
    
    #* Change Start Level here
    app.level = 0
    createWorld(app) #creates all components
    
    
    
    app.wPressed = False
    app.sPressed = False
    app.aPressed = False
    app.dPressed = False
    
    
    