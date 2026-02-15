import arcade
from constants import *


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = MENU_BG_COLOR
        self.music_player = None
        self.button_clicked = False  # ИСПРАВЛЕНО: флаг для предотвращения двойного клика

    def on_show(self):
        if MUSIC["menu"]:
            sound = arcade.load_sound(MUSIC["menu"])
            self.music_player = arcade.play_sound(sound, volume=0.3)
            if self.music_player:
                self.music_player.looping = True
        self.button_clicked = False  # Сбрасываем флаг при показе

    def on_hide(self):
        if self.music_player:
            arcade.stop_sound(self.music_player)

    def on_draw(self):
        self.clear()

        arcade.draw_text(
            "ТЕТРИС",
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 150,
            arcade.color.WHITE,
            font_size=72,
            anchor_x="center",
            bold=True
        )

        button_y = SCREEN_HEIGHT // 2
        button_spacing = 80

        # Кнопка "Начать игру"
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, button_y, 300, 60),
            (50, 150, 255, 255)
        )
        arcade.draw_text(
            "НАЧАТЬ ИГРУ",
            SCREEN_WIDTH // 2,
            button_y,
            arcade.color.WHITE,
            font_size=28,
            anchor_x="center",
            anchor_y="center"
        )

        # Кнопка "Выход"
        arcade.draw_rect_filled(
            arcade.rect.XYWH(SCREEN_WIDTH // 2, button_y - button_spacing, 300, 60),
            (255, 50, 50, 255)
        )
        arcade.draw_text(
            "ВЫХОД",
            SCREEN_WIDTH // 2,
            button_y - button_spacing,
            arcade.color.WHITE,
            font_size=28,
            anchor_x="center",
            anchor_y="center"
        )

        arcade.draw_text(
            "Управление: ← → ↓ ↑ или WASD, ПРОБЕЛ - быстрый сброс",
            SCREEN_WIDTH // 2,
            100,
            TEXT_SHADOW,
            font_size=16,
            anchor_x="center"
        )

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and not self.button_clicked:
            button_y = SCREEN_HEIGHT // 2
            button_spacing = 80

            # Проверка кнопки "Начать игру"
            if (SCREEN_WIDTH // 2 - 150 <= x <= SCREEN_WIDTH // 2 + 150 and
                    button_y - 30 <= y <= button_y + 30):
                self.button_clicked = True
                from views.game_view import GameView
                game_view = GameView()
                self.window.show_view(game_view)
                return

            # Проверка кнопки "Выход"
            elif (SCREEN_WIDTH // 2 - 150 <= x <= SCREEN_WIDTH // 2 + 150 and
                  button_y - button_spacing - 30 <= y <= button_y - button_spacing + 30):
                self.button_clicked = True
                arcade.close_window()
                return

    def on_key_press(self, key, modifiers):
        if not self.button_clicked:
            if key == arcade.key.ENTER or key == arcade.key.SPACE:
                self.button_clicked = True
                from views.game_view import GameView
                game_view = GameView()
                self.window.show_view(game_view)
            elif key == arcade.key.ESCAPE:
                self.button_clicked = True
                arcade.close_window()