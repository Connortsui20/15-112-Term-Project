from OpenGL.GL import *
import pygame as pg


#* Not even going to pretend this is my code, I barely understand what's going on here
class Material:
    def __init__(self, filepath, temp):
        if (temp == "png"):
            #* Diffuse Texture
            self.diffuseTexture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.diffuseTexture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) #s coord
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) #t coord
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) #normalized min
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) #normalized max
            image = pg.image.load(f"{filepath}_diffuse.png").convert() #! each file needs to have a _diffuse and a _specular version
            image_width,image_height = image.get_rect().size
            img_data = pg.image.tostring(image,'RGBA')
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data) #If the person who wrote this doesn't understand this then neither do I
            glGenerateMipmap(GL_TEXTURE_2D)
            
            #* Specular Texture
            self.specularTexture = glGenTextures(1) #specular version
            glBindTexture(GL_TEXTURE_2D, self.specularTexture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            image = pg.image.load(f"{filepath}_specular.png").convert()
            image_width,image_height = image.get_rect().size
            img_data = pg.image.tostring(image,'RGBA')
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
            glGenerateMipmap(GL_TEXTURE_2D)
        
        else:
            #* Diffuse Texture
            self.diffuseTexture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.diffuseTexture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT) #s coord
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT) #t coord
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) #normalized min
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR) #normalized max
            image = pg.image.load(f"{filepath}_diffuse.png").convert_alpha() #! each file needs to have a _diffuse and a _specular version
            image_width,image_height = image.get_rect().size
            img_data = pg.image.tostring(image,'RGBA')
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
            glGenerateMipmap(GL_TEXTURE_2D)
            
            #* Specular Texture
            self.specularTexture = glGenTextures(1) #specular version
            glBindTexture(GL_TEXTURE_2D, self.specularTexture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            image = pg.image.load(f"{filepath}_specular.png").convert_alpha()
            image_width,image_height = image.get_rect().size
            img_data = pg.image.tostring(image,'RGBA')
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
            glGenerateMipmap(GL_TEXTURE_2D)


    def use(self): #binds all textures
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.diffuseTexture)
        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, self.specularTexture)
    
    
    def destroy(self): #? I have no idea what the point of this is
        glDeleteTextures(2, (self.diffuseTexture, self.specularTexture))