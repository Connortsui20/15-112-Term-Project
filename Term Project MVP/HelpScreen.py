


def HelpMode_keyPressed(app, event):
    if (event.key == "p"):
        app.mode = "GameMode"



def HelpMode_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="#8B0000")
    
    canvas.create_text(app.width//2, app.height//4, fill="white",
                        text="Goal: Get to the other side", font="Arial 40")
    
    canvas.create_text(app.width//2, app.height//2-(app.height//10), fill="white",
                        text="WASD for movement", font="Arial 20")
    canvas.create_text(app.width//2, app.height//2, fill="white",
                        text="Arrow keys to look around", font="Arial 20")
    canvas.create_text(app.width//2, app.height//2+(app.height//10), fill="white",
                        text="Space to jump, tab to crouch", font="Arial 20")
    


