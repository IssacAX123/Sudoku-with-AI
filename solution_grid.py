from grid import Grid
from random import randint


class SolutionGrid(Grid):
    def __init__(self):
        super().__init__()
        self._game_grid[randint(0, 8)][randint(0, 8)].set_chosen(str(randint(1, 9)))
        self._game_grid[0][randint(0, 8)].set_chosen(str(randint(1, 9)))
        self._game_grid[1][randint(0, 8)].set_chosen(str(randint(1, 9)))
        self.place_number()


