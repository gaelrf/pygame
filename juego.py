import pygame


class Juego:
    pantalla = None
    enemigos = []
    disparos = []
    prededor = False

    def __init__(self,ancho,alto):
        pygame.init()
        self.ancho = ancho
        self.alto = alto
        self.pantalla = pygame.display.set_mode((ancho,alto))
        self.reloj = pygame.time.Clock()
        terminado = False

        while not terminado:

            if len(self.enemigos) == 0:
                self
            for event in pygame.event.get():
                if event.type == pygame.quit():
                    hecho = True

        pygame.display.flip()
        self.reloj.tick(60)
        self.pantalla.fill(0,0,0)


