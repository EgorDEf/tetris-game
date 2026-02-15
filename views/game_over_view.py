import arcade
from constants import *


class GameOverView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view  # Сохраняем игровой экран
        self.background_color = (20, 0, 0, 255)

    def on_draw(self):
        """Отрисовка экрана Game Over"""
        self.clear()

        # Тёмный фон
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            (20, 0, 0, 255)
        )

        # Game Over текст
        arcade.draw_text(
            "GAME OVER",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150,
            (255, 50, 50, 255), 72,
            anchor_x="center",
            bold=True
        )

        # Статистика
        arcade.draw_text(
            f"Финальный счет: {self.game_view.game.board.score}",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
            TEXT_COLOR, 32,
            anchor_x="center"
        )

        arcade.draw_text(
            f"Достигнут уровень: {self.game_view.game.level_index + 1}",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
            TEXT_COLOR, 28,
            anchor_x="center"
        )

        arcade.draw_text(
            f"Очищено линий: {self.game_view.game.board.lines_cleared}",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
            TEXT_SHADOW, 24,
            anchor_x="center"
        )

        # Опции
        arcade.draw_text(
            "Нажми R для рестарта",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150,
            ACCENT_COLOR, 26,
            anchor_x="center"
        )

        arcade.draw_text(
            "Нажми ESC для выхода в меню",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200,
            TEXT_SHADOW, 22,
            anchor_x="center"
        )

    def on_key_press(self, key, modifiers):
        """Обработка нажатий клавиш"""
        if key == arcade.key.R:
            # Рестарт игры - импортируем внутри функции
            import sys
            import os
            sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            from views.game_view import GameView
            game_view = GameView()
            self.window.show_view(game_view)

        elif key == arcade.key.ESCAPE:
            # Выход в меню
            from views.menu_view import MenuView
            menu_view = MenuView()
            self.window.show_view(menu_view)