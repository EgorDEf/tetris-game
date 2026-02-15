import arcade
from constants import *


class GameOverView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view  # Сохраняем для статистики
        self.background_color = (20, 0, 0, 255)

    def on_draw(self):
        self.clear()

        # Фон
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            (20, 0, 0, 255)
        )

        # Заголовок
        arcade.draw_text(
            "ИГРА ОКОНЧЕНА",
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

        # Кнопка рестарта
        restart_y = SCREEN_HEIGHT // 2 - 120
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, restart_y, 300, 50),
            (50, 150, 255, 200)
        )
        arcade.draw_rect_outline(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, restart_y, 300, 50),
            ACCENT_COLOR, 2
        )
        arcade.draw_text(
            "РЕСТАРТ (R)",
            SCREEN_WIDTH // 2, restart_y,
            TEXT_COLOR, 24,
            anchor_x="center",
            anchor_y="center"
        )

        # Кнопка выхода в меню
        menu_y = SCREEN_HEIGHT // 2 - 190
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, menu_y, 300, 50),
            (255, 50, 50, 200)
        )
        arcade.draw_rect_outline(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, menu_y, 300, 50),
            ACCENT_COLOR, 2
        )
        arcade.draw_text(
            "В МЕНЮ (TAB)",
            SCREEN_WIDTH // 2, menu_y,
            TEXT_COLOR, 24,
            anchor_x="center",
            anchor_y="center"
        )

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            restart_y = SCREEN_HEIGHT // 2 - 120
            menu_y = SCREEN_HEIGHT // 2 - 190

            # Рестарт - создаем НОВУЮ игру
            if (SCREEN_WIDTH // 2 - 150 <= x <= SCREEN_WIDTH // 2 + 150 and
                    restart_y - 25 <= y <= restart_y + 25):
                from views.game_view import GameView
                game_view = GameView()  # Создаем новую игру
                self.window.show_view(game_view)
                return

            # Выход в меню - создаем НОВОЕ меню
            elif (SCREEN_WIDTH // 2 - 150 <= x <= SCREEN_WIDTH // 2 + 150 and
                  menu_y - 25 <= y <= menu_y + 25):
                from views.menu_view import MenuView
                menu_view = MenuView()  # Создаем новое меню
                self.window.show_view(menu_view)
                return

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            from views.game_view import GameView
            game_view = GameView()  # Создаем новую игру
            self.window.show_view(game_view)
            return

        elif key == arcade.key.TAB:
            from views.menu_view import MenuView
            menu_view = MenuView()  # Создаем новое меню
            self.window.show_view(menu_view)
            return