import pygame.draw


class EnemigoBasico:

    def __init__(self, juego, x, y):
        self.x = x
        self.juego = juego
        self.y = y
        self.tamano = 30

    def aparecer(self):
        pygame.draw.rect(self.juego.pantalla,(81,43,88),pygame.Rect(self.x, self.y, self.tamano, self.tamano))
        self.y += 0.5

    def colision(self, juego):

        for disparo in juego.disparos:

            if (disparo.x < self.x + self.tamano and
                disparo.x > self.x - self.tamano and
                disparo.y < self.y + self.tamano and
                disparo.y > self.y - self.tamano):
                juego.disparos.remove(disparo)
                juego.enemigos.remove(self)