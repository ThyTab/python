import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船发射的子弹的类'''
    def __init__(self, ai_game):
        '''在飞船的当前位置添加一个子弹对象'''
        super().__init__()   #调用super()来继承Sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #在（0，0）处创建子弹矩形，再设置正确的位置
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)   #手动绘制矩形
        self.rect.midtop = ai_game.ship.rect.midtop

        #存储用浮点数表示子弹的位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动子弹'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        pygame.draw.rect(self.screen,self.color,self.rect)   #画矩形
  