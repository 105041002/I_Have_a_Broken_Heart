# -*- coding: utf-8 -*-
def init_all_cards():
    suits = '♣♦♠♥'
    numbers = list(range(1, 14))
    return ["{0}{1}".format(suit, number) for suit, number in product(suits, numbers)]

def get_legal_moves(cards_you_have, cards_played, heart_broken=False):
    legal_moves=[]
    if cards_played:
        star=cards_played[0]
        first=star[0]
        for card in cards_you_have:
            if card[0]==first:
                 legal_moves.append(card)
        if legal_moves:
            return legal_moves
        else :
            return cards_you_have
    else:
        if '♣2' in cards_you_have:
            return '♣2'
        else:
            if heart_broken:
                return cards_you_have
            else:
                for card in cards_you_have:
                    if not card.startswith('♥'):
                        legal_moves.append(card)
            if legal_moves:
                return legal_moves
            else:
                return cards_you_have

class Agent:
    def __init__(self, id):
        self.id = id

    def play(self, cards_you_have, cards_played, heart_broken, info):
        pass

    def pass_cards(self, cards):
        pass
