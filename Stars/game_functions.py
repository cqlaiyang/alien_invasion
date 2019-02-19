# -*-coding:UTF-8-*-
import sys
import pygame


def check_event(ship):
    """响应案件和鼠标事件"""
    # 如果判断为QUIT健就退出系统
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_lift =True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_lift = False


def update_screen(ai_setting,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()