import sys   #用于退出
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()   #初始化背景
        self.settings = Settings()   #将实例作为参数
        #以下注释代码可实现全屏 
        '''self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width   
        self.settings.screen_height = self.screen.get_rect().height'''
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        #将surface（已配置大小）赋给self.screen的同时创建屏幕
        pygame.display.set_caption("Alien Invasion")   #为屏幕添加标题
        self.clock = pygame.time.Clock()   #为控制帧率做准备
        self.stats = GameStats(self)   #创建一个用于存储游戏统计数据的实例
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()   #创建用于存储子弹的编组
        self.aliens = pygame.sprite.Group()   #创建存储外星舰队的编组
        self._create_fleet()

        self.game_active = True   #游戏启动后处于活动状态

    def run_game(self):
        '''开始游戏的主循环'''
        while True:   #游戏的主循环
            self._check_event()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)   #控制帧率

    def _check_event(self):
        '''检查按键和鼠标事件'''
        #侦听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   #退出
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''创建一颗子弹,并将其加入编组bullets'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)   #为编组加入元素

    def _update_bullets(self):
        '''更新子弹的位置并删除子弹'''
        self.bullets.update()
        #删除已消失的子弹
        #for循环不能从列表或编组中删除元素，因此必须遍历编组的副本，从而修改原始编组
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        

    def _check_bullet_alien_collisions(self):
        #检查是否有子弹击中了外星人
        #如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        #此方法将所有子弹和外星人进行比较，collisions为返回的字典，键表示子弹，值为外星人
        #两个值为True的实参告诉pygame发生碰撞时删除对应的子弹和外星人
        if not self.aliens:
            #删除现有的子弹并创建一个新的舰队
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        '''用于更新屏幕上的图形并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        #对编组调用draw()方法时，会将编组中所有元素绘制在属性rect指定的位置上
        #draw()方法接受一个参数，即表示绘制在哪个surface上
        pygame.display.flip()   #让最近绘制的屏幕可见，刷新屏幕

    def _create_fleet(self):
        '''创建一个外星舰队'''
        #创建一个外星人，再不断添加，直到没有空间添加外星人为止
        #外星人的间距为外星人的宽度和高度
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        
        current_x,current_y = alien_width,alien_height
        while current_y < (self.settings.screen_height - 5*alien_height):
            while current_x < (self.settings.screen_width - 2*alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2*alien_width
            #添加一行外星人后，重置x值并递增y值
            current_x = alien_width
            current_y += 2*alien_height

    def _create_alien(self,x_position,y_position):
        '''创建一个外星人并将其放在当前行中'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        '''有外星人到达边缘时采取相应措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''让整个舰队向下移动，并改变他们的方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        '''响应外星人与飞船的碰撞'''
        if self.stats.ships_left > 0:
            #飞船数量-1
            self.stats.ships_left -= 1
            #清空外星人列表和子弹列表
            self.aliens.empty()
            self.bullets.empty()
            #创建一个新的外星舰队并将飞船放置于屏幕底部正中央
            self._create_fleet()
            self.ship.center_ship()
            #暂停
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        '''检查是否有外星人到达屏幕下边缘'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                #像飞船被撞到一样处理
                self._ship_hit()
                break

    def _update_aliens(self):
        '''检查是否有外星人位于屏幕边缘，并更新所有外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()
        #检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):   #若未碰撞，此方法会返回None；若碰撞，会返回这个外星人
            self._ship_hit()
        #检查是否有外星人到达屏幕下边缘
        self._check_aliens_bottom()


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
