from pygame import *
from time import time as timer
clock = time.Clock()
window = display.set_mode((1000, 700))
display.set_caption('ping-pong')
background = transform.scale(image.load('fon.png'), (1000, 700))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 605:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 605:
            self.rect.y += self.speed
        
ball = GameSprite('pinpong.png',400, 400, 70, 70,10)
roketka1 = Player('rok.png',5,400,40,200,10)
roketka2 = Player('rok.png',960,400,40,200,10)


GAME = True

while GAME:
    for e in event.get():
        if e.type == QUIT:
            GAME = False
    window.blit(background, (0, 0))
    roketka1.reset()
    roketka1.update()
    roketka2.reset()
    roketka2.update()
    ball.reset()
    ball.update()
    
    display.update()
    clock.tick(60)
