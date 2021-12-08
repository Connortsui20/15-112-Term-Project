import pygame as pg

#* Mouse Presses
def handleCameraLook(self):
    x, y = pg.mouse.get_pos()
    dThetaX = self.mouseSensitivity * (self.width//2 - x)
    dThetaY = self.mouseSensitivity * (self.height//2 - y)
    self.player.rotateCamera(dThetaX, dThetaY)
    pg.mouse.set_pos((self.width//2, self.height//2))
    

#* Key Presses
def handleMovement(self, keys, dt):
    if keys[pg.K_w]:
        self.player.movePlayer("forward", dt)
    if keys[pg.K_a]:
        self.player.movePlayer("right", dt)
    if keys[pg.K_s]:
        self.player.movePlayer("backward", dt)
    if keys[pg.K_d]:
        self.player.movePlayer("left", dt)
    
    