import arcade
from constants import *
from .tetromino import Tetromino
from .board import Board


class TetrisGame:
    def __init__(self):
        self.board = Board()
        self.current_piece = None
        self.next_piece = None
        self.fall_speed = LEVELS[0]["speed"]
        self.fall_timer = 0
        self.level_index = 0
        self.current_level = LEVELS[0]
        self.paused = False
        self.game_active = True
        self.level_complete = False
        self.move_cooldown = 0
        self.move_delay = 0.1

        self.spawn_new_piece()
        self.spawn_next_piece()

    def spawn_new_piece(self):
        start_x = BOARD_WIDTH // 2 - 1
        start_y = BOARD_HEIGHT - 1

        if self.next_piece:
            self.current_piece = self.next_piece
            self.current_piece.x = start_x
            self.current_piece.y = start_y
        else:
            self.current_piece = Tetromino(start_x, start_y)

        if not self.board.is_valid_position(self.current_piece):
            self.board.lose_life()
            if self.board.lives > 0:
                self.board.reset_for_new_life()
                self.spawn_new_piece()
            else:
                self.game_active = False
                self.board.game_over = True
            return

        self.spawn_next_piece()

    def spawn_next_piece(self):
        self.next_piece = Tetromino(0, 0)

    def move_piece(self, dx, dy):
        if not self.game_active or self.paused:
            return False

        self.current_piece.x += dx
        self.current_piece.y += dy

        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.x -= dx
            self.current_piece.y -= dy
            return False

        arcade.play_sound(arcade.load_sound(SOUNDS["move"]), volume=0.3)
        return True

    def rotate_piece(self):
        if not self.game_active or self.paused:
            return

        original_shape = [row[:] for row in self.current_piece.shape]
        self.current_piece.rotate()

        if not self.board.is_valid_position(self.current_piece):
            self.current_piece.shape = original_shape

        arcade.play_sound(arcade.load_sound(SOUNDS["rotate"]), volume=0.3)

    def hard_drop(self):
        if not self.game_active or self.paused:
            return

        while True:
            if not self.move_piece(0, -1):
                break

        self.lock_piece()

    def lock_piece(self):
        if not self.game_active or self.paused:
            return


        self.board.place_tetromino(self.current_piece)


        if self.check_level_complete():
            self.level_complete = True
            arcade.play_sound(arcade.load_sound(SOUNDS["level_up"]), volume=0.5)


        self.spawn_new_piece()

    def check_level_complete(self):
        return self.board.score >= self.current_level["required_score"]

    def next_level(self):

        if self.level_index < len(LEVELS) - 1:
            self.level_index += 1
            self.current_level = LEVELS[self.level_index]
            self.fall_speed = self.current_level["speed"]


            self.fall_timer = 0


            self.board.reset_for_new_life()


            self.current_piece = None
            self.next_piece = None


            self.spawn_new_piece()
            self.spawn_next_piece()

            self.level_complete = False
            return True
        return False

    def update(self, delta_time):
        if not self.game_active or self.paused:
            return


        if self.move_cooldown > 0:
            self.move_cooldown -= delta_time

        self.fall_timer += delta_time

        if self.fall_timer >= self.fall_speed:
            self.fall_timer = 0

            if not self.move_piece(0, -1):
                self.lock_piece()