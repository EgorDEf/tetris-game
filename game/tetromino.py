import random
from constants import TETROMINOES, COLORS


class Tetromino:


    def __init__(self, x, y, shape_idx=None):

        if shape_idx is None:
            shape_idx = random.randint(0, len(TETROMINOES) - 1)

        self.shape = TETROMINOES[shape_idx]  # Матрица фигуры
        self.color = COLORS[shape_idx]  # Цвет фигуры
        self.x = x
        self.y = y
        self.rotation = 0

    def rotate(self, clockwise=True):

        if clockwise:
            # Поворот по часовой стрелке
            rows = len(self.shape)
            cols = len(self.shape[0])
            rotated = [[self.shape[rows - 1 - r][c] for r in range(rows)]
                       for c in range(cols)]
        else:
            # Поворот против часовой стрелки
            rows = len(self.shape)
            cols = len(self.shape[0])
            rotated = [[self.shape[r][cols - 1 - c] for r in range(rows)]
                       for c in range(cols)]

        self.shape = rotated
        self.rotation = (self.rotation + (1 if clockwise else -1)) % 4

    def get_cells(self):

        cells = []
        for r, row in enumerate(self.shape):
            for c, cell in enumerate(row):
                if cell:
                    cells.append((self.x + c, self.y - r))
        return cells

    def clone(self):

        new_tetromino = Tetromino(self.x, self.y)
        new_tetromino.shape = [row[:] for row in self.shape]
        new_tetromino.color = self.color
        new_tetromino.rotation = self.rotation
        return new_tetromino