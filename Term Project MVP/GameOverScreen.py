from Graphics.cmu_112_graphics import *


def GameOver_redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
    canvas.create_text(app.width//2, app.height//2, text="Game Over You Are Bad", fill="red", font="Arial 50")
    canvas.create_text(app.width//2, app.height//2+app.height//6,
                       text="just quit now don't bother trying again", fill="red", font="Arial 30")