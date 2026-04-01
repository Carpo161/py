import random

suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:

    def __init__(self,suit,rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = ranks.index(rank.capitalize())
    
    def __gt__(self,other):
        return self.value > other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def __eq__(self,other):
        return self.value == other.value

    def __str__(self):
        return f'{self.rank} Of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in suits for rank in ranks]
    
    def deck(self):
        card_list = [str(card) for card in self.cards]
        return card_list
    
    def deal(self):
        hand = random.sample(self.cards, 26)
        for i in hand:
            self.cards.remove(i)
        return hand

class Player:
    def __init__(self,name,deck):
        self.name = name
        self.deck = deck
    
    def remove_card(self,middle):
        if len(self.deck) == 0:
            return
        middle.append(self.deck.pop(random.randint(0,len(self.deck)-1)))
        return f'{self.name} placed: \n{middle[-1]}'
    
    def add_card(self,middle):
        print(f"{self.name} won the round and collected: {", ".join(str(c) for c in middle)}")
        self.deck.extend(middle)
        middle.clear()
    
    def __str__(self):
        str_hand = ", ".join(str(c) for c in self.deck)
        return f'The current deck is {str_hand}'
    
    def __len__(self):
        return len(self.deck)

class Game:
    def __init__(self):
        self.middle = []
        deck = Deck()
        self.p1 = Player('Player 1', deck.deal())
        self.p2 = Player('Player 2', deck.deal())
    
    def round(self):
        self.p1.remove_card(self.middle)
        self.p2.remove_card(self.middle)
        if self.middle[-2] > self.middle[-1]:
            self.p1.add_card(self.middle)
        elif self.middle[-2] < self.middle[-1]:
            self.p2.add_card(self.middle)
        elif self.middle[-2] == self.middle[-1]:
            print("It's a Draw. 5 cards will be placed.")
            for _ in range(5):
                if len(self.p1) == 0 or len(self.p2) == 0:
                    break
                self.p1.remove_card(self.middle)
                self.p2.remove_card(self.middle)
            if self.middle[-2] > self.middle[-1]:
                self.p1.add_card(self.middle)
            elif self.middle[-2] < self.middle[-1]:
                self.p2.add_card(self.middle)
            else:
                if len(self.p1) > len(self.p2):
                    self.p1.add_card(self.middle)
                else:
                    self.p2.add_card(self.middle)
    
    def end(self):
        if len(self.p1) == 0:
            return 'Game Over! Player 2 wins.'
        elif len(self.p2) == 0:
            return 'Game Over! Player 1 wins.'

game = Game()
rounds = 0

while True:
    game.round()
    rounds += 1
    result = game.end()
    if result:
        print(f'{result} It took {rounds} rounds.')
        break