import random

#lowkey forgot python :(

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.deck = []
        self.reset()
    
    def reset(self):
        self.deck = []
        suits = ["Hearts",'Diamonds','Clubs','Spades']
        ranks = ['two', 'three', 'four,' 'five', 'six', 'seven,' 'eight',' nine', 'ten','jack','queen','king','ace']
        values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values[rank]))
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        if self.deck:
            return self.deck.pop()
        return None


class Person:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.wins = 0

    def add_card(self, card):
        self.hand.add_card(card)

    def get_val(self):
        return self.hand.get_value()
    

class Player(Person):
    def move(self):
        while True:
            action = input(f"\n{self.name}, hit or stand ")
            return action
        
class Dealer(Person):
    def __init__(self):
        super().__init__("dealer")

    def should_hit(self):
        return self.get_hand_value() < 17
    

class game:
    def __init__(self):
        self.deck, self.dealer, self.players = Deck(), Dealer(), []

        #idk adding more ppl to the game

#    def _deal_init_cards(self):
 #       self.deck.shufle()
  ##         for


  #struggling to add the logic for the game & 
  #what i can think
    #first start and print everything & get names, then deal the 2 cards
    #then display hands, then not really sure