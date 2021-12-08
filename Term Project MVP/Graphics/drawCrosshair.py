



from tkinter.constants import W


def drawCrosshair(app, canvas):
    centerX = app.width//2
    centerY = app.height//2
    radius = 3
    color = "#ffff00"
    #dotCrosshair(canvas, centerX, centerY, radius, color)
    
    #better to have even numbers here
    distance = 4
    length = 8
    thickness = 4
    stroke = 1
    
    defaultCrosshair(canvas, centerX, centerY,
                     distance, length, thickness, color, stroke)

def dotCrosshair(canvas, centerX, centerY, radius, color):
    canvas.create_oval(centerX-radius, centerY-radius,
                       centerX+radius, centerY+radius,
                       fill=color, outline="black")
    
    

def defaultCrosshair(canvas, centerX, centerY,
                     distance, length, thickness, color, width):
    
    canvas.create_rectangle(centerX+distance, centerY-thickness//2,
                            centerX+distance+length, centerY+thickness//2,
                            fill=color, outline="black", width=width)
    
    canvas.create_rectangle(centerX-distance, centerY-thickness//2,
                            centerX-distance-length, centerY+thickness//2,
                            fill=color, outline="black", width=width)
    
    canvas.create_rectangle(centerX-thickness//2, centerY-distance,
                            centerX+thickness//2, centerY-distance-length,
                            fill=color, outline="black", width=width)
    
    canvas.create_rectangle(centerX-thickness//2, centerY+distance,
                            centerX+thickness//2, centerY+distance+length,
                            fill=color, outline="black", width=width)