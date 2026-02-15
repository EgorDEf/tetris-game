import arcade
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from views.menu_view import MenuView

class TetrisWindow(arcade.Window):
    def __init__(self):
        super().__init__(
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            SCREEN_TITLE,
            update_rate=1/60,  # 60 FPS
            resizable=False     # Фиксированный размер окна
        )
        # Устанавливаем цвет фона (RGB + Alpha 255 - непрозрачный)
        arcade.set_background_color((10, 10, 40, 255))

def main():
    """Точка входа в игру"""
    window = TetrisWindow()
    menu_view = MenuView()      # Создаём меню
    window.show_view(menu_view) # Показываем меню
    arcade.run()                # Запускаем игровой цикл

if __name__ == "__main__":
    main()