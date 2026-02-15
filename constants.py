# ============ ОСНОВНЫЕ НАСТРОЙКИ ============
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Тетрис PyGame"
FPS = 60

# ============ ЦВЕТА ============
BACKGROUND_COLOR = (10, 10, 40, 255)
MENU_BG_COLOR = (20, 20, 60, 255)
TEXT_COLOR = (255, 255, 255, 255)
TEXT_SHADOW = (100, 100, 150, 255)
ACCENT_COLOR = (255, 215, 0, 255)

GRID_COLOR = (50, 50, 100, 255)
GRID_LINE_COLOR = (80, 80, 130, 255)
PAUSE_BG_COLOR = (30, 30, 80, 200)

# ============ ТЕТРИС-ФИГУРЫ ============
TETROMINOES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1]]
]

COLORS = [
    (0, 255, 255, 255),
    (255, 255, 0, 255),
    (128, 0, 128, 255),
    (0, 255, 0, 255),
    (255, 0, 0, 255),
    (0, 0, 255, 255),
    (255, 165, 0, 255)
]

# ============ ИГРОВЫЕ НАСТРОЙКИ ============
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 30
BOARD_OFFSET_X = 100
BOARD_OFFSET_Y = 50
LIVES = 3

# ИСПРАВЛЕНО: новая скорость движения (было 5, стало 2)
PLAYER_SPEED = 2  # <-- ИЗМЕНЕНО с 5 на 2

LEVELS = [
    {
        "name": "Новичок",
        "required_score": 1000,
        "speed": 1.2,        # Медленное падение
        "lines_per_level": 5,
        "color": (100, 200, 255, 255)
    },
    {
        "name": "Мастер",
        "required_score": 5000,
        "speed": 1.0,        # ИСПРАВЛЕНО: было 0.7 (слишком быстро), стало 1.0 (чуть быстрее)
        "lines_per_level": 10,
        "color": (255, 200, 100, 255)
    }
]

SCORE_PER_LINE = 100
SCORE_PER_LEVEL_MULTIPLIER = 2

# ============ УПРАВЛЕНИЕ ============
CONTROLS = {
    "left": ["left", "a"],
    "right": ["right", "d"],
    "rotate": ["up", "w"],
    "soft_drop": ["down", "s"],
    "hard_drop": ["space"],
    "pause": ["escape"],
    "restart": ["r"]
}

# ============ ЗВУКИ ============
SOUNDS = {
    "rotate": ":resources:/sounds/laser1.wav",
    "move": ":resources:/sounds/jump1.wav",
    "line_clear": ":resources:/sounds/coin1.wav",
    "level_up": ":resources:/sounds/upgrade1.wav",
    "game_over": ":resources:/sounds/gameover1.wav",
    "life_lost": ":resources:/sounds/hurt3.wav"
}

MUSIC = {
    "menu": ":resources:/music/funkyrobot.mp3",
    "game": ":resources:/music/1918.mp3"
}