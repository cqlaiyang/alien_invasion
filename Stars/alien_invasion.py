# -*-coding:UTF-8-*-
import pygame

from Stars.settings import Settings
from Stars.ship import Ship
import Stars.game_functions as gf
def run_game():
    # 初始化游戏并且创建一个屏幕对象
    pygame.init()

    # 初始化 Settings
    ai_settings = Settings()

    # 设置屏幕显示大小
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    # 设置窗体颜色
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings,screen)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_event(ship)

        # 更新Ship位置
        ship.update()

        gf.update_screen(ai_settings,screen,ship)

run_game()
