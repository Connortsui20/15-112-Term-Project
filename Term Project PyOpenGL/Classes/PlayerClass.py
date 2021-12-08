from OpenGL.GL import *

import numpy as np
import pyrr


class Player:
    def __init__(self, position, playerHeight, moveSpeed, worldCollisions):
        
        self.position = np.array(position, dtype=np.float32)
        self.thetaX = 90 #looking towards positive y on spawn
        self.thetaY = 0
        self.thetaZ = 0
        self.forwardVector = np.array([0, 0, 0], dtype=np.float32) #initialize look vector
        self.globalUpVector = np.array([0, 0, 1], dtype=np.float32) #z is up, initialize vector
        self.normalDirection = (1, 0)
        
        self.playerHeight = playerHeight
        self.thickness = 0.5
        self.moveSpeed = moveSpeed
        self.crouchAmount = 1
        self.crouch = False
        
        self.velocity = np.array([0, 0, 0], dtype=np.float32)
        self.jumpSpeed = 30
        self.gravity = 100
        self.goaldx, self.goaldy = 0, 0
        self.userMovePlayer = False
        self.acceleration = 5
        # self.sharpness = 1/10 #How fast speed up
        self.smoothness = 3 #How slow slow down
        
        self.minWorldX, self.maxWorldX = worldCollisions[0], worldCollisions[1]
        self.minWorldY, self.maxWorldY = worldCollisions[2], worldCollisions[3]
        
        self.nearBluePortal = False
        self.nearOrangePortal = False
        self.teleportedRecently = False
        
        
    def movePlayer(self, direction, dt): #TODO Add angle now
        
        self.userMovePlayer = True
        
        if (direction == "forward"):
            lookAngle = 0
        if (direction == "backward"):
            lookAngle = 180
        if (direction == "right"):
            lookAngle = 90
        if (direction == "left"):
            lookAngle = -90

        walkDirection = (lookAngle + self.thetaX) % 360
        
        self.goaldx += (np.cos(np.radians(walkDirection), dtype=np.float32))
        self.goaldy += (np.sin(np.radians(walkDirection), dtype=np.float32))

        self.normalDirection = np.array((self.goaldx, self.goaldy), dtype=np.float32) #normal direction vector
        
        goals = (self.normalDirection * self.moveSpeed) * self.acceleration * dt
        
        self.velocity[0] += goals[0]
        self.velocity[1] += goals[1]
        
        if (np.sqrt(self.velocity[0]**2 + self.velocity[1]**2) >= self.moveSpeed):
            self.velocity[0], self.velocity[1] = self.normalDirection * self.moveSpeed
        
        
    def crouchPlayer(self):
        self.moveSpeed /= 2
        self.jumpSpeed /= 1.5
        self.crouch = True
        
    def unCrouchPlayer(self):
        self.moveSpeed *= 2
        self.jumpSpeed *= 1.5
        self.crouch = False
        
    def jumpPlayer(self):
        if (self.velocity[2] == 0): #only jump if not in midair
            self.velocity[2] = self.jumpSpeed

   
    def rotateCamera(self, dThetaX, dThetaY):
        self.thetaX = (self.thetaX + dThetaX) % 360
        self.thetaY = min(max(self.thetaY + dThetaY, -89.9), 89.9) # when 90 weird things happen with flipping
        

    def update(self, shaders, bluePortal, orangePortal, dt):
        
        self.physics(dt)
        
        collisionsXY = True
        collisionsZ = True
        
        if (self.nearBluePortal is True and orangePortal != None and self.nearOrangePortal is False):
            if (bluePortal.normal[2] == 0):
                collisionsXY = False #redundancy
                collisionsZ = True
            else:
                collisionsXY = True
                collisionsZ = False
            self.teleportFromTo(bluePortal, orangePortal, dt)
    
        if (self.nearOrangePortal is True and bluePortal != None and self.nearBluePortal is False):
            if (orangePortal.normal[2] == 0):
                collisionsXY = False
                collisionsZ = True
            else:
                collisionsXY = True
                collisionsZ = False
            self.teleportFromTo(orangePortal, bluePortal, dt)
            
        if (collisionsXY):
            self.checkCollisionsXY()
        if (collisionsZ):
            self.checkCollisionsZ()
        
        self.goaldx, self.goaldy = 0, 0
        
        self.userMovePlayer = False
        
        originalPosition = self.position[2]
        if (self.crouch):
            self.position[2] -= self.crouchAmount

        self.openGLCamera(shaders)
          
        self.position[2] = originalPosition
        

    #* So I spent 20+ hours on this and for some reason this sort of works, definitely wasn't trial and error haha ...
    def teleportFromTo(self, startPortal, endPortal, dt): #ignore the dt, it should be there but I couldn't figure it out
        #np.set_printoptions(precision=3, suppress=True)
        
        goingThroughFloor = False
        if (startPortal.normal[2] == 0):
            relativePos = self.tryTeleport("wall")
        else:
            relativePos = self.tryTeleport("floor")
            goingThroughFloor = True
        
        if (not relativePos is None):
            rotation = np.degrees(np.radians(startPortal.rotation) - np.radians(-endPortal.rotation)) #may have to mod 360
            
            if (goingThroughFloor): #enter through floor, CANNOT enter a ceiling for now
                
                if (endPortal.normal[0] != 0 and endPortal.normal[1] != 0): #wall, if normal is not 1 then it must be the ceiling, in that case don't rotate at all
                    self.thetaX, self.thetaY = -(self.thetaY + rotation[2]), 0 #idk quaternions and gimbal lock would solve this
                    rotationMatrixZ = pyrr.matrix33.create_from_z_rotation(np.radians(rotation[2]))
                    
                    if (endPortal.normal[0] != 1): # I think this is working now (not really just sort of)
                        rotationMatrixXY = pyrr.matrix33.create_from_x_rotation(np.radians(rotation[1]))
                    else:
                        rotationMatrixXY = pyrr.matrix33.create_from_y_rotation(np.radians(rotation[1]))
                    
                    relativePos = np.matmul(rotationMatrixZ, relativePos)
                    relativePos = np.matmul(rotationMatrixXY, relativePos)
                    self.position = endPortal.position - relativePos
                    self.velocity = np.matmul(rotationMatrixZ, self.velocity)
                    self.velocity = np.matmul(rotationMatrixXY, self.velocity)
                    
                else: #ceiling
                    self.position = endPortal.position - relativePos
            
            else: #going through a wall
                
                if (endPortal.normal[2] == 0): #exit portal is a wall
                    self.thetaX = (self.thetaX + rotation[2]) #look rotation
                    self.goaldx = (np.cos(np.radians(self.thetaX), dtype=np.float32))
                    self.goaldy = (np.sin(np.radians(self.thetaX), dtype=np.float32))
                    self.normalDirection = np.array((self.goaldx, self.goaldy), dtype=np.float32) #normal direction vector
                    rotationMatrixZ = pyrr.matrix33.create_from_z_rotation(np.radians(rotation[2]))
                    relativePos = np.matmul(rotationMatrixZ, relativePos)
                    # relativePos = np.matmul(rotationMatrixXY, relativePos)
                    self.position = endPortal.position - relativePos
                    self.velocity = np.matmul(rotationMatrixZ, self.velocity)
                    # self.velocity = np.matmul(rotationMatrixXY, self.velocity)
                    
                else: #exit portal is either ceiling or floor
                    self.thetaY = (self.thetaY + rotation[1]) #weird things happen with % 360 bc of (-90, 90) limits
                    self.goaldx = (np.cos(np.radians(self.thetaX), dtype=np.float32))
                    self.goaldy = (np.sin(np.radians(self.thetaX), dtype=np.float32))
                    self.normalDirection = np.array((self.goaldx, self.goaldy), dtype=np.float32) #normal direction vector
                    rotationMatrixZ = pyrr.matrix33.create_from_z_rotation(np.radians(rotation[2]))
                    
                    if (endPortal.normal[0] != 1): # I think this is working now (not really just sort of)
                        rotationMatrixXY = pyrr.matrix33.create_from_x_rotation(np.radians(rotation[1]))
                    else:
                        rotationMatrixXY = pyrr.matrix33.create_from_y_rotation(np.radians(rotation[1]))
                    
                    relativePos = np.matmul(rotationMatrixZ, relativePos)
                    relativePos = np.matmul(rotationMatrixXY, relativePos)
                    self.position = endPortal.position - relativePos
                    self.velocity = np.matmul(rotationMatrixZ, self.velocity)
                    self.velocity = np.matmul(rotationMatrixXY, self.velocity)
                    
        self.teleportedRecently = True
        

    def tryTeleport(self, surface): #only works for x and y right now
        if (surface == "wall"):
            relativePos = np.array([0, 0, 0], dtype=np.float32)
            teleport = False
            if (self.position[0] > self.maxWorldX): # Collisions with portal
                distance = self.position[0] - self.maxWorldX
                relativePos[0] += distance
                teleport = True
            if (self.position[0] < self.minWorldX):
                distance = self.position[0] - self.minWorldX
                relativePos[0] += distance
                teleport = True
            if (self.position[1] > self.maxWorldY):
                distance = self.position[1] - self.maxWorldX
                relativePos[1] += distance
                teleport = True
            if (self.position[1] < self.minWorldY):
                distance = self.position[1] - self.minWorldX
                relativePos[1] += distance
                teleport = True
            if (teleport):
                return relativePos
            else: return None
            
        elif (surface == "floor"):
            relativePos = np.array([0, 0, 0], dtype=np.float32)
            teleport = False
            if (self.position[2] > 20):
                distance = self.position[2] - 20
                relativePos[1] += distance
                teleport = True
            if (self.position[2] < self.playerHeight):
                distance = self.position[2] - self.playerHeight
                relativePos[2] += distance
                teleport = True
            if (teleport):
                return relativePos
            else: return None


    def physics(self, dt):
        #* Friction
        if (self.position[2] <= self.playerHeight):
            if (self.velocity[0] < 0):
                self.velocity[0] += self.acceleration * dt * self.smoothness * abs(self.normalDirection[0])
                if (self.velocity[0] >= 0):
                    self.velocity[0] = 0
            elif (self.velocity[0] >= 0):
                self.velocity[0] -= self.acceleration * dt * self.smoothness * abs(self.normalDirection[0])
                if (self.velocity[0] <= 0):
                    self.velocity[0] = 0
                    
            if (self.velocity[1] < 0):
                self.velocity[1] += self.acceleration * dt * self.smoothness * abs(self.normalDirection[1])
                if (self.velocity[1] >= 0):
                    self.velocity[1] = 0
            elif (self.velocity[1] >= 0):
                self.velocity[1] -= self.acceleration * dt * self.smoothness * abs(self.normalDirection[1])
                if (self.velocity[1] <= 0):
                    self.velocity[1] = 0
        
        #* Time increment
        self.velocity[2] += -self.gravity * dt #gravity
        
        self.position[0] += self.velocity[0] * dt
        self.position[1] += self.velocity[1] * dt
        self.position[2] += self.velocity[2] * dt


    def checkCollisionsXY(self):
        if (self.position[0] >= self.maxWorldX - self.thickness): #* Collisions with body
            self.position[0] = self.maxWorldX - self.thickness
        if (self.position[0] <= self.minWorldX + self.thickness):
            self.position[0] = self.minWorldX + self.thickness
            
        if (self.position[1] >= self.maxWorldY - self.thickness):
            self.position[1] = self.maxWorldY - self.thickness
        if (self.position[1] <= self.minWorldY + self.thickness):
            self.position[1] = self.minWorldY + self.thickness
    
    
    def checkCollisionsZ(self):
        if (self.position[2] <= self.playerHeight):
            self.position[2] = self.playerHeight
            self.velocity[2] = 0

    
    def openGLCamera(self, shaders):
        camera_cos = np.cos(np.radians(self.thetaX), dtype=np.float32) #! Not my code, but pretty standard look matrix
        camera_sin = np.sin(np.radians(self.thetaX), dtype=np.float32)
        camera_cos2 = np.cos(np.radians(self.thetaY), dtype=np.float32)
        camera_sin2 = np.sin(np.radians(self.thetaY), dtype=np.float32)
        self.forwardVector[0] = camera_cos * camera_cos2
        self.forwardVector[1] = camera_sin * camera_cos2
        self.forwardVector[2] = camera_sin2
    
        rightVector = np.cross(self.forwardVector, self.globalUpVector) #had to change these bc they were backwards
        upVector = np.cross(rightVector, self.forwardVector)
        lookat_matrix = pyrr.matrix44.create_look_at(self.position, self.position + self.forwardVector, upVector, dtype=np.float32) #built-in I have no idea about the actual math
        
        for shader in shaders: #can have multiple shaders
            glUseProgram(shader)
            glUniformMatrix4fv(glGetUniformLocation(shader, "view"), 1, GL_FALSE, lookat_matrix)
            glUniform3fv(glGetUniformLocation(shader, "cameraPos"), 1, self.position) #! End of not my code
