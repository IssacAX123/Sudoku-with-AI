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
        print('  1 2 3  4 5 6  7 8 9')
        for row_index, row in enumerate(GameGrid.game_grid):
            for column_index, column in enumerate(row):
                if (column_index + 1) % 9 != 0:
                    if (column_index + 1) != 9 and (column_index + 1) % 3 == 0:
                        print(column, end="-")
                    else:
                        if (column_index + 1) % 9 == 1:
                            print(row_index + 1, end=" ")
                            print(column, end="")
                        else:
                            print(column, end="")
                else:
                    print(column, end="\n")
                    if (row_index + 1) % 3 == 0:
                        print(' ', '-' * 20)
