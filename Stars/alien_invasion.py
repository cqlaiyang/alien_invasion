# -*-coding:UTF-8-*-
import sys
import pygame

from Stars.settings import Settings
from Stars.ship import Ship
def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()

    # 初始化 Settings
    ai_settings = Settings()

    # 设置屏幕显示大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    # 设置窗体颜色
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 设置背景颜色
        screen.fill(ai_settings.bg_color)

        ship.blitme()

        # 让最近绘制屏幕可见
        pygame.display.flip()

run_game()
