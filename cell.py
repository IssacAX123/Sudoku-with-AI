class Cell:
    def __init__(self, row, column):
        self.__available = [str(i) for i in range(1, 10)]
        self.__chosen = ' '
        self.__row = row
        self.__column = column

    def get_length_available(self):
        return len(self.__available)

    def get_available(self):
        return self.__available

    def set_chosen(self, number):
        self.__chosen = number

    def get_chosen(self):
        return self.__chosen
    
    def remove_available(self, number):
        if number in self.__available:
            self.__available.remove(number)

    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def __str__(self):
        return self.__chosen
