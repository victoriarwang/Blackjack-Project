class User:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, card):
        self.hand.append(card)

    def score(self):
        card_values = [card.value for card in self.hand]
        total_score = sum(card_values)
        for i in range(card_values.count(11)):
            if total_score > 21:
                total_score -= 10
        return total_score

    def formatted_hand(self):
        return ' '.join([card.character for card in self.hand])