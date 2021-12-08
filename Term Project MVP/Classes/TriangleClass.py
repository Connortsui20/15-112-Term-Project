import numpy as np

from Graphics.transformMatrices import *
from Graphics.frustumCull import *
#from printNdList import *

from Classes.NDCTriangleClass import *

#TODO find new color value given a point light (directonal for now)

class Triangle:
    def __init__(self, point0, point1, point2,
                 cameraTransX, cameraTransY, cameraTransZ,
                 cameraThetaX, cameraThetaY, cameraThetaZ,
                 aspectRatio, fov, nearBound, farBound, color):
        
        np.set_printoptions(suppress=True) #* only for readability in debugging
        
        #* World coordinates are tuples, immutable
        self.worldPoints = np.array((point0, point1, point2))
        self.getNormal()
        # self.points is a np array of the 3 homogenous coordinate points
        self.points = np.array((self.worldToHomog(self.worldPoints[0]),
                                self.worldToHomog(self.worldPoints[1]),
                                self.worldToHomog(self.worldPoints[2]) ))
        
        #* Triangle Properties
        self.doesNotExist = False
        self.contains2Triangles = False
        self.color = color
        self.shadedColor = self.color #! CHANGE LATER
        self.updateNeeded = False

        #* Project the triangle into clip space
        self.projectTriangle(cameraTransX, cameraTransY, cameraTransZ, cameraThetaX, cameraThetaY, cameraThetaZ,
                             aspectRatio, fov, nearBound, farBound)

        
    def __repr__(self):
        #return (f"Triangle: Point 0 = {self.worldPoints[0]}, Point 1 = {self.worldPoints[1]}, Point 2 = {self.worldPoints[2]}")
        #return (f"Triagnle: Point 0 = {self.homogPoint0}, Point 1 = {self.homogPoint1}, Point 2 = {self.homogPoint2}")
        return (f"Triangle: Point 0 = {self.points[0]}; Point 1 = {self.points[1]}; Point 2 = {self.points[2]}\n")
        #return (f"Triangle: Point 0 = {np.array((np.round(x, 2) for x in self.NDCPoints[0][:-1]))}; Point 1 = {np.array((np.round(x, 2) for x in self.NDCPoints[1][:-1]))}; Point 2 = {np.array((np.round(x, 2) for x in self.NDCPoints[2][:-1]))}\n")
        #! ^ something wrong with this line
    
    
    #* Find normal vector of the triangle
    def getNormal(self):
        vector1 = np.subtract(self.worldPoints[1], self.worldPoints[0])
        vector2 = np.subtract(self.worldPoints[2], self.worldPoints[0])
        crossProduct = np.cross(vector1, vector2)
        self.normal = crossProduct
        
        
    def getCorrectedColor(self):
        baseColor = self.color
    
    
    # #* returns the centroid of the triangle
    # def getMidpoint(self):
    #     point0 = self.culledTriangles[0]
    #     point1 = self.culledTriangles[1]
    #     point2 = self.culledTriangles[2]
    #     averageX = np.average([point0[0], point1[0], point2[0]])
    #     averageY = np.average([point0[1], point1[1], point2[1]])
    #     averageZ = np.average([point0[2], point1[2], point2[2]])
    #     return np.array((averageX, averageY, averageZ))
    
    
    #* Add the w coordinate; Homogeneous coordinates are np arrays (mutable)
    def worldToHomog(self, point):
        return (np.array((point[0], point[1], point[2], 1.0)))
    
    
    #* Move world points of triangle
    def translateTriangle(self, transX, transY, transZ):
        
        translatedWorldPoints = []
        for point in self.worldPoints:
            point = np.add(point, np.array((transX, transY, transZ)))
            translatedWorldPoints.append(point)
        self.worldPoints = np.array(translatedWorldPoints)
        self.getNormal() #have to find new normal #? Do I even need to do this?
        
        translatedPoints = []
        for point in self.points:
            point = translationMatrix(point, transX, transY, transZ)
            translatedPoints.append(point)
        self.points = np.array(translatedPoints)
       
        
    #* Rotates the world points of the triangle
    def rotateTriangle(self, thetaX, thetaY, thetaZ):
        rotatedPoints = []
        for point in self.points:
            point = rotationMatrix(point, thetaX, thetaY, thetaZ)
            rotatedPoints.append(point)
        self.points = np.array(rotatedPoints)


    #* Project triangle into clip space, then clip, then cull, then return the list of triangles in NDC Points
    def projectTriangle(self, cameraTransX, cameraTransY, cameraTransZ, cameraThetaX, cameraThetaY, cameraThetaZ,
                        aspectRatio, fov, nearBound, farBound):
        
        transformedPoints = []
        for point in self.points:
            translatedPoint = translationMatrix(point, cameraTransX, cameraTransY, cameraTransZ)
            rotatedPoint = rotationMatrix(translatedPoint, cameraThetaX, cameraThetaY, cameraThetaZ)
            transformedPoints.append(rotatedPoint)
        
        #* Projected Points are clip coordinates BEFORE the perspective divide, should have 3 lists
        self.projectedPoints = perspectiveTransform(transformedPoints, aspectRatio, fov, #before perspective divide
                                                    nearBound, farBound) #! THESE ARE THE CLIP COORDINATES
        
        self.frustumCull() #* creates self.culledTriangles
        
        self.NDCPoints = []
        for triangle in self.culledTriangles: #* Perspective divide for NDC and remove w coordinates
            newNDCTriangle = NDCTriangle(triangle, self.normal, self.shadedColor)
            self.NDCPoints.append( newNDCTriangle )
        

    #* Clip and cull the triangle
    def frustumCull(self): #needs no other arguments other than self.projectedPoints
        #* culledTriangles is a list of triangles in homogenous coordinates
        self.culledTriangles = frustumCullTriangleZ(self.projectedPoints)
        










