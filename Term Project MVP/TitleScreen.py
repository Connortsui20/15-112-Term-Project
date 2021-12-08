from Graphics.cmu_112_graphics import *
from GameFunctions.initGame import *

from HelpScreen import *


def TitleScreen_mousePressed(app, event):
    if (not app.settingsSet):
        app.fov = int(app.getUserInput("What is the FOV of hell? (rec. 100, int between 45 and 150)"))
        app.fps = int(app.getUserInput("What is the speed of hell? (rec. 90, int between 30 and 150, smaller is faster)"))
        app.gravitySet = float(app.getUserInput("What is the gravity of hell? (rec. 9.81, float between 5 and 15)"))
        app.translationScaleSet = int(app.getUserInput("How fast do you move in hell? (rec. 500, int between 300 and 800)"))
        app.jumpSpeedSet = int(app.getUserInput("What is your jump strength in hell? (rec. 1800, int between 1000 and 3000)"))
        app.lives = int(app.getUserInput("How many lives do you get? (If you choose anything higher than 3 you are weak)"))
    app.settingsSet = True
    


def defaultSettings(app):
    app.fov = 100
    app.fps = 90
    app.gravitySet = 9.81
    app.translationScaleSet = 500
    app.jumpSpeedSet = 1800
    app.lives = 3
    app.settingsSet = True
    
    

def TitleScreen_keyPressed(app, event):
    if (event.key == "g"):
        defaultSettings(app)
    if (event.key == "Enter"):
        if (app.fov and app.fps and app.gravitySet and app.translationScaleSet and app.jumpSpeedSet and app.lives):
            app.mode = "GameMode"
            initGame(app) # add arguments
    if (event.key == "p"):
        app.mode = "HelpMode"



def TitleScreen_redrawAll(app, canvas):
    if (not app.settingsSet):
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#8B0000")
        canvas.create_text(app.width//2, app.height//2,
                        text="WELCOME TO HELL", font="Arial 40")
        canvas.create_text(app.width//2, app.height//2+app.height//4,
                        text="click anywhere to determine hell's settings", font="Arial 20")
        canvas.create_text(app.width//2, app.height//2+(app.height//3),
                        text="(or press g to use default settings)", font="Arial 20")
    else:
        canvas.create_rectangle(0, 0, app.width, app.height, fill="#F7342B")
        canvas.create_text(app.width//2, app.height//2,
                        text="THIS IS HELL", font="Arial 40")
        canvas.create_text(app.width//2, app.height//2+app.height//4,
                        text="PRESS ENTER WHEN YOU ARE READY", font="Arial 20")
    canvas.create_text(app.width-app.width//20, app.height//20, text=f"Press P for help", fill="white")