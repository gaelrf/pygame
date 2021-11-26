import pygame.draw


class EnemigoBasico:

    def __init__(self, juego, x, y):
        self.x = x
        self.juego = juego
        self.y = y
        self.tamaño = 30

    def aparecer(self):
        pygame.draw.rect(self.juego.pantalla,
                         (81,43,88),
                         pygame.Rect(self.x, self.y, self.tamaño, self.tamaño))
        self.y += 0.5

    def colision(self, juego):

        for disparo in juego.disparos:

            if (disparo.x < self.x + self.tamaño and
                disparo.x > self.x - self.tamaño and
                disparo.y < self.y + self.tamaño and
                disparo.y > self.y - self.tamaño):
                juego.disparos.remove(disparo)
                juego.enemigos.remove(self)