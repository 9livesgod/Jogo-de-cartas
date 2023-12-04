import random
from carta import *


class Deck:
    NAIPE_TUPLE = ('Ouros', 'Paus', 'Copas', 'Espadas')
    NUMERO_VALORES_DICT = {'Ás': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                       '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                       'Valete': 11, 'Rainha': 12, 'Rei': 13}

    def __init__(self, window):
        self.deck_inicial = []
        self.deck_atual = []
        for naipe in self.NAIPE_TUPLE:
            for numero, value in self.NUMERO_VALORES_DICT.items():
                carta = Carta(window, numero, naipe, value)
                self.deck_inicial.append(carta)
        self.embaralhar()

    def embaralhar(self):
        self.deck_atual = self.deck_inicial.copy()
        for carta in self.deck_atual:
            carta.conceal()
        random.shuffle(self.deck_atual)

    def get_carta(self):
        return self.deck_atual.pop()

    def add_carta(self, card):
        self.deck_atual.insert(0, card)