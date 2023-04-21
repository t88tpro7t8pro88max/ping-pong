from pygame import*

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


clock = time.Clock()
FPS = 60
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    class Player(GameSprite):
        def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.y > 5:
                self.rect.y -= self.speed
             if keys[K_RIGHT] and self.rect.y < win_width - 80:
                self.rect.y += self.speed

            if keys[K_LEFT] and self.rect.y > 5:
                self.rect.y -= self.speed
             if keys[K_RIGHT] and self.rect.y < win_width - 80:
                self.rect.y += self.speed


ball = Player('ball.png', 250, 200, 50, 50, 5)
platform1 = Player('platform.jpeg', 300, 250, 30, 150, 5)
platform2 = Player('platform.jpeg', 0, 250, 30, 150, 5)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False





    ball.reset()
    platform1.reset()
    platform2.reset()
    platform1.update_left()
    platform2.update_right()


    display.update()
    clock.tick(FPS)





    