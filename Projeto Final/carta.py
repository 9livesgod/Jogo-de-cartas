import pygame
import pygwidgets


class Carta:
    BACK_IMAGE = pygame.image.load('assets/images/BackOfCard.png')

    def __init__(self, window, numero, naipe, value):
        self.window = window
        self.numero = numero
        self.naipe = naipe
        self.nome_carta = f'{numero} de {naipe}'
        self.value = value
        front_image_path = f'assets/images/{self.nome_carta}.png'
        self.images = pygwidgets.ImageCollection(window, (0, 0),
                                                 {'front': front_image_path, 'back': self.BACK_IMAGE}, 'back')

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def get_name(self):
        return self.nome_carta

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.naipe

    def get_rank(self):
        return self.numero

    def set_loc(self, loc):
        self.images.setLoc(loc)

    def get_loc(self):
        return self.images.getLoc()

    def draw(self):
        self.images.draw()
