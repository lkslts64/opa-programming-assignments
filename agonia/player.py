#import deck
#from .deck import Deck
from deck import Deck
from deck import suits
import random

class Player:
    def __init__(self,name):
        self.cards = []
        self.points = 0
        self.name = name
    def sum_points_of_cards(self):
        card_points = [card.val for card in self.cards]
        return sum(card_points)
    def on_round_end(self):
        self.points += self.sum_points_of_cards()
        self.cards = [] #prepare cards for the next round
    def display(self):
        print('Player ' + self.name + ' has ' + str(self.points) + ' points and holds:')
        for c in self.cards:
            print(c,end='')
        print()
    def play(self,d):
        top = d.top_card()
        if top.num == '7':
            d.draw_card(self)
            d.draw_card(self)
        print('Player ' + self.name + ' played ',end='')
        for card in self.cards:
            if card.matches(top):
                self.cards.remove(card)
                #if we picked to play an ace, then choose the new suit of the top card at random.
                #The suit of the ace (i.e the `card` variable) will be the suit that the next player
                #should see as the current suit.
                #We dont choose the suit strategically yet.
                if card.num == 'A': 
                    card.suit = suits[random.randint(0,len(suits)-1)] 
                d.opened.append(card)
                print(card)
                if card.num == '8':
                    self.play(d)
                return
        #if we don't have any card, draw one
        d.draw_card(self)
        print('Pass')

