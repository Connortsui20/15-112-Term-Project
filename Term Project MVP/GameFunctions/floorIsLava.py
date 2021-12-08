from GameOverScreen import *
from WinScreen import *

from GameFunctions.worldComponents import *



def checkCompleteLevel(app):
    if ( (app.posX > app.levelEndMinX) and (app.posX < app.levelEndMaxX) and
         (app.posZ > app.levelEndMinZ) and (app.posZ < app.levelEndMaxZ)  ):
        
        app.level += 1
        app.posX, app.posY, app.posZ = app.startPosition
        app.time = 0
        
        createWorld(app)
        
    if (app.level == 8):
        app.mode = "WinMode"





def checkFloorIsLava(app):
    
    if (app.cheats):
        adjust = 1000 #set to 0 when normally playing without cheats
    else:
        adjust = 0
    
    if (app.crouch): #? probably a better way to do this but no idea
        if (app.posY == app.playerHeight+app.floorHeight-app.crouchAmount-adjust):
            app.lives -= 1
            app.posX, app.posY, app.posZ = app.startPosition
            createWorld(app)
            #print(app.lives)
    else:
        if (app.posY == app.playerHeight+app.floorHeight-adjust):
            app.lives -= 1
            app.posX, app.posY, app.posZ = app.startPosition
            createWorld(app)
            #print(app.lives)
    
    
    
    
    
    if (app.lives == -1):
        app.mode = "GameOver"