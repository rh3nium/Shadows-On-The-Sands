#### Transforms ####

# sprite_highlight with animation
transform sprite_highlight(sprite_name):
    zoom 1.0  # Starting scale
    linear 0.09 zoom 1.02  # Zoom in to scale x over y seconds

# sprite_zoomout with animation
transform sprite_zoomout(sprite_name):
    zoom 1.02
    linear 0.09 zoom 1.0

# move to center
transform movecenter:
    linear 0.4 xpos 576

# 2 sprites on screen
transform left2:
    xpos 384
    ypos -50

transform moveleft2:
    linear 0.4 xpos 384

transform right2:
    xpos 768
    ypos -50

transform moveright2:
    linear 0.4 xpos 768

# 3 sprites on screen
transform left3:
    xpos 288
    ypos -50

transform moveleft3:
    linear 0.4 xpos 288

transform right3:
    xpos 864
    ypos -50

transform moveright3:
    linear 0.4 xpos 864

# 4 sprites on screen
transform leftmost4:
    xpos 144
    ypos -50

transform moveleftmost4:
    linear 0.4 xpos 144

transform center_left4:
    xpos 432
    ypos -50

transform movecenter_left4:
    linear 0.4 xpos 432

transform center_right4:
    xpos 720
    ypos -50

transform movecenter_right4:
    linear 0.4 xpos 720

transform rightmost4:
    xpos 1006
    ypos -50

transform moverightmost4:
    linear 0.4 xpos 1006

# 5 sprites on screen
transform leftmost5:
    xpos 128
    ypos -50

transform moveleftmost5:
    linear 0.4 xpos 128

transform center_left5:
    xpos 384
    ypos -50

transform movecenter_left5:
    linear 0.4 xpos 384

transform center_right5:
    xpos 768
    ypos -50

transform movecenter_right5:
    linear 0.4 xpos 768

transform rightmost5:
    xpos 1024
    ypos -50

transform moverightmost5:
    linear 0.4 xpos 1024

# sprite creepy_closeup
transform creepy_closeup(sprite_name):
    anchor (0.5, 0.5)  # Set the anchor point to the center of the sprite
    linear 0.09 zoom 2

# sprite_zoomout_tiny
transform sprite_zoomout_tiny(sprite_name):
    zoom 1.0
    linear 1.0 zoom 0.4
