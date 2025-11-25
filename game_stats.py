# class GameStats:
#     """Track statistics for Alien Invasion."""

#     def __init__(self, ai_game):
#         """Initialize statistics."""
#         self.settings = ai_game.settings
#         self.reset_stats()

#         # High score should never be reset.
#         self.high_score = 0

#     def reset_stats(self):
#         """Initialize statistics that can change during the game."""
#         self.ships_left = self.settings.ship_limit
#         self.score = 0
#         self.level = 1

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        # 修改：从文件读取历史最高分，如果文件不存在则初始化为0
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    # 新增：从文件加载最高分的方法
    def _load_high_score(self):
        """Load high score from file, return 0 if file doesn't exist."""
        try:
            with open('high_score.txt', 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            # 如果文件不存在，返回0作为初始最高分
            return 0
        except ValueError:
            # 如果文件内容不是有效数字，返回0
            return 0
    
    # 新增：保存最高分到文件的方法
    def save_high_score(self):
        """Save high score to file."""
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))