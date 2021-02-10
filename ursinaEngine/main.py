from ursina import *


def update():
    if held_keys['w']:
        cam.y += 1 * time.dt
    elif held_keys['a']:
        cam.x -= 1 * time.dt
    elif held_keys['s']:
        cam.y -= 1 * time.dt
    elif held_keys['d']:
        cam.x += 1 * time.dt


app = Ursina()
approLogo_texture = load_texture('textures/approachcircle.bmp')
cam_texture = load_texture('textures/cam.png')
approLogo = Entity(model='quad', scale=(4.8, 0.5), position=(-4.87, -3.838), texture=approLogo_texture)
cam = Entity(model='quad', scale=(7, 7), position=(0, 0), texture=cam_texture)
app.run()
