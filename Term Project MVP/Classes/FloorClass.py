import math

from Classes.TriangleClass import *


class Floor:
    def __init__(self, coord0, coord1, cameraTransX, cameraTransY, cameraTransZ,
                                       cameraThetaX, cameraThetaY, cameraThetaZ,
                                       aspectRatio, fov, nearBound, farBound, color):
        #*Component details
        self.coord0 = coord0
        self.coord1 = coord1
        self.center = np.add((np.subtract(self.coord1, self.coord0))/2, self.coord0)
        # self.radiusBound = math.dist(self.coord1, self.center)
        self.color = color
        
        self.floorMin = self.coord0[1] #Y value 
        
        #*Camera details
        self.cameraTransX = cameraTransX
        self.cameraTransY = cameraTransY
        self.cameraTransZ = cameraTransZ
        self.cameraThetaX = cameraThetaX
        self.cameraThetaY = cameraThetaY
        self.cameraThetaZ = cameraThetaZ
        self.aspectRatio = aspectRatio
        self.fov = fov
        self.nearBound = nearBound
        self.farBound = farBound
        
        #* Create component
        self.allTriangles = self.createFloor()
        self.clipCullTriangles(cameraTransX, cameraTransY, cameraTransZ)
        self.updateNeeded = False
        
    
    # def __repr__(self):
    #     return self.triangles
    
    
    #* Move position of entire component
    def translatePrism(self, transX, transY, transZ):
        for triangle in self.allTriangles: #Translate all triangles
            triangle.translateTriangle(transX, transY, transZ)
        self.updateNeeded = True
        
    
    #* Clips and culls every triangle list (since each triangle is a list of triangles after clipping)
    def clipCullTriangles(self, cameraTransX, cameraTransY, cameraTransZ): #? will have to include angles soon as well maybe?
        self.triangles = self.backfaceCull(self.allTriangles, cameraTransX, cameraTransY, cameraTransZ)
        self.finalTriangles = []
        for triangle in self.triangles: #each triangle in self.triangles is a list
            self.finalTriangles.extend(triangle.NDCPoints)
   
    
    #* backface culls and also elminates things behind the camera
    def backfaceCull(self, unsortedTriangles, cameraTransX, cameraTransY, cameraTransZ): #thetaZ should always be 0
        seenTriangles = []
        for triangle in unsortedTriangles: #! Change to broadcast for clarity here
            cameraToPointVector = np.subtract([-cameraTransX, -cameraTransY, -cameraTransZ], triangle.worldPoints[0])
            dotProduct = np.dot(triangle.normal, cameraToPointVector)
            if ((dotProduct < 0) and (not math.isclose(dotProduct, 0))): #! Something is backwards here...
                seenTriangles.append(triangle)
        return seenTriangles
    
    
    #* Move camera around prism
    def moveAround(self, cameraTransX, cameraTransY, cameraTransZ, cameraThetaX, cameraThetaY, cameraThetaZ,
                        aspectRatio, fov, nearBound, farBound):
        for triangle in self.allTriangles:
            triangle.projectTriangle(cameraTransX, cameraTransY, cameraTransZ, cameraThetaX, cameraThetaY, cameraThetaZ,
                        aspectRatio, fov, nearBound, farBound) #project into clip space
        self.clipCullTriangles(cameraTransX, cameraTransY, cameraTransZ) #clip space to homogenous space
    
    
    #* Create 12 different triangles based off 2 3d coordinates
    def createFloor(self):
        (x0, y0, z0) = self.coord0
        (x1, y1, z1) = self.coord1
        
        if ( (x0 > x1) or (y0 > y1) or (z0 > z1) ):
            raise Exception("First coordinate of createFloor must be less than the second")
        
        # 0 1 4
        triY0a = Triangle( ( x0, y0, z0 ),
                        ( x1, y0, z0 ),
                        ( x0, y0, z1 ),
                        self.cameraTransX, self.cameraTransY, self.cameraTransZ,
                        self.cameraThetaX, self.cameraThetaY, self.cameraThetaZ,
                        self.aspectRatio, self.fov,
                        self.nearBound, self.farBound, self.color)
        # 1 5 4
        triY0b = Triangle( ( x1, y0, z0 ),
                        ( x1, y0, z1 ),
                        ( x0, y0, z1 ),
                        self.cameraTransX, self.cameraTransY, self.cameraTransZ,
                        self.cameraThetaX, self.cameraThetaY, self.cameraThetaZ,
                        self.aspectRatio, self.fov,
                        self.nearBound, self.farBound, self.color)
          
        triangleList = []
        
        triangleList.extend((triY0a, triY0b, ))
        
        #triangleList.append(triY0a)
        #triangleList.append(triY0b)
        
        return triangleList