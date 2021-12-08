'''
All credit goes to GetIntoGameDev and his PyOpenGl tutorials: https://www.youtube.com/playlist?list=PLn3eTxaOtL2PDnEVNwOgZFm5xYPr4dUoR
His github: https://github.com/amengede/getIntoGameDev/tree/main/pyopengl

I follow his version of the engine and the App class wrapper, and all the code surrounding texture and shading is his.
Everything else and all comments are my own code. If there is a #? then that is definitely his code

All images were initially taken by me within the game Portal by Valve, available on Steam. I created the specular maps myself.
'''

import pathlib
import pygame as pg
import numpy as np

from OpenGL.GL import *

from Functions.initApp import *
from Functions.initOpenGL import *
from Functions.loadWorld import *
from Functions.eventHandler import *
from Functions.checkNearPortal import *

from Classes.PortalClass import *

#! Going through portals on floor (and I assume ceiling) does not work properly, but you can exit them
class App:
    
    def __init__(self):
        np.set_printoptions(precision=3)
        
        pg.init()
        
        # self.width = 600
        # self.height = 400
        # self.width = 960
        # self.height = 540
        self.width = 1920
        self.height = 1080
        
        self.path = str(pathlib.Path(__file__).parent.resolve()) + "/"
        
        initApp(self)
        initOpenGL(self)
        loadWorld(self)

        playerHeight = 3 #TODO figure out proper variables later
        movement = 10
        worldCollisions = (self.minWorldX, self.maxWorldX, self.minWorldY, self.maxWorldY)
        self.player = Player([0, 0, playerHeight], playerHeight, movement, worldCollisions)
        self.mainLoop()
    
    
    def mainLoop(self):
        
        running = True
        while (running):
            
            self.getFrameRate() # timing
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #refresh screen
            
            #* Events
            for event in pg.event.get():
                if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                    running = False
                if (event.type == pg.KEYDOWN and event.key == pg.K_LCTRL):
                    self.player.crouchPlayer()
                if (event.type == pg.KEYUP and event.key == pg.K_LCTRL):
                    self.player.unCrouchPlayer()
                if (event.type == pg.KEYDOWN and event.key == pg.K_SPACE):
                    self.player.jumpPlayer()
                if (event.type == pg.KEYDOWN and event.key == pg.K_l):
                    self.bluePortal = None
                    self.orangePortal = None
                
                if (event.type == pg.MOUSEBUTTONDOWN and event.button == 1): #left click
                    createPortal(self, "blue")
                if (event.type == pg.MOUSEBUTTONDOWN and event.button == 3): #right click
                    createPortal(self, "orange")
            
            handleCameraLook(self) # mouse look
            keys = pg.key.get_pressed()
            handleMovement(self, keys, self.dt) # wasd
            
            #* Update and draw components
            for worldComponent in self.worldComponents:
                worldComponent.update()
                worldComponent.draw()
            
            for component in self.components:
                component.update()
                component.draw()
            
            for light in self.lights:
                light.update()
                light.draw()
            
            if (self.bluePortal):
                self.bluePortal.update()
                self.bluePortal.draw()
            if (self.orangePortal):
                self.orangePortal.update()
                self.orangePortal.draw()
            
            if (self.bluePortal != None): #remove wall collisions if near portal
                self.player.nearBluePortal = checkNearPortal(self.player, self.bluePortal)
            if (self.orangePortal != None):
                self.player.nearOrangePortal = checkNearPortal(self.player, self.orangePortal)
                    
            self.player.update([self.shaderBasic, self.shader], self.bluePortal, self.orangePortal, self.dt)
        
            pg.display.flip()

        pg.quit()
        
    
    #* Framerate
    def getFrameRate(self): #also gets frame time for physics
        self.currentTime = pg.time.get_ticks()
        deltaTimeSecond = self.currentTime - self.lastSecond
        self.dt = (self.currentTime - self.previousTime)/1000
        if (deltaTimeSecond >= 1000): #every second
            pg.display.set_caption(f"Running at {self.frames} fps.")
            self.lastSecond = self.currentTime #reset seconds
            self.frames = 0 #reset frame count
        self.previousTime = self.currentTime
        self.frames += 1

    
myApp = App()


