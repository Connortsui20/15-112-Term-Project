
def checkNearPortal(player, portal):
    if (portal.normal[0] != 0):
        portalWidthX = player.thickness*3 #honestly idk why 3 instead of 2 it just works
        portalWidthY = portal.width
    elif (portal.normal[1] != 0):
        portalWidthX = portal.width
        portalWidthY = player.thickness*3
    elif (portal.normal[2] != 0):
        portalWidthX = portal.width*player.thickness
        portalWidthY = portal.height*player.thickness
   
    playerThickness = player.thickness
    
    playerHeight = player.playerHeight
    portalHeight = portal.height
    
    playerX = player.position[0]
    portalX = portal.position[0]
    playerY = player.position[1]
    portalY = portal.position[1]
    playerZ = player.position[2]
    portalZ = portal.position[2]
    
    if ( #* + portalHeight/8 for extra leeway
        ( ( ((playerX + playerThickness) <= (portalX + portalWidthX/2 + portalHeight/8)) and
            ((playerX - playerThickness) >= (portalX - portalWidthX/2 - portalHeight/8)) )
        and
          ( ((playerY + playerThickness) <= (portalY + portalWidthY/2 + portalHeight/8)) and
            ((playerY - playerThickness) >= (portalY - portalWidthY/2 - portalHeight/8)) )
        and
          ( ((playerZ + 0) <= (portalZ + portalHeight/2 + portalHeight/8)) and
            ((playerZ - playerHeight) >= (portalZ - portalHeight/2 - portalHeight/8)) ) )
        ):
        return True
    else:
        return False

    