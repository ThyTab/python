import pygame

class Ship:
    '''管理飞船的类'''
    def __init__(self,ai_game):
        '''初始化飞船并设置初始位置'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()   #获取屏幕的外接矩形
        self.settings = ai_game.settings

        '''加载飞船图形并获取其外接矩形'''
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        '''每艘新飞船都放在屏幕底部的中央'''
        self.rect.midbottom = self.screen_rect.midbottom 

        #在飞船的属性x中存储一个浮点数（为了更精确地调节速度）
        self.x = float(self.rect.x)

        #管理移动
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''用于调整飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:   # >0 也可以
            self.x -= self.settings.ship_speed
        self.rect.x = self.x   #self.rect.x 只存储 self.x 的整数部分

    def center_ship(self):
        '''将飞船放置于屏幕底部中央'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        '''在特定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)   #绘制图像
        #blit() 是将一个图像（Surface）绘制到另一个图像（通常是屏幕）上的核心方法
        #语法：目标图像.blit(源图像, 位置/矩形)     位置：（x,y）   矩形：即矩形对象

        