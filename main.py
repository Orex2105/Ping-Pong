from pygame import *
import random
from settings import *

window = display.set_mode((width, height))
clock = time.Clock()
mixer.init()
font.init()
display.set_caption("Игра")
font1 = font.Font(None, 30)
font_for_points = font.Font(None, 30)
point = {
    'player': 0,
    'opponent': 0
}

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
        self.speed_x = speed
        self.speed_y = random.randint(-5, 5)
        self.default_pos = (0.5*width, 0.5*height)

    def update(self):
        if self.rect.bottom >= height:
            self.speed_y = random.randint(-5, -1)
        elif self.rect.top <= 0:
            self.speed_y = random.randint(1, 5)
        if sprite.collide_mask(self, player) or sprite.collide_mask(self, enemy):
            self.speed_x *= -1
        if self.rect.left <= 0:
            point['player'] += 1
            self.rect.x, self.rect.y = self.default_pos
        if self.rect.right >= width:
            point['opponent'] += 1
            self.rect.x, self.rect.y = self.default_pos
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

player = Player('platform.png', 3.5*(width*0.25), height//4, (43, 206), 3)
enemy = Enemy('platform.png', 0.3*(width*0.25), height//4, (43, 206), 3)
ball = Ball('ball.png', 0.5*width, 0.5*height, (32, 32), 5)

finish = False
render_point = False

while True:
    window.fill(white)
    ball.reset(); ball.update()
    player.reset(); player.update()
    enemy.reset(); enemy.update()

    keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            exit()
    if keys[K_TAB]:
        render_point = True
    else:
        render_point = False
    
    if not finish:
        pass
    else:
        pass

    fps_text = font1.render(f'{round(clock.get_fps())}', True, (0, 0, 0))
    point_text_player = font_for_points.render(f'Соперник: {point["opponent"]}', True, (0, 0, 0))
    point_text_opponent = font_for_points.render(f'Игрок: {point["player"]}', True, (0, 0, 0))

    window.blit(fps_text, (width - fps_text.get_width() - 10, height-fps_text.get_height()))
    if render_point:
        window.blit(point_text_player, (200, 10))
        window.blit(point_text_opponent, (600, 10))

    display.update()
    clock.tick(fps)