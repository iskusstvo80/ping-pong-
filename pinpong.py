from pygame import *
from time import time as timer

window = display.set_mode((1000, 700))
display.set_caption('Shooter')
background = transform.scale(image.load('back.jpg'), (1000, 700))

clock = time.Clock()


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
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 605:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 605:
            self.rect.y += self.speed

speed_x = 3
speed_y = 3
racket1 = Player('racket.png', 5, 400, 40, 200, 10)
racket2 = Player('racket.png', 960, 400, 40, 200, 10)
ball = GameSprite('tenis_ball.png', 400, 400, 70, 70, 10)
run = True
font.init()
font1 = font.SysFont('Algerian',60)

lose1 = font1.render('Racket1 Lose!', True, (0,0,255))
lose2 = font1.render('Racket2 Lose!', True, (0,0,255))
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.blit(background, (0, 0))
        racket1.reset()
        racket1.update_l()
        racket2.reset()
        racket2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > 650:
            speed_y *= -1
        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1,(450,350))
        if ball.rect.x > 1000:
            finish = True
            window.blit(lose2,(450,350))

    display.update()
    clock.tick(60)
