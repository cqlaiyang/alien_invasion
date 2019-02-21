# -*-coding:UTF-8-*-
import pygame

from Stars.settings import Settings
from Stars.alien import Alien
from Stars.ship import Ship
import Stars.game_functions as gf
from pygame.sprite import Group
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

    # 创建一个用于储存子弹,外星人的编组
    bullets =Group()
    aliens = Group()

    # 创建一个外星人群

    gf.create_fleet(ai_settings,screen,ship,aliens)
    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_event(ai_settings,screen,ship,bullets)

        # 更新Ship位置
        ship.update()

        # 删除已经消失的子弹
        gf.update_bullets(aliens,bullets)

        # 更新外星人的位置
        gf.update_aliens(ai_settings,aliens)

        gf.update_screen(ai_settings,screen,ship,aliens,bullets,)

run_game()
