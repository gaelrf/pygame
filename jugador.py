import pygame.draw


class Jugador:
    def __init__(self, juego, x, y):
        self.juego = juego
        self.x = x
        self.y = y

    def aparecer(self):
        pygame.draw.rect(self.juego.pantalla,
                         (210, 250,251),
                         pygame.Rect(self.x, self.y, 10, 5))
