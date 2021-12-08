import math
import numpy as np

# from printNdList import *


#! Should return a numpy array of 0-2 triangles
#* projectedPoints should be a list of 3 points, each point has 4 dimensions
def frustumCullTriangleZ(projectedPoints):
    point0 = projectedPoints[0] #each points has 4 dimensions
    point1 = projectedPoints[1]
    point2 = projectedPoints[2]
    if (not pointsInView(point0, point1, point2)): #entire triangle is not in view
        return np.array([])
    else: #at least one point is not in view
        #! WILL ONLY CLIP AGAINST THE NEAR PLANE FOR NOW
        if (point0[2] < 0):
            if (point1[2] < 0): #point2 is in view
                return clipTriangle2z(point0, point1, point2)
            elif (point2[2] < 0): #point1 is in view
                return clipTriangle2z(point0, point2, point1)
            else: #point1 and point2 are in view
                return clipTriangle1z(point0, point1, point2)
        elif (point1[2] < 0):
            if (point2[2] < 0): #point0 is in view
                return clipTriangle2z(point1, point2, point0)
            else: #point0 and point2 are in view
                return clipTriangle1z(point1, point0, point2)
        elif (point2[2] < 0): #point0 and point1 are in view
            return clipTriangle1z(point2, point0, point1)
        else:
            return [projectedPoints]
     


#* Check if all points are within view, if not
def pointsInView(point0, point1, point2):
    if ( (point0[0] < -point0[3]) and #test x against x = -1
         (point1[0] < -point1[3]) and
         (point2[0] < -point2[3]) ):
        return False
    if ( (point0[0] > point0[3]) and #test x against x = 1
         (point1[0] > point1[3]) and
         (point2[0] > point2[3]) ):
        return False
    if ( (point0[1] < -point0[3]) and #test y against y = -1
         (point1[1] < -point1[3]) and
         (point2[1] < -point2[3]) ):
        return False
    if ( (point0[1] > point0[3]) and #test y against y = 1
         (point1[1] > point1[3]) and
         (point2[1] > point2[3]) ):
        return False
    if ( (point0[2] < -point0[3]) and #test z against z = -1
         (point1[2] < -point1[3]) and
         (point2[2] < -point2[3]) ):
        return False
    if ( (point0[2] > point0[3]) and #test z against z = 1
         (point1[2] > point1[3]) and
         (point2[2] > point2[3]) ):
        return False
    #* If all tests pass, then at least some part of the triangle is in view
    return True



#* Creates 2 new triangles
def clipTriangle1z(point0, point1, point2): #! Assume point0 is on the wrong side of the plane
    zNearPlane = np.array([0, 0, 1, 0])
    interpolated1 = interpolate3d(point0, point1, zNearPlane)
    interpolated2 = interpolate3d(point0, point2, zNearPlane)
    if (interpolated1 != [] and interpolated2 != []):
        triangle1 = np.array([interpolated1, point1, interpolated2])
        triangle2 = np.array([point1, point2, interpolated2])
        return np.array([triangle1, triangle2])
    else: #to stop drawing an infinitely large triangle on top of the near plane
        return np.array([])
    


#* Creates 1 new triangle
def clipTriangle2z(point0, point1, point2): #! Assume both v0 and v1 are on the wrong side of the plane
    zNearPlane = np.array([0, 0, 1, 0])
    interpolated0 = interpolate3d(point0, point2, zNearPlane)
    interpolated1 = interpolate3d(point1, point2, zNearPlane)
    if (interpolated0 != [] and interpolated1 != []):
        triangle = np.array([interpolated0, interpolated1, point2])
        return np.array([triangle])
    else:
        return np.array([])



#! INTERPOLATION STILL SLIGHTLY WRONG, BUT BETTER
#* Interpolated between 2 points and a plane
def interpolate3d(point0, point1, plane):
    dot0 = np.dot(point0, plane)
    dot1 = np.dot(point1, plane)
    if (math.isclose(dot0, dot1)): #* DO NOT want a division by 0
        return []
    normalized = (dot0) / (dot0-dot1)
    final = point0*(1-normalized) + point1*normalized
    return final
    

'''
Clipping planes for interpolation:
xLeft = np.array([1, 0, 0, 0]) #? what is w coordinate??
xRight = np.array([-1, 0, 0, 0])
yTop = np.array([0, 1, 0, 0])
yBottom = np.array([0, -1, 0, 0])
zNear = np.array([0, 0, 1, 0])
zFar = np.array([0, 0, -1, 0])
'''

# triangle1 = np.array([[-12.06285143, -10.7225346,   15.91591592,  16.,        ],
#                       [ 12.06285143,  10.7225346,   15.91591592,  16.,        ],
#                       [-12.06285143,  10.7225346,   15.91591592,  16.,        ],])

# triangle2 = np.array([[-22.74620296, -10.7225346,   -0.76101505,  -0.66025404,],
#                       [-10.68335153,  10.7225346,   16.57683087,  16.66025404,],
#                       [-22.74620296,  10.7225346,   -0.76101505,  -0.66025404,],])

# triangle3 = np.array([[-22.74620296, -10.7225346,   -0.76101505,  -0.66025404],
#                       [-10.68335153, -10.7225346,   16.57683087,  16.66025404],
#                       [-10.68335153,  10.7225346,   16.57683087,  16.66025404],])



# print(frustumCullTriangle(triangle3))