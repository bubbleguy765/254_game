import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.value == 11:
            display_rank = 'Ace'
        elif self.value == 10:
            display_rank = random.choice(['Ten', 'Jack', 'Queen', 'King'])
        else:
            display_rank = str(self.value)
        
        return f"{display_rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.deck = []
        self.reset()
    
    def reset(self):
        self.deck = []
        suits = ["Hearts", 'Diamonds', 'Clubs', 'Spades']
        card_values = [11] * 4 + [10] * 16 + [9] * 4 + [8] * 4 + [7] * 4 + [6] * 4 + [5] * 4 + [4] * 4 + [3] * 4 + [2] * 4
        
        for suit in suits:
            for value in card_values:
                self.deck.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        if self.deck:
            return self.deck.pop()
        return None

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        
        if card.value == 11:
            self.aces += 1
    
    def get_value(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10 
            self.aces -= 1
        return self.value
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

def play(deck):
    player_hand = Hand()
    dealer_hand = Hand()

    for _ in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    print("\n new round:  ")
    print(f"Dealer  : {dealer_hand.cards[0]}")
    print(f"ur hand: {player_hand} (Value: {player_hand.get_value()})")

    while player_hand.get_value() < 21:
        action = input("h or s (hit or stand)? ").lower()
        
        if action == 'h':
            new_card = deck.deal()
            player_hand.add_card(new_card)
            print(f"You drew a {new_card}.")
            print(f"Your Hand: {player_hand} (Value: {player_hand.get_value()})")
            
            if player_hand.get_value() > 21:
                print("You busted.")
                return 'lose'
        elif action == 's':
            print("You stand.")
            break 

    player_final_value = player_hand.get_value()
    if player_final_value <= 21:
        print("\nDEALERS TURN........")
        print(f"Dealer's full hand: {dealer_hand} (Value: {dealer_hand.get_value()})")

        while dealer_hand.get_value() < 17:
            new_card = deck.deal()
            dealer_hand.add_card(new_card)
            print(f"dealer draws {new_card}.")
            print(f"dealer's Hand: {dealer_hand} (Value: {dealer_hand.get_value()})")

        dealer_final = dealer_hand.get_value()

        if dealer_final > 21:
            print("omg u won bc dealer busted")
            return 'win'
        
        print(f"Dealer stands {dealer_final}.")

        if player_final_value > dealer_final:
            print("you WIN!!")
            return 'win'
        elif player_final_value < dealer_final:
            print("you lost :(")
            return 'lose'
        else:
            print("Tie - both equal")
            return 'push'
    
    return 'lose'

def main():
    player_wins = 0
    player_losses = 0
    
    print("Hello and welcome to Blackjack.")

    while True:
        game_deck = Deck()
        game_deck.shuffle()

        result = play(game_deck)

        if result == 'win':
            player_wins = player_wins + 1
        elif result == 'lose':
            player_losses = player_losses + 1

        print("\nSCORE:")
        print(f"Wins: {player_wins}")
        print(f"Losses: {player_losses}")
        
        play_again = input("\nPlay again (y/n)? ").lower()
        if play_again not in ['y', 'yes']:
            print("\nheres ur W and L data")
            print(f"Wins: {player_wins}, Losses: {player_losses}")
            break

if __name__ == "__main__":
    main()
