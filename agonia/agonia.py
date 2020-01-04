

from itertools import cycle
from player import Player
from deck import Deck

class Agonia:
    def __init__(self,players):
        #self.deck = Deck()
        self.playersLst = []
        for name in players:
            self.playersLst.append(Player(name))
        self.players = cycle(self.playersLst)
        self.rounds = 0
    def run(self):
        while(True):
            print('New round!')
            self.rounds += 1
            self.deck = Deck()
            for p in self.playersLst:
                self.deck.deal_cards(p)
            while(True):
                p = next(self.players)
                print('Deck has ' + str(len(self.deck.opened)) + ' cards and top card: ',end='')
                print(self.deck.top_card())
                p.display()
                p.play(self.deck)
                if len(p.cards) == 0:
                    if self.on_round_end():
                        return  #exit
                    break #start another round
                if self.deck.top_card().num == '9': 
                    p = next(self.players) #skip player
    def on_round_end(self):
        """returns if the game ended"""
        for p in self.playersLst:
            p.on_round_end()
            if p.points > 50:
                return self.on_game_end()
        return False
    def on_game_end(self):
        """returns if the game ended if not (we may have a draw)"""
        self.playersLst.sort(key=lambda x:x.points)
        winner = self.playersLst[0]
        if winner == self.playersLst[1]: #we have a draw
            #limit the players to the 2 winners and prepare for another round.
            #TODO: maybe there are more winners.
            secondWinner = self.playersLst[1]
            self.playersLst = [winner,secondWinner]
            self.players = cycle(self.playersLst)
            return False
        print('Player ' + winner.name + ' won the game after ' + str(self.rounds) + ' rounds') 
        return True


if __name__ == '__main__':
    players = []
    """"while(True):
        name = input('Give player name or \'END\'  if no more players will play.')
        if name == 'END':
            break
        players.append(name)
    """
    players.append('loukas')
    players.append('pretty_girl')
    agonia = Agonia(players)
    agonia.run()