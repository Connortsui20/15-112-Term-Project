import math

from Classes.RectPrismClass import *
from HelpScreen import *

# from printNdList import *

#! NOT WORKING PROPERLY
#! WANT TO CHANGE MOVEMENT BASED ON CURRENT ANGLE

def GameMode_keyPressed(app, event):
    
    # camera rotation
    if (event.key == "Right"):
        app.dThetaY = math.radians(app.rotationScale)
    elif (event.key == "Left"):
        app.dThetaY = -math.radians(app.rotationScale)
    elif (event.key == "Down"):
        app.dThetaX = -math.radians(app.rotationScale)
    elif (event.key == "Up"):
        app.dThetaX = math.radians(app.rotationScale)
    
    # camera movement
    elif (event.key == "w"):
        app.wPressed = True
    elif (event.key == "s"):
        app.sPressed = True
    elif (event.key == "a"):
        app.aPressed = True
    elif (event.key == "d"):
        app.dPressed = True
    
    # up down
    elif (event.key == "Space"):
        if (app.crouch): #? again probably a better way to do this but don't know
            if (app.posY == app.playerHeight+app.minHeight-app.crouchAmount): #prevent flying
                app.dy = app.jumpSpeed
        else:
            if (app.posY == app.playerHeight+app.minHeight):
                app.dy = app.jumpSpeed
            
    # crouch
    elif (event.key == "Tab"):
        if (not app.crouch): #only do it once
            app.translationScale /= app.slowed
            app.jumpSpeed /= (app.slowed*2/3)
        app.crouch = True
        app.posY -= app.crouchAmount
        
    # # reset debugging
    # elif (event.key == "r"):
    #     app.appStarted()
        
    elif (event.key == "p"):
        app.mode = "HelpMode"

    
     
def GameMode_keyReleased(app, event):
    # rotations
    if (event.key == "Right"):
        app.dThetaY = 0
    elif (event.key == "Left"):
        app.dThetaY = 0
    elif (event.key == "Down"):
        app.dThetaX = 0
    elif (event.key == "Up"):
        app.dThetaX = 0
        
   # camera movement
    elif (event.key == "w"):
        app.wPressed = False
    elif (event.key == "s"):
        app.sPressed = False
    elif (event.key == "a"):
        app.aPressed = False
    elif (event.key == "d"):
        app.dPressed = False
    
    #crouch
    elif (event.key == "Tab"):
        if (app.crouch): #only do it once
            app.translationScale *= app.slowed
            app.jumpSpeed *= (app.slowed*2/3)
        app.crouch = False
        app.posY += app.crouchAmount




