import math, random, time

from Graphics.cmu_112_graphics import *
from Graphics.transformMatrices import *
from Graphics.drawTriangle import *
from Graphics.drawCrosshair import *

from GameFunctions.worldComponents import * #* import classes here
from GameFunctions.keyPressedReleased import *
from GameFunctions.movePlayer import *
from GameFunctions.floorIsLava import *

# from printNdList import *

#TODO FIGURE OUT CORRECT FPS
#? Potentially clip against x and y planes, cull against far plane

#TODO Flat shading, will have to either pass through new object or another dimension in triangle with tuple of color
#TODO determine color when getting normal, pass through everything


#* Update a specific component that needs updating (world coordinates moved)
def updateComponent(app):
    for component in app.components:
        if (isinstance(component, RectPrism)):
            
            if (component.updateNeeded):
                component.moveAround(-app.posX, -app.posY, -app.posZ,
                                         app.thetaX, app.thetaY, app.thetaZ,
                                         app.aspectRatio, app.fov, app.nearBound, app.farBound)
                component.updateNeeded = False


#* Update every single component
def moveCamera(app):
    for component in app.components:
        if (not component.inHand): #TODO pick up objects
            if (isinstance(component, RectPrism)):
                component.moveAround(-app.posX, -app.posY, -app.posZ,
                                        app.thetaX, app.thetaY, app.thetaZ,
                                        app.aspectRatio, app.fov, app.nearBound, app.farBound)
    for component in app.worldComponents: #? Probably don't need the if statement now
        if (isinstance(component, Wall) or isinstance(component, Floor) or isinstance(component, Ceiling)):
            component.moveAround(-app.posX, -app.posY, -app.posZ,
                                        app.thetaX, app.thetaY, app.thetaZ,
                                        app.aspectRatio, app.fov, app.nearBound, app.farBound)
    
    
#* Order drawn in terms of components
def orderComponents(app):
    if (len(app.components) >= 1):
        #! sorts by the last triangle created per object, lots of problems with this but it is efficient
        app.components = sorted(app.components, key=lambda x: (x.finalTriangles[-1].triangle[-1][2]
                                if ((len(x.finalTriangles) > 0)) else -1), reverse=True)


#* Tick
def GameMode_timerFired(app):
    
    app.time += 1
    
    for component in app.components:
        if (component.dx or component.dy or component.dz):
            component.translatePrism(component.dx, component.dy, component.dz)
        if (app.time % 200 == 0): #idk time is weird and changes every single level
            component.dx *= -1
        if (app.time % 500 == 0):
            component.dz *= -1
    
    
    #* Camera Movement
    app.thetaX += app.dThetaX
    if (app.thetaX > math.pi/2):
        app.thetaX = math.pi/2
    elif (app.thetaX < -math.pi/2):
        app.thetaX = -math.pi/2
    app.thetaY += app.dThetaY
    app.thetaZ += app.dThetaZ
    
    
     
    if (app.dx or app.dy or app.dz or
        app.dThetaX or app.dThetaY or app.dThetaZ):
        moveCamera(app) #if the camera moves or rotates at all
    else:
        updateComponent(app) #will update only the components that need updating (world position changed)
    
    orderComponents(app) #order in terms of NDC z value of last triangle drawn now
    
    #* Player Movement
    movePlayer(app)
    checkCompleteLevel(app)
    
    
    checkFloorIsLava(app)
    
    
    
    


#* Draw
def GameMode_redrawAll(app, canvas):
    
    for worldComponent in app.worldComponents:
        if (len(worldComponent.finalTriangles) > 0):
            for triangle in range(len(worldComponent.finalTriangles)):
                drawTriangle(app, canvas, worldComponent.finalTriangles[triangle])
                
    for component in app.components:
        if (len(component.finalTriangles) > 0):
            for triangle in range(len(component.finalTriangles)):
                #if (component.triangles[triangle].doesNotExist == False):
                drawTriangle(app, canvas, component.finalTriangles[triangle])


    drawCrosshair(app, canvas)


    canvas.create_text(app.width//20, app.height//20, text=f"Extra Lives: {app.lives}", fill="white")
    canvas.create_text(app.width-app.width//20, app.height//20, text=f"Press P for help", fill="white")


