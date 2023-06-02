#импортировать модули
#создать классы
#создать окно, сцену
#создать спрайты
#создать игровой цикл
#обновить спрайты и сцену





# from pygame import *
# from random import randint

# class GameSprite(sprite.Sprite):
#     def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
#         super(). __init__()

#         self.image = transform.scale(image.load(player_image), (size_x, size_y))
#         self.speed = player_speed
#         self.rect = self.image.get_rect()
#         self.rect.x = player_x
#         self.rect.y = player_y
    
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys_passed = key.get_pressed()
#         if keys_passed[K_LEFT] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys_passed[K_RIGHT] and self.rect.x < win_width -80:
#             self.rect.x += self.speed
#     def fire(self):
#         bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
#         bullets.add(bullet)

# class Ball(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width - 80)
#             self.rect.y = 0
#             lost += 1


# win_width = 700
# win_height = 500

# ufos = sprite.Group()

# for i in range(1, 6):
#     ufo = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#     ufos.add(ufo)


# score = 0
# lost = 0
# goal = 10 

# window = display.set_mode((win_width, win_height))
# game = True
# finish = False
# clock = time.Clock()
# FPS = 60

# display.set_caption('Название окна')
# background = transform.scale(image.load("задник"), (win_width, win_height))

# player = Player('игрок', 5, win_height - 100, 80, 100, 10)


# font.init()
# font1 = font.Font(None, 100)

# font2 = font.Font(None, 40)
# win = font1.render('YOU WIN! :D', True, (255, 215, 0))
# lose = font1.render('YOU LOSE! :(', True, (180, 0, 0))

# """музыка"""
# mixer.init()
# mixer.music.load()
# mixer.music.play()
# kick = mixer.Sound()
# """""""

# while game:
#     for e in event.get():
#         if e.type == QUIT:
#             game = False
#         elif e.type == KEYDOWN:
#             if e.key == K_SPACE:
#                 player.fire()    
#     if finish != True:
#         window.blit(background,(0, 0))
        
#         win.blit(lose, (200, 200))

#         text = font2.render("Score:"+str(score), 1, (255, 255, 255))
#         window.blit(text, (10, 20))

#         text_lose = font2.render("Lost:"+str(lost), 1, (255, 255, 255))
#         window.blit(text_lose, (10, 50))
        
#         player.update()
#         ufos.update()
#         bullets.update()


#         player.reset()
#         ufos.draw(window)
#         bullets.draw(window)

#     collides = sprite.groupcollide(bullets, ufos, True, True)
#     for ufo in collides:
#         ufo = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
#         ufos.add(ufo)
#         score+=1
# #lost
#     if sprite.spritecollide(player, ufos, False) or lost >= 3:
#         finish = True
#         window.blit(lose, (150, 190))

# #won
#     if score >= goal:
#         finish = True
#         window.blit(win, (150, 190))


#     display.update()
#     time.delay(25)