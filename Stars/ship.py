# -*-coding:UTF-8-*-
import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """初始化飞船并且设置初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('../images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志位
        self.moving_right = False
        self.moving_lift = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_lift and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
