from pygame import *
import random
import math
from settings import *

window = display.set_mode((width, height))
clock = time.Clock()
mixer.init()
font.init()
display.set_caption("Игра")
font1 = font.Font(None, 30)


class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, size, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (size[0], size[1]))
        #https://pg1.readthedocs.io/en/latest/ref/sprite.html#pygame.sprite.collide_mask
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, pimage, x, y, size, speed):
        super().__init__(pimage, x, y, size, speed)

    def update(self):
        keys = key.get_pressed()
        if keys[K_w]:
            if self.rect.y != 0.01*height:
                self.rect.y -= self.speed
        if keys[K_s]:
            if self.rect.y != height-0.35*height:
                self.rect.y += self.speed


class Enemy(GameSprite):
    def __init__(self, pimage, x, y, size, speed):
        super().__init__(pimage, x, y, size, speed)
        self.move = 'up'

    def update(self):
        if self.rect.y == height-0.35*height:
            self.move = 'up'
        if self.rect.y == 0.01*height:
            self.move = 'down'
        if self.move == 'up':
            self.rect.y -= self.speed
        if self.move == 'down':
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, pimage, x, y, size, speed):
        super().__init__(pimage, x, y, size, speed)

player = Player('platform.png', 3.5*(width*0.25), height//4, (43, 206), 3)
enemy = Enemy('platform.png', 0.3*(width*0.25), height//4, (43, 206), 3)

finish = False

while True:
    window.fill(white)
    player.reset()
    player.update()
    enemy.reset()
    enemy.update()

    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            exit()
    
    if not finish:
        pass
    else:
        pass

    fps_text = font1.render(f'fps: {round(clock.get_fps())}', True, (0, 0, 0))

    window.blit(fps_text, (width//2, 15))

    display.update()
    clock.tick(fps)




'''class Button(GameSprite):
    def __init__(self, pimage, x, y, size, name, speed):
        super().__init__(pimage, x, y, speed)
        self.width = size[0]
        self.height = size[1]
        self.button_name = name
        self.image = transform.scale(image.load(pimage), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0

    def update(self):
        x_mouse, y_mouse = mouse.get_pos()
        mouse_rect = Rect(x_mouse, y_mouse, 1, 1)
        if self.rect.colliderect(mouse_rect):
            if mouse.get_pressed()[0]:
                return self.button_name'''