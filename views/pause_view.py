import arcade
from constants import *


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_draw(self):
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT),
            PAUSE_BG_COLOR
        )

        arcade.draw_text(
            "ПАУЗА",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
            ACCENT_COLOR, 64,
            anchor_x="center",
            bold=True
        )

        # ИСПРАВЛЕНО: новые подсказки по клавишам
        arcade.draw_text(
            "Нажми TAB для продолжения",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30,
            TEXT_COLOR, 24,
            anchor_x="center"
        )

        arcade.draw_text(
            "Нажми ESC для выхода в меню",
            SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80,
            TEXT_SHADOW, 20,
            anchor_x="center"
        )

    def on_key_press(self, key, modifiers):
        # ИСПРАВЛЕНО: TAB - продолжить, ESC - в меню
        if key == arcade.key.TAB:
            self.window.show_view(self.game_view)
            return

        if key == arcade.key.ESCAPE:
            from views.menu_view import MenuView
            menu_view = MenuView()
            self.window.show_view(menu_view)
            return