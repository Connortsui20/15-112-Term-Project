import pygame as pg


def initApp(self):
        
        #* Display Settings
        self.aspect = self.width/self.height
        self.nearBound = 0.1
        self.farBound = 50
        self.background = (0, 0, 0) #rgb background normalized 0-1
        pg.display.set_mode((self.width, self.height), pg.OPENGL | pg.DOUBLEBUF)
        
        #* Mouse Settings
        pg.mouse.set_pos((self.width//2, self.height//2))
        pg.mouse.set_visible(False)
        
        #* Framerate Settings
        self.lastSecond = 0
        self.previousTime = 0
        self.currentTime = 0
        self.frames = 0
        self.frameTime = 0
        self.frameRate = 0
    
        #* Portals
        self.bluePortal = None
        self.orangePortal = None
    
        #* Adjustable Settings
        self.mouseSensitivity = 1/20
        
        
        