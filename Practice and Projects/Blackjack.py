'''
Plan:
1. Select a buy in amount
2. Create a deck of cards with designated value attributes ✓
3. Shuffle the cards 
4. Deal a card facedown for the dealer and faceup for the player
5. Deal a second card to the player and reveal the dealer's second card
6. Player decides whether to stay or hit - n number of times
7. Once player decides to stay, dealer reveals original card
8. If dealer total <= 16, dealer has to hit and stay if total >= 17
9. If the dealer gets a blackjack, the player automatically loses unless they have a Blackjack themselves in which case they get back their original bet amount
10. You get your original bet amount back in the case of a draw
11. If the dealer busts, all remaining hands that are 21 or lower win their bet
11. A winning hand gets paid in a 1:1 ratio and a blackjack hand gets paid in a 3:2 ratio
12. Return all cards, shuffle and start a new round
'''

import random
suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
ranks = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':[1,11]}

class Cards:
    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = ranks.get(rank)
    
    def __repr__(self):
        return f'{self.rank} Of {self.suit}'

class Deck:
    def deck(self):
        self.cards = [Cards(rank,suit) for rank in ranks for suit in suits]
        return self.cards
    
    def deal(self):
        self.deck()
        random.shuffle(self.cards)
        return self.cards[-1]

    def __len__(self):
        return len(self.cards)

class Game:
    def __init__(self,bet_amount):
        self.player_cards = []
        self.dealer_cards = []
        self.bet_amount = bet_amount
    
    def dealer_points(self,hand):
        dealer_points = 0
        for card in hand:
            if card.value == [1,11]:
                continue
            dealer_points += card.value
        for card in hand:
            if card.value == [1,11]:
                if dealer_points + 11 > 16:
                    card.value = 1
                elif dealer_points <= 16 or dealer_points == 7:
                    card.value = 11
        return dealer_points
        
    def round(self):
        deck = Deck()

        # Dealer deals
        self.dealer_cards.append(deck.deal())
        self.player_cards.append(deck.deal())
        print(f'\nYou got dealt {self.player_cards[-1]}')
        input('Press enter to continue...')

        # Dealer deals second time
        self.dealer_cards.append(deck.deal())
        print(f"\nThe dealer's second card was {self.dealer_cards[-1]}")
        self.player_cards.append(deck.deal())
        print(f'You got dealt {self.player_cards[-1]}')

        # Player stay or hit loop
        while True:
            choice = input('\nWould you like to stay or hit? (Enter s or h) ')
            if choice == 'h':
                self.player_cards.append(deck.deal())
                print(f'\nYou got dealt {self.player_cards[-1]}')
            elif choice not in ['s','h']:
                print('Please select between s and h.')
                continue
            else:
                break
        
        # Tally up player points
        player_points = 0
        for card in self.player_cards:
            if card.value == [1,11]:
                card.value = 1 if player_points + 11 > 21 else 11
            player_points += card.value
        
        if player_points > 21:
            print('\nBust! You lose.')
            self.bet_amount = 0
        
        if player_points <= 21:
            # Reveal original dealer card and calcualte dealer points
            print(f"\nThe dealer's original card was {self.dealer_cards[0]}\n")
            self.dealer_points(self.dealer_cards)

            if ('Ace' in [self.suit for self.suit in self.dealer_cards] and self.dealer_points(self.dealer_cards) == 17):
                self.dealer_cards.append(deck.deal())
                print(f"The dealer hit and their card was {self.dealer_cards[-1]}")
                self.dealer_points(self.dealer_cards)
            
            while self.dealer_points(self.dealer_cards) <= 16:
                self.dealer_cards.append(deck.deal())
                print(f"The dealer hit and their card was {self.dealer_cards[-1]}")
                self.dealer_points(self.dealer_cards)

            if self.dealer_points(self.dealer_cards) == 21:
                if player_points == 21:
                    print('\nYour hand is a push')
                else: 
                    print('\nThe dealer got BlackJack. You lose.')
                    self.bet_amount = 0
            
            if player_points > self.dealer_points(self.dealer_cards):
                if player_points == 21:
                    print('\nBlackJack! You win!')
                    self.bet_amount += round((3/2)*self.bet_amount)
                else:
                    print('\nYou win!')
                    self.bet_amount *= 2

            if player_points < self.dealer_points(self.dealer_cards):
                if self.dealer_points(self.dealer_cards) <= 21:
                    print('\nYou lose.')
                    self.bet_amount = 0
                elif player_points == 21:
                    print('\nBlackJack! You win!')
                    self.bet_amount += round((3/2)*self.bet_amount)
                else:
                    print('\nYou win!')
                    self.bet_amount *= 2

            if player_points == self.dealer_points(self.dealer_cards):
                print("\nIt's a tie and your hand is a push.")

def bet(n):
    bet_amount = 0
    while True:
        if bet_amount <= n:
            try:
                bet_amount = int(input('Select a bet amount: '))
                return bet_amount
            except ValueError:
                print('Please enter an integer.')
        else:
            print('Your bet cannot exceed your buy-in amount.')

def game_on_func():
    while True:
        game_on = input('\nWould you like to continue playing? (y / n) ').lower()
        while game_on in ['y','n']:
            return game_on == 'y'
        print('Please enter between Y or N.')

game_on = True

print(f'''--------------------------------------------------------------------------------------------------------------
{'Welcome to BlackJack':^110}
--------------------------------------------------------------------------------------------------------------''')
while True:
    try:
        buy_in = int(input('Select a buy in amount: '))
        break
    except ValueError:
        print('Please enter an integer.')

while game_on:

    bet_amount = bet(buy_in)
    g = Game(bet_amount)
    buy_in -= bet_amount

    g.round()

    buy_in += g.bet_amount
    print(f"\nYour current balance is {buy_in}.")

    if buy_in <= 0:
        print("\nYou do not any avaible chips.")

    game_on = game_on_func()
    
    print('--------------------------------------------------------------------------------------------------------------')

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(f"\n{'Thank you for playing':^62}\n{logo}")

