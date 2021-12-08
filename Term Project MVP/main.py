from GameEngine import *
from GameFunctions.initGame import *

from TitleScreen import *


def appStarted(app):
    
    app.mode = "TitleScreen"
    app.fov = None
    app.fps = None
    app.gravitySet = None
    app.jumpSpeedSet = None
    app.translationScaleSet = None
    app.settingsSet = False
    
    app.cheats = False #dont do it, im watching
  

'''
Different 16/9 ratios, but you can set it to whatever you want:
640x360
960x540
1200x675
1280x720
1600x900
1920x1080
'''
    
#runApp(width=960, height=540)
runApp(width=1600, height=900)





