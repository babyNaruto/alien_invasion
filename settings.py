class Settings:
    """存储所有的设置类"""
    alien_points: int

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed_factor = 0.5
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 12
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 以什么样的速度加快游戏
        self.speedup_scale = 1.1

        # 外星人分数提高的速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
