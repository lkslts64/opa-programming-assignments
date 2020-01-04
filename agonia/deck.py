import random 
import sys

suits = ['\u2665','\u2660','\u2666','\u2663']

class Deck:
    heart = '\u2665'
    spade = '\u2660'
    diamond = '\u2666'
    club = '\u2663'
    def __init__(self):
        """creates a deck by creating 52 new Card instances"""
        self.opened = []
        #self.topCard = None
        self.closed = []
        for suit in suits:
            for i in range(2,11):
                self.closed.append(Card(str(i),suit,i))
            self.closed.append(Card(str('J'),suit,10))
            self.closed.append(Card(str('Q'),suit,10))
            self.closed.append(Card(str('K'),suit,10))
            self.closed.append(Card(str('A'),suit,11))
        self.shuffle_closed()
        #at start we need to put one card at the opend ones
        self.opened.append(self.closed.pop())
    def shuffle_closed(self):
        random.shuffle(self.closed)
    def draw_card(self,player):
        if len(self.closed) == 0:
            if len(self.opened) == 0:
                sys.exit("draw_card: opened and closed cards are empty.Propably all cards are in players hands.The game will abnormally end.") 
            #make the opened ones closed
            self.closed = self.opened[:-1]
            self.opened = [self.opened[-1]]
        #give a card to the player from the closed ones.
        self.deal_card(player)
    def top_card(self):
        return self.opened[-1]
    def deal_card(self,player):
        player.cards.append(self.closed.pop())
    def deal_cards(self,player):
        for _ in range(7):
            self.deal_card(player)


        




class Card:
    def __init__(self,num,suit,val):
        self.num = num
        self.suit = suit
        self.val = val
        self.t = (num,suit,val)
    def display(self):
        print((self.num,self.suit))
    def __str__(self):
        return self.num + self.suit
    def matches(self,card):
        return self.suit == card.suit or self.num == card.num or self.num == 'A'
    