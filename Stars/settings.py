# -*-coding:UTF-8-*-

class Settings():
    """储存《外星人入侵》的所有设置的类"""
    bg_color = None

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)