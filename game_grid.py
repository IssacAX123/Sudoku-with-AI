from grid import Grid


class GameGrid(Grid):
    def __init__(self):
        super().__init__()

    def generate_filler(self, difficulty):
        if difficulty == 'easy':
            filler_range =(37, 41)
        elif difficulty == 'medium':
            filler_range = (32, 36)
        elif difficulty == 'hard':
            filler_range = (27, 31)




