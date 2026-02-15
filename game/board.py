import arcade
from constants import BOARD_WIDTH, BOARD_HEIGHT, SOUNDS, SCORE_PER_LINE


class Board:
    def __init__(self):
        self.width = BOARD_WIDTH
        self.height = BOARD_HEIGHT
        self.grid = [[None for _ in range(self.width)]
                     for _ in range(self.height)]
        self.score = 0
        self.level = 0
        self.lines_cleared = 0
        self.lives = 3
        self.game_over = False

    def is_valid_position(self, tetromino):
        for x, y in tetromino.get_cells():
            if x < 0 or x >= self.width or y < 0:
                return False
            if y < self.height and self.grid[y][x] is not None:
                return False
        return True

    def place_tetromino(self, tetromino):
        """Размещает фигуру на поле"""
        for x, y in tetromino.get_cells():
            if 0 <= y < self.height:
                self.grid[y][x] = tetromino.color

        # Проверяем и очищаем линии
        self._check_and_clear_lines()

    def _check_and_clear_lines(self):
        """Проверяет все линии и очищает заполненные, опуская всё что выше"""
        lines_cleared = 0
        y = self.height - 1  # Начинаем с самого низа

        while y >= 0:
            # Проверяем, заполнен ли текущий ряд
            if all(cell is not None for cell in self.grid[y]):
                # Ряд заполнен - удаляем его
                lines_cleared += 1

                # ИСПРАВЛЕНО: опускаем все ряды ВЫШЕ на одну позицию вниз
                for move_y in range(y, self.height - 1):
                    self.grid[move_y] = self.grid[move_y + 1][:]

                # Самый верхний ряд делаем пустым
                self.grid[self.height - 1] = [None for _ in range(self.width)]

                # Продолжаем проверять с той же позиции y (так как ряды сместились)
                # Не увеличиваем y, так как ряд сместился
            else:
                y -= 1  # Переходим к ряду выше

        if lines_cleared > 0:
            # Начисляем очки
            self.lines_cleared += lines_cleared
            self.score += lines_cleared * SCORE_PER_LINE * (self.level + 1)

            # Звук
            arcade.play_sound(arcade.load_sound(SOUNDS["line_clear"]), volume=0.5)

            # Обновляем уровень
            self.update_level()

        return lines_cleared

    def update_level(self):
        new_level = self.lines_cleared // 10
        if new_level != self.level:
            self.level = new_level

    def check_top_reached(self):
        return any(self.grid[0])

    def reset_for_new_life(self):
        self.grid = [[None for _ in range(self.width)]
                     for _ in range(self.height)]

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.game_over = True
            arcade.play_sound(arcade.load_sound(SOUNDS["game_over"]), volume=0.7)
        else:
            arcade.play_sound(arcade.load_sound(SOUNDS["life_lost"]), volume=0.5)
            self.reset_for_new_life()
        return self.lives > 0