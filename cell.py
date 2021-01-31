from random import randint

class Cell:
    def __init__(self):
        self.__available = [i for i in range(1,10)]
        self.__chosen = 0

    def get_length(self):
        return len(self.__available)

    def set_chosen(self):
        self.__chosen = self.__available[randint(0, len(self.__available)-1)]
    
    def get_chosen(self):
        return self.__chosen
    
    def remove_available(self, number):
        if number in self.__available:
            self.__available.remove(number)
        else:
            print('number not in list')
        