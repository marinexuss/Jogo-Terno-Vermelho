import random

class Deck:
    def __init__(self):
        naipes = ['♥️', '♦️', '♣️', '♠️']
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cartas = [f"{valor}{naipe}" for naipe in naipes for valor in valores] * 2
        random.shuffle(self.cartas)

    def distribuir_cartas(self, num_jogadores):
        return [self.cartas[i*15:(i+1)*15] for i in range(num_jogadores)]
