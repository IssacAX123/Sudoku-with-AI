from user_grid import UserGrid
from random import randint

class PlayGameGrid(UserGrid):
    def __init__(self):
        super().__init__()

    def generate_filler(self, difficulty):
        if difficulty == 'easy':
            filler_range = randint(37, 41)
        elif difficulty == 'medium':
            filler_range =  randint(32, 36)
        elif difficulty == 'hard':
            filler_range =  randint(27, 31)

        for i in range(81-filler_range+1):
            self._game_grid[randint(0, 8)][randint(0, 8)].set_chosen(' ')

