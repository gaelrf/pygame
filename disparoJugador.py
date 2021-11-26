import pygame.draw


class DisparoJugador:

    def __init__(self, juego, x, y):
        self.juego = juego
        self.x = x
        self.y = y

    def aparecer(self):
        pygame.draw.rect(self.juego.pantalla,
                         (254,52,110),
                         pygame.Rect(self.x, self.y, 2, 4))
        self.y -=2