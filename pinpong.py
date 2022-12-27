from pygame import *
from time import time as timer
clock = time.Clock()
window = display.set_mode((1000, 700))
display.set_caption('ping-pong')
background = transform.scale(image.load('fon.png'), (1000, 700))

GAME = True

while GAME:
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    window.blit(background, (0, 0))
    display.update()
    clock.tick(60)
