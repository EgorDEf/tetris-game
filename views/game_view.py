import arcade
from constants import *
from game.game_logic import TetrisGame


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.game = TetrisGame()
        self.background_color = BACKGROUND_COLOR
        self.music_player = None
        self.keys_pressed = set()
        self.info_texts = []  # ИСПРАВЛЕНО: для текстовых объектов вместо draw_text

    def on_show(self):
        if MUSIC["game"]:
            sound = arcade.load_sound(MUSIC["game"])
            self.music_player = arcade.play_sound(sound, volume=0.2)
            if self.music_player:
                self.music_player.looping = True

    def on_hide(self):
        if self.music_player:
            arcade.stop_sound(self.music_player)

    def on_draw(self):
        self.clear()

        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            BACKGROUND_COLOR
        )

        self._draw_board()
        self._draw_current_piece()  # ИСПРАВЛЕНО: без проекции
        self._draw_next_piece()
        self._draw_info_panel()

        if not self.game.game_active:
            self._draw_game_over()

    def _draw_board(self):
        board_left = BOARD_OFFSET_X - 5
        board_right = BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE + 5
        board_top = BOARD_OFFSET_Y + BOARD_HEIGHT * CELL_SIZE + 5
        board_bottom = BOARD_OFFSET_Y - 5

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                (board_left + board_right) // 2,
                (board_bottom + board_top) // 2,
                board_right - board_left,
                board_top - board_bottom
            ),
            (40, 40, 80, 255)
        )

        # Сетка
        for x in range(BOARD_WIDTH + 1):
            line_x = BOARD_OFFSET_X + x * CELL_SIZE
            arcade.draw_line(
                line_x, BOARD_OFFSET_Y,
                line_x, BOARD_OFFSET_Y + BOARD_HEIGHT * CELL_SIZE,
                GRID_LINE_COLOR, 1
            )

        for y in range(BOARD_HEIGHT + 1):
            line_y = BOARD_OFFSET_Y + y * CELL_SIZE
            arcade.draw_line(
                BOARD_OFFSET_X, line_y,
                BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE, line_y,
                GRID_LINE_COLOR, 1
            )

        # Заполненные клетки
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.game.board.grid[y][x]:
                    color = self.game.board.grid[y][x]
                    self._draw_cell(x, y, color, False)

    def _draw_current_piece(self):
        """Рисует только текущую фигуру, без проекции"""
        if not self.game.current_piece or not self.game.game_active:
            return

        # ИСПРАВЛЕНО: убрана проекция, только сама фигура
        for x, y in self.game.current_piece.get_cells():
            if 0 <= y < BOARD_HEIGHT:
                self._draw_cell(x, y, self.game.current_piece.color, False)

    def _draw_next_piece(self):
        if not self.game.next_piece:
            return

        next_panel_x = BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE + 50
        next_panel_y = SCREEN_HEIGHT - 150

        # ИСПРАВЛЕНО: используем Text объекты вместо draw_text
        next_label = arcade.Text(
            "Следующая:",
            next_panel_x, next_panel_y,
            TEXT_COLOR, 20
        )
        next_label.draw()

        piece = self.game.next_piece
        for r, row in enumerate(piece.shape):
            for c, cell in enumerate(row):
                if cell:
                    draw_x = next_panel_x + c * CELL_SIZE
                    draw_y = next_panel_y - 50 - r * CELL_SIZE

                    arcade.draw_rect_filled(
                        arcade.rect.XYWH(draw_x + CELL_SIZE // 2, draw_y + CELL_SIZE // 2,
                                         CELL_SIZE - 2, CELL_SIZE - 2),
                        piece.color
                    )

                    arcade.draw_rect_outline(
                        arcade.rect.XYWH(draw_x + CELL_SIZE // 2, draw_y + CELL_SIZE // 2,
                                         CELL_SIZE - 2, CELL_SIZE - 2),
                        (255, 255, 255, 100), 1
                    )

    # ЗАМЕНИ только метод _draw_info_panel в game_view.py

    # ЗАМЕНИ метод _draw_info_panel в game_view.py на этот:

    def _draw_info_panel(self):
        info_x = BOARD_OFFSET_X + BOARD_WIDTH * CELL_SIZE + 50
        info_y = SCREEN_HEIGHT - 250

        # Уровень
        level_text = arcade.Text(
            f"Уровень: {self.game.level_index + 1}",
            info_x, info_y,
            self.game.current_level["color"], 24
        )
        level_text.draw()

        level_name = arcade.Text(
            self.game.current_level["name"],
            info_x, info_y - 30,
            TEXT_COLOR, 18
        )
        level_name.draw()

        # Очки и цель
        score_text = arcade.Text(
            f"Очки: {self.game.board.score}",
            info_x, info_y - 80,
            ACCENT_COLOR, 24
        )
        score_text.draw()

        target_text = arcade.Text(
            f"Цель: {self.game.current_level['required_score']}",
            info_x, info_y - 110,
            TEXT_SHADOW, 16
        )
        target_text.draw()

        # Жизни (сердечки)
        lives_text = arcade.Text(
            f"Жизни: {self.game.board.lives}",
            info_x, info_y - 150,
            TEXT_COLOR, 20
        )
        lives_text.draw()

        for i in range(3):
            x_pos = info_x + i * 35
            if i < self.game.board.lives:
                # Живое сердечко
                arcade.draw_rect_filled(
                    arcade.rect.XYWH(x_pos, info_y - 180, 30, 30),
                    (255, 50, 50, 255)
                )
                # Блик
                arcade.draw_rect_filled(
                    arcade.rect.XYWH(x_pos - 5, info_y - 170, 10, 10),
                    (255, 255, 255, 100)
                )
            else:
                # Потерянное сердечко
                arcade.draw_rect_filled(
                    arcade.rect.XYWH(x_pos, info_y - 180, 30, 30),
                    (50, 50, 50, 255)
                )
                # Крестик
                arcade.draw_line(
                    x_pos - 10, info_y - 165,
                    x_pos + 10, info_y - 195,
                    (100, 100, 100, 255), 3
                )
                arcade.draw_line(
                    x_pos - 10, info_y - 195,
                    x_pos + 10, info_y - 165,
                    (100, 100, 100, 255), 3
                )

            arcade.draw_rect_outline(
                arcade.rect.XYWH(x_pos, info_y - 180, 30, 30),
                (255, 255, 255, 50), 1
            )

        # ИСПРАВЛЕНО: Управление с правильными клавишами
        controls_title = arcade.Text(
            "Управление:",
            info_x, info_y - 230,
            TEXT_COLOR, 16
        )
        controls_title.draw()

        controls_text = [
            "←→/AD: Движение",
            "↑/W: Поворот",
            "↓/S: Быстрый спуск",
            "ПРОБЕЛ: Мгновенный сброс",
            "TAB: Пауза",  # ИСПРАВЛЕНО: было ESC, стало TAB
            "R: Рестарт"
        ]

        for i, text in enumerate(controls_text):
            control = arcade.Text(
                text,
                info_x, info_y - 260 - i * 25,
                TEXT_SHADOW, 14
            )
            control.draw()

    @staticmethod
    def _draw_cell(grid_x, grid_y, color, is_ghost):
        screen_x = BOARD_OFFSET_X + grid_x * CELL_SIZE + CELL_SIZE // 2
        screen_y = BOARD_OFFSET_Y + grid_y * CELL_SIZE + CELL_SIZE // 2

        if is_ghost:
            arcade.draw_rect_filled(
                arcade.rect.XYWH(screen_x, screen_y, CELL_SIZE - 2, CELL_SIZE - 2),
                color
            )
            arcade.draw_rect_outline(
                arcade.rect.XYWH(screen_x, screen_y, CELL_SIZE - 2, CELL_SIZE - 2),
                (color[0], color[1], color[2], 120), 1
            )
        else:
            # Тень
            arcade.draw_rect_filled(
                arcade.rect.XYWH(screen_x - 2, screen_y - 2, CELL_SIZE - 2, CELL_SIZE - 2),
                (color[0] // 3, color[1] // 3, color[2] // 3, 255)
            )

            # Основной блок
            arcade.draw_rect_filled(
                arcade.rect.XYWH(screen_x, screen_y, CELL_SIZE - 4, CELL_SIZE - 4),
                color
            )

            # Светлая часть
            light_color = (
                min(255, color[0] + 50),
                min(255, color[1] + 50),
                min(255, color[2] + 50),
                100
            )
            arcade.draw_rect_filled(
                arcade.rect.XYWH(screen_x - CELL_SIZE // 4, screen_y + CELL_SIZE // 4,
                                 CELL_SIZE // 2, CELL_SIZE // 2),
                light_color
            )

            # Контур
            arcade.draw_rect_outline(
                arcade.rect.XYWH(screen_x, screen_y, CELL_SIZE - 4, CELL_SIZE - 4),
                (255, 255, 255, 50), 1
            )

    def _draw_game_over(self):
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, 0, 0, 180)
        )

        game_over_text = arcade.Text(
            "ИГРА ОКОНЧЕНА",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
            (255, 50, 50, 255), 48,
            anchor_x="center"
        )
        game_over_text.draw()

        score_text = arcade.Text(
            f"Финальный счет: {self.game.board.score}",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
            TEXT_COLOR, 24,
            anchor_x="center"
        )
        score_text.draw()

        esc_text = arcade.Text(
            "Нажми ESC для выхода в меню",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
            TEXT_SHADOW, 20,
            anchor_x="center"
        )
        esc_text.draw()

        restart_text = arcade.Text(
            "Нажми R для рестарта",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100,
            TEXT_SHADOW, 20,
            anchor_x="center"
        )
        restart_text.draw()

    def on_update(self, delta_time):
        if self.game.paused or not self.game.game_active:
            return

        if self.game.level_complete:
            from views.level_complete_view import LevelCompleteView
            level_complete_view = LevelCompleteView(self, self.game.level_index + 1)
            self.window.show_view(level_complete_view)
            self.game.level_complete = False
            return

        self.game.update(delta_time)

        if self.game.move_cooldown <= 0:
            moved = False
            if arcade.key.LEFT in self.keys_pressed or arcade.key.A in self.keys_pressed:
                self.game.move_piece(-1, 0)
                moved = True
            elif arcade.key.RIGHT in self.keys_pressed or arcade.key.D in self.keys_pressed:
                self.game.move_piece(1, 0)
                moved = True

            if moved:
                self.game.move_cooldown = self.game.move_delay

        if arcade.key.DOWN in self.keys_pressed or arcade.key.S in self.keys_pressed:
            self.game.move_piece(0, -1)

    # ЗАМЕНИ только метод on_key_press в game_view.py

    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)

        # ИСПРАВЛЕНО: TAB для паузы
        if key == arcade.key.TAB:
            if not self.game.game_active:
                from views.game_over_view import GameOverView
                game_over_view = GameOverView(self)
                self.window.show_view(game_over_view)
            else:
                from views.pause_view import PauseView
                pause_view = PauseView(self)
                self.window.show_view(pause_view)
            return

        elif key == arcade.key.R:
            self.game = TetrisGame()
            return

        elif key == arcade.key.UP or key == arcade.key.W:
            self.game.rotate_piece()
            return

        elif key == arcade.key.SPACE:
            self.game.hard_drop()
            return

        # Остальные клавиши для движения обрабатываются в on_update

    def on_key_release(self, key, modifiers):
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)