#импортировать модули
#создать классы
#создать окно, сцену
#создать спрайты
#создать игровой цикл
#обновить спрайты и сцену



from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
         super(). __init__()

         self.image = transform.scale(image.load(player_image), (size_x, size_y))
         self.speed = player_speed
         self.rect = self.image.get_rect()
         self.rect.x = player_x
         self.rect.y = player_y
     def reset(self):
         window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_DOWN] and self.rect.y < win_height -80:
            self.rect.y += self.speed
    
    def update_left(self):
        keys_passed = key.get_pressed()
        if keys_passed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_passed[K_s] and self.rect.y < win_height -80:
            self.rect.y += self.speed


class Ball(GameSprite):
    pass


win_width = 700
win_height = 500

score = 0
lost = 0
goal = 10 

background_colour = (135,206,235)


window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60

display.set_caption('Название окна')

player_left = Player('platform.png', 0, 0, 30, 100, 1)
player_right = Player('platform.png', 0, 0, 30, 100, 1)

"""
mixer.init()
mixer.music.load()
mixer.music.play()
kick = mixer.Sound()
"""

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False  
    window.fill(background_colour) 
    
    player_left.update_left()
    player_right.update_right()
    player_left.reset()
    player_right.reset()
    
    display.update()
clock.tick(FPS)
