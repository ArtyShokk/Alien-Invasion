class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Настройки экрана
        self.screen_width: int = 1200
        self.screen_height: int = 900
        self.bg_color: tuple = (230, 230, 230)

        # Настройки корабля
        self.ship_limit: int = 3

        # Настройки снарядов
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 100

        # Настройки пришельцев
        self.fleet_drop_speed = 3

        # Темп ускорения игры
        self.speedup_scale = 1.1
        #Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dunamic_settings()


    def initialize_dunamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 0.5

        # fleet_direction = 1 обозначает движ вправо; -1 - влево
        self.fleet_direction = 1

        #Подсчет очков
        self.alien_points = 50


    def increase_speed(self):
        """Увеличение настройки игры и стоимость пришельцев"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
