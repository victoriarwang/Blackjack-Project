
# 
class Card:
    def __init__(self, number):
        self.value = Card.map_value(number)
        self.character = Card.map_character(number)

    @staticmethod
    def map_value(number):
        if number == 1:
            return 11
        elif number < 11:
            return number
        else:
            return 10

    @staticmethod
    def map_character(number):
        mappings = {}
        for i in range(2, 11):
            mappings[i] = str(i)

        mappings[1] = 'A'
        mappings[11] = 'J'
        mappings[12] = 'Q'
        mappings[13] = 'K'
        return mappings[number]