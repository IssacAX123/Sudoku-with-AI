from cell import Cell

class Grid:
    def __init__(self):
        self._game_grid = []
        self.create_empty_grid()

    def create_empty_grid(self):
        for row in range(9):
            row = []
            for column in range(9):
                cell_obj = Cell(row, column)
                row.append(cell_obj)
            self._game_grid.append(row)

    def print_grid(self):
        print('  1 2 3   4 5 6   7 8 9')
        for row_index, row in enumerate(self._game_grid):
            for column_index, column in enumerate(row):
                if (column_index + 1) % 9 != 0:
                    if (column_index + 1) != 9 and (column_index + 1) % 3 == 0:
                        print(column, end=" | ")
                    else:
                        if (column_index + 1) % 9 == 1:
                            print(row_index + 1, end="|")
                            print(column, end=" ")
                        else:
                            print(column, end=" ")
                else:
                    print(column, end="\n")
                    if (row_index + 1) % 3 == 0:
                        print(' ', '-' * 21)

    def get_grid(self):
        return self._game_grid

    def compare_with(self, grid):
        if self._game_grid == grid.get_grid():
            return True
        else:
            return False

    def place_number(self):
        coordinates = self.find_empty_cell()
        if coordinates is False:
            return True
        else:
            for number in coordinates[1].get_available():
                if self.check_valid(number, coordinates[0]):
                    coordinates[1].set_chosen(number)
                    self.remove_available(number, coordinates[0])

                    if self.place_number():
                        return True

                    self._game_grid[coordinates[0][0]][coordinates[0][1]].set_chosen(' ')
            return False


    def find_empty_cell(self):
        empty_coordinates = []
        for row_index, row in enumerate(self._game_grid):
            for column_index, cell in enumerate(row):
                if cell.get_chosen() == ' ':
                    coordinates = (row_index, column_index)
                    empty_coordinates.append([coordinates, cell])

        if len(empty_coordinates) == 0:
            return False
        else:
            lowest_available = 10
            lowest_available_coordinates = (0, 0)
            for cell in empty_coordinates:
                if cell[1].get_length_available() < lowest_available:
                    lowest_available = cell[1].get_length_available()
                    lowest_available_coordinates = cell
            return lowest_available_coordinates

    def check_valid(self, number, coordinates):
        return self.check_row(number, coordinates) and self.check_column(number, coordinates) and \
               self.check_3x3(number, coordinates)

    def check_row(self, number, coordinates):
        for i in range(len(self._game_grid)):
            cell_number = self._game_grid[coordinates[0]][i].get_chosen()
            if cell_number == number and i != coordinates[1]:
                return False
        return True

    def check_column(self, number, coordinates):
        for i in range(len(self._game_grid)):
            cell_number = self._game_grid[i][coordinates[1]].get_chosen()
            if cell_number == number and i != coordinates[0]:
                return False
        return True

    def check_3x3(self, number, coordinates):
        start_row = (coordinates[0] // 3) * 3
        start_column = (coordinates[1] // 3) * 3
        end_row = start_row + 3
        end_column = start_column + 3

        for row in range(start_row, end_row):
            for column in range(start_column, end_column):
                cell_number = self._game_grid[row][column].get_chosen()
                if cell_number == number and row != coordinates[0] and column != coordinates[1]:
                    return False
        return True

    def remove_available(self, number, coordinates):
        return self.check_row(number, coordinates) and self.check_column(number, coordinates) and \
               self.check_3x3(number, coordinates)

    def remove_available_row(self, number, coordinates):
        for i in range(len(self._game_grid)):
            self._game_grid[coordinates[0]][i].get_available(number)

    def remove_available_column(self, number, coordinates):
        for i in range(len(self._game_grid)):
            self._game_grid[i][coordinates[1]].remove_available(number)

    def remove_available_3x3(self, number, coordinates):
        start_row = (coordinates[0] // 3) * 3
        start_column = (coordinates[1] // 3) * 3
        end_row = start_row + 3
        end_column = start_column + 3

        for row in range(start_row, end_row + 1):
            for column in range(start_column, end_column + 1):
                self._game_grid[row][column].remove_available(number)

