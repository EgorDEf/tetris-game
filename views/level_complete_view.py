import arcade
from constants import *


class LevelCompleteView(arcade.View):
    def __init__(self, game_view, next_level_index):
        super().__init__()
        self.game_view = game_view
        self.next_level_index = next_level_index

        if next_level_index < len(LEVELS):
            self.next_level = LEVELS[next_level_index]
        else:
            self.next_level = None

    def on_draw(self):
        self.clear()

        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            BACKGROUND_COLOR
        )

        if self.next_level:
            arcade.draw_text(
                "УРОВЕНЬ ПРОЙДЕН!",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100,
                (100, 255, 100, 255), 48,
                anchor_x="center",
                bold=True
            )

            arcade.draw_text(
                f"Переходим на уровень {self.next_level_index + 1}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30,
                TEXT_COLOR, 28,
                anchor_x="center"
            )

            arcade.draw_text(
                f"Название: {self.next_level['name']}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20,
                self.next_level["color"], 32,
                anchor_x="center"
            )


            arcade.draw_text(
                f"Текущие очки: {self.game_view.game.board.score}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 70,
                ACCENT_COLOR, 24,
                anchor_x="center"
            )

            arcade.draw_text(
                f"Нужно для победы: {self.next_level['required_score']}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 110,
                TEXT_COLOR, 20,
                anchor_x="center"
            )

            arcade.draw_text(
                "Нажми ПРОБЕЛ для продолжения",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 180,
                ACCENT_COLOR, 22,
                anchor_x="center"
            )
        else:
            arcade.draw_text(
                "ИГРА ПРОЙДЕНА!",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100,
                (255, 215, 0, 255), 64,
                anchor_x="center",
                bold=True
            )

            arcade.draw_text(
                "Поздравляем!",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20,
                TEXT_COLOR, 36,
                anchor_x="center"
            )

            arcade.draw_text(
                f"Финальный счет: {self.game_view.game.board.score}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                ACCENT_COLOR, 28,
                anchor_x="center"
            )

            arcade.draw_text(
                f"Очищено линий: {self.game_view.game.board.lines_cleared}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100,
                TEXT_COLOR, 24,
                anchor_x="center"
            )

            arcade.draw_text(
                "Нажми ESC для выхода в меню",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 180,
                TEXT_SHADOW, 22,
                anchor_x="center"
            )

    def on_key_press(self, key, modifiers):
        if self.next_level:
            if key == arcade.key.SPACE or key == arcade.key.ENTER:

                self.game_view.game.next_level()
                self.window.show_view(self.game_view)
        else:
            if key == arcade.key.ESCAPE:
                from views.menu_view import MenuView
                menu_view = MenuView()
                self.window.show_view(menu_view)