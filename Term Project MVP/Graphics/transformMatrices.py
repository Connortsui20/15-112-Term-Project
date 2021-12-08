import math
import numpy as np

# from printNdList import *


#* Translates a single point
def translationMatrix(point, transX, transY, transZ):
    translationMatrix =  np.array(( [1, 0, 0, transX],
                                    [0, 1, 0, transY],
                                    [0, 0, 1, transZ],
                                    [0, 0, 0, 1], ))
    translatedPoint = np.matmul(translationMatrix, point)
    
    return translatedPoint



#* Rotates a single point
def rotationMatrix(point, thetaX, thetaY, thetaZ):
    #Rotate points around x axis
    rotationMatrixX = np.array(( [               1,                 0,                 0, 0],
                                 [               0,  math.cos(thetaX), -math.sin(thetaX), 0],
                                 [               0,  math.sin(thetaX),  math.cos(thetaX), 0],
                                 [               0,                 0,                 0, 1], ))
    #Rotate points around y axis
    rotationMatrixY = np.array(( [math.cos(thetaY),                 0, -math.sin(thetaY), 0],
                                 [               0,                 1,                 0, 0],
                                 [math.sin(thetaY),                0,   math.cos(thetaY), 0],
                                 [               0,                 0,                 0, 1], ))
    #Rotate points around z axis
    rotationMatrixZ = np.array(( [math.cos(thetaZ), -math.sin(thetaZ),                 0, 0],
                                 [math.sin(thetaZ),  math.cos(thetaZ),                 0, 0],
                                 [               0,                 0,                 1, 0],
                                 [               0,                 0,                 0, 1], ))
    rotatedPoint = np.matmul(rotationMatrixZ, point) #apply x rotation
    rotatedPoint = np.matmul(rotationMatrixY, rotatedPoint) #apply y rotation
    rotatedPoint = np.matmul(rotationMatrixX, rotatedPoint) #apply z rotation
    
    return rotatedPoint
    
    

#* Projects the 3 points of a triangle, return a projected triangle list
def perspectiveTransform(triangle, aspectRatio, fov, nearBound, farBound): #projects every shape
    fov = math.radians(fov)
    perspectiveMatrix = np.array(( [ 1/(math.tan(fov/2)*aspectRatio), 0, 0, 0 ],
                                   [ 0, 1/(math.tan(fov/2)),             0, 0 ],
                                   [ 0, 0, farBound/(farBound-nearBound), -(farBound*nearBound)/(farBound-nearBound) ],
                                   [ 0, 0, 1,                               0 ],
                                ))
    
    projectedTriangle = []
    for point in triangle:
        projectedPoint = np.matmul(perspectiveMatrix, point)
        projectedTriangle.append(projectedPoint)

    return np.array(projectedTriangle)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
Main Original Version
def perspectiveMatrix(shapes, aspectRatio, fov, nearBound, farBound, radiusBound): #projects every shape
    fov = math.radians(fov)
    perspectiveMatrix = [ [ 1/(math.tan(fov/2)*aspectRatio), 0, 0, 0 ],
                          [ 0, 1/(math.tan(fov/2)), 0, 0 ],
                          [ 0, 0, farBound/(farBound-nearBound), -(farBound*nearBound)/(farBound-nearBound) ],
                          [ 0, 0, 1, 0 ],
                        ]
    allProjectedShapes = []
    for shape in shapes:
        projectedPoints = []
        for point in shape:
            projectedPoint = np.matmul(perspectiveMatrix, point)
            w = projectedPoint[3]
            if ((projectedPoint[0] >= -(1+radiusBound)*w) and (projectedPoint[0] <= (1+radiusBound)*w) and
                (projectedPoint[1] >= -(1+radiusBound)*w) and (projectedPoint[1] <= (1+radiusBound)*w) and
                (projectedPoint[2] >= 0) and (projectedPoint[2] <= (1+radiusBound)*w) ):
                for dimension in range(len(projectedPoint)): #perspective divide here
                    projectedPoint[dimension] /= projectedPoint[3] #* divide each dimension by w (4th coord) for homogenous coordinates
                projectedPoints.append(projectedPoint)
        allProjectedShapes.append(projectedPoints)
    return (allProjectedShapes)
    
'''
    
 
'''
Testing Version:
def perspectiveMatrix(shapes, aspectRatio, fov, nearBound, farBound, radiusBound): #projects every shape
    fov = math.radians(fov)
    perspectiveMatrix = [ [ 1/(math.tan(fov/2)*aspectRatio), 0, 0, 0 ],
                          [ 0, 1/(math.tan(fov/2)), 0, 0 ],
                          [ 0, 0, farBound/(farBound-nearBound), -(farBound*nearBound)/(farBound-nearBound) ],
                          [ 0, 0, 1, 0 ],
                        ]
    allProjectedShapes = []
    for shape in shapes:
        projectedPoints = []
        for point in shape:
            projectedPoint = np.matmul(perspectiveMatrix, point)
            w = projectedPoint[3]
            # if ((projectedPoint[0] >= -(1+radiusBound)*w) and (projectedPoint[0] <= (1+radiusBound)*w) and
            #     (projectedPoint[1] >= -(1+radiusBound)*w) and (projectedPoint[1] <= (1+radiusBound)*w) and
            if ( (projectedPoint[2] >= 0) and (projectedPoint[2] <= (1+radiusBound)*w) ):
                for dimension in range(len(projectedPoint)): #perspective divide here
                    projectedPoint[dimension] /= projectedPoint[3] #* divide each dimension by w (4th coord) for homogenous coordinates
                    projectedPoints.append(projectedPoint)
        allProjectedShapes.append(projectedPoints)
    return (allProjectedShapes)


'''




    
'''
THIS IS THE VERY OLD ORIGNIAL WORKING FUNCTION, TESTING FOR NOW
def perspectiveMatrix(shapes, aspectRatio, fov, nearBound, farBound): #projects every shape
    fov = math.radians(fov)
    perspectiveMatrix = [ [ 1/(math.tan(fov/2)*aspectRatio), 0, 0, 0 ],
                          [ 0, 1/(math.tan(fov/2)), 0, 0 ],
                          [ 0, 0, farBound/(farBound-nearBound), -(farBound*nearBound)/(farBound-nearBound) ],
                          [ 0, 0, 1, 0 ],
                        ]
    allProjectedShapes = []
    for shape in shapes:
        projectedPoints = []
        for point in shape:
            projectedPoint = np.matmul(perspectiveMatrix, point)
            for dimension in range(len(projectedPoint)): #perspective divide here
                projectedPoint[dimension] /= projectedPoint[3] #* divide each dimension by w (4th coord) for homogenous coordinates
            if ((projectedPoint[2] >= 0) and (projectedPoint[2] <= 1)):
                projectedPoints.append(projectedPoint)
        allProjectedShapes.append(projectedPoints)
    return allProjectedShapes
'''






