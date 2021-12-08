
#* Draw one triangle
def drawTriangle(app, canvas, triangle):
    trianglePoints = []
    for point in triangle.triangle:
        coord = []
        coord.append(int((point[0]+1)*app.width/2))
        coord.append(int((1-point[1])*app.height/2))
        trianglePoints.append(coord)
    #canvas.create_polygon(trianglePoints, fill=f"{fill}", outline="black", width=1)
    canvas.create_polygon(trianglePoints, fill=triangle.color, outline="black", width=1)

