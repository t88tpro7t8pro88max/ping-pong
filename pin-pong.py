from pygame import *
from random import randint

win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption("пинг понг")
back = (75, 75, 75)
window.fill(back)

clock = time.Clock()

score = 0
speed_x = 3
speed_y = 3

game = True
finish = False
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed() 

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed

ball = Player("ball.png", 300, 250, 50, 50, 5)
platform1 = Player("platform.jpeg", 0, 250, 30, 150, 5)
platform2 = Player("platform.jpeg", 570, 250, 30, 150, 5)

font.init()
font = font.Font(None, 70)
lose = font.render('YOU LOSE!', True, (180, 0, 0))
total = font.render("Счёт: " + str(score), 1, (255, 255, 255))
window.blit(total, (0, 0))

stop_for_schet = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(back)
    
    
    ball.reset()
    platform1.reset()
    platform2.reset()
    platform1.update_left()
    platform2.update_right()

    if finish != True:
        total = font.render("Счёт: " + str(score), 1, (255, 255, 255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(total, (0, 0))

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
        

    if sprite.collide_rect(platform1, ball) or sprite.collide_rect(platform2, ball):
        speed_x *= -1
        speed_y *= 1

    if ball.rect.x > 600 or ball.rect.x < 0:
        window.blit(lose, (200, 200))
        if stop_for_schet:
            score += 1
            stop_for_schet = False

    display.update()
    clock.tick(FPS)



    



    
