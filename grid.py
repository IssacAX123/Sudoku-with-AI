class GameGrid:
    game_grid = []
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def create_empty_grid(self):
        for row in range(9):
            row = []
            for column in range(9):
                row.append([])
            GameGrid.game_grid.append(row)

    def print_grid(self):
        for row in GameGrid.game_grid:
            print(row)


