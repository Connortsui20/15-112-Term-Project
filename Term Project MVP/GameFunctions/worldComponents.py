import random

from Classes.RectPrismClass import *
from Classes.WallClass import *
from Classes.FloorClass import *
from Classes.CeilingClass import *

#* From 15-112 website
def convertHex(r, g, b):
    if (r > 255):
        r = 255
    if (r < 0):
        r = 0
    if (g > 255):
        g = 255
    if (g < 0):
        g = 0
    if (b > 255):
        b = 255
    if (b < 0):
        b = 0
    return (f"#{r:02x}{g:02x}{b:02x}")


def convertRGB(hexString):
    # format = # FF 00 D3
    r = int(hexString[1:3], base=16) #convert hex to int
    g = int(hexString[3:5], base=16)
    b = int(hexString[5:7], base=16)
    return (r, g, b)


def createWorld(app):
    #* Every scene needs to have 1 floor and walls (ceiling not so important):
    floor = Floor( (-800, 0, -400), (800, 0, 1600), -app.posX, -app.posY, -app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(255, 0, 0))
    
    walls = Wall( (-800, 0, -400), (800, 800, 1600), -app.posX, -app.posY, -app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(100, 100, 100))
    
    ceiling = Ceiling( (-800, 800, -400), (800, 800, 1600), -app.posX, -app.posY, -app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(130, 30, 0))
    
    app.worldComponents = np.array((floor, walls, ceiling))
    
        
    app.floorHeight = app.worldComponents[0].floorMin # [1] is always the floor
    app.minHeight = app.floorHeight
    
    app.components = []
    
    # gold: convertHex(212, 175, 55)
    startPlate = RectPrism( (-300, 0, -300), (300, 150, -100), -app.posX, -app.posY, -app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(0, 230, 30))
    app.components.append(startPlate)
    
    
    endPlate = RectPrism( (-300, 0, 1300), (300, 150, 1500), -app.posX, -app.posY, -app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(0, 230, 30))
    app.components.append(endPlate)
    
    if (app.level == 0):
        level0(app)
    elif (app.level == 1):
        level1(app)
    elif (app.level == 2):
        level2(app)
    elif (app.level == 3):
        level3(app)
    elif (app.level == 4):
        level4(app)
    elif (app.level == 5):
        level5(app)
    elif (app.level == 6):
        level6(app)
    elif (app.level == 7):
        level7(app)
    elif (app.level == 8):
        level8(app)
    elif (app.level == 9):
        level9(app)
    elif (app.level == 10):
        level10(app)
    

def level0(app):
    
    bridge = RectPrism( (-150, 0, 0), (150, 100, 1200), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    app.components.append(bridge)



def level1(app):
    
    for i in range(6):
        tempPrism1 = RectPrism( (-100, 0, i*200+50), (100, 100, i*200+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        app.components.append(tempPrism1)
  
    

def level2(app):
      
    for i in range(4):
        tempPrism1 = RectPrism( (-100, 0, i*300+100), (100, 100, i*300+200), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # tempPrism2 = RectPrism( (100, 0, i*300+50), (200, 100, i*300+150), app.posX, app.posY, app.posZ,
        #                                         app.thetaX, app.thetaY, app.thetaZ,
        #                 app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        app.components.append(tempPrism1)
   
   
   
def level3(app):
    for i in range(6):
        if (i % 2 == 0):
            tempPrism1 = RectPrism( (-200, 0, i*200+50), (-100, 100, i*200+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        else:
            tempPrism1 = RectPrism( (100, 0, i*200+50), (200, 100, i*200+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        app.components.append(tempPrism1)
    
    
        
def level4(app):
    for i in range(3):
        tempPrism1 = RectPrism( (-100, 0, i*300-50), (100, 100, i*300+100), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tempPrism1.dz = 1
        app.components.append(tempPrism1)

   
   
def level5(app):
        
    for i in range(4):
        if (i % 2 == 0):
            tempPrism1 = RectPrism( (-150, 0, i*250-50), (-50, 100, i*250+100), app.posX, app.posY, app.posZ,
                                                    app.thetaX, app.thetaY, app.thetaZ,
                            app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        else:
            tempPrism1 = RectPrism( (50, 0, i*250-50), (150, 100, i*250+100), app.posX, app.posY, app.posZ,
                                                    app.thetaX, app.thetaY, app.thetaZ,
                            app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        tempPrism1.dz = 1
        app.components.append(tempPrism1)



def level6(app):
    
    for i in range(6):
        tempPrism1 = RectPrism( (-300, 0, i*200+50), (-150, 100, i*200+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tempPrism1.dx = 3
        app.components.append(tempPrism1)


def level7(app):
    for i in range(5):
        if (i % 2 == 0):
            tempPrism1 = RectPrism( (-175, 0, i*250+25), (-25, 100, i*250+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            tempPrism1.dx = -2
        else:
            tempPrism1 = RectPrism( (25, 0, i*250+25), (175, 100, i*250+150), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            tempPrism1.dx = 2
            
        app.components.append(tempPrism1)


def level8(app):
    pass


def level9(app):
    pass


def level10(app):
    pass
     
     
     
     
     
     
     
     
       
def level66(app):
    for i in range(6):
        tempPrism1 = RectPrism( (-200, 0, i*200+50), (-100, 100, i*200+125), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tempPrism2 = RectPrism( (100, 0, i*200+50), (200, 100, i*200+125), app.posX, app.posY, app.posZ,
                                                app.thetaX, app.thetaY, app.thetaZ,
                        app.aspectRatio, app.fov, app.nearBound, app.farBound, convertHex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        app.components.extend([tempPrism1, tempPrism2])