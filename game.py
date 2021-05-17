import sys
from deck import Deck
from user import User

class Game:
    def __init__(self):
        self.dealer = User("Dealer")
        self.player = User("Player")
        self.deck = Deck()
        self.winner = None
        self.loser = None

        self.start()

    def start(self):
        self.dealer.draw(self.deck.deal())
        self.dealer.draw(self.deck.deal())
        self.player.draw(self.deck.deal())
        self.player.draw(self.deck.deal())

    def play(self):
        self.print_hands()
        while not self.turn_over(self.player, self.dealer):
            user_input = input("Would you like to (H)it or (S)tand? ")
            if user_input == "H":
                self.player.draw(self.deck.deal())
            elif user_input == "S":
                break
            if not self.turn_over(self.player, self.dealer):
              self.print_hands()

        if not self.game_over():
            print("\nPlayer stands with", self.player.formatted_hand(), "=", self.player.score())
            print("\nDealer has:", self.dealer.formatted_hand(), "=", self.dealer.score())
            while self.dealer.score() < 17 or self.dealer.score() <= self.player.score():
              print("Dealer hits")
              self.dealer.draw(self.deck.deal())
              print("Dealer has:", self.dealer.formatted_hand(), "=", self.dealer.score())
              if self.turn_over(self.dealer, self.player):
                break
            
            if not self.game_over() and not self.dealer.score() == 21:
              print("Dealer stands")
            if self.dealer.score() > self.player.score() and self.dealer.score() <= 21:
              self.winner = self.dealer
              self.loser = self.player
            else: 
              self.winner = self.player
              self.loser = self.loser

        if self.winner.score() == 21:
            print("Blackjack!")
            print("\n{} wins!".format(self.winner.name))
        elif self.loser.score() > 21:
            print("\n" + self.loser.name, "has:", self.loser.formatted_hand(), "=", self.loser.score())
            print(self.loser.name, "busts with", self.loser.score())
            print("\n{} wins!".format(self.winner.name))
        else:
            print("\n{} wins!".format(self.winner.name))
            print("{} = {} to {}'s {} = {}".format(
                self.winner.formatted_hand(),
                self.winner.score(),
                self.loser.name,
                self.loser.formatted_hand(),
                self.loser.score())
            )

    def print_hands(self):
        print("\nDealer has:", self.dealer.hand[0].character, "? = ?")
        print("Player has:", self.player.formatted_hand(), "=", self.player.score())

    def turn_over(self, currUser, nextUser):
        if currUser.score() == 21:
          self.winner = currUser
          self.loser = nextUser
          return True
        elif currUser.score() > 21:
          self.winner = nextUser
          self.loser = currUser
          return True
        return False
    
    def game_over(self): 
      return self.winner != None and self.loser != None
 
def test_card_init_creates_a_new_card():
    card = Card(1)
    assert 'A' == card.character
    assert 11 == card.value

def test_deck_init_creates_a_randomly_shuffled_deck_of_cards():
    deck = Deck()
    assert 52 == len(deck.cards)

def test_deck_deal_removes_a_card_from_deck():
    deck = Deck()
    deck.deal()
    assert 51 == len(deck.cards)

if __name__ == "__main__":
    deck = Deck()

    # import pdb; pdb.set_trace()
    args = sys.argv[1] if len(sys.argv) > 1 else None
    if args == "--test":
        test_card_init_creates_a_new_card()
        test_deck_init_creates_a_randomly_shuffled_deck_of_cards()
        test_deck_deal_removes_a_card_from_deck()
    else:
      new_game = Game()
      new_game.play()