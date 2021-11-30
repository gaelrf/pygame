import pygame

import disparoJugador
import generador
import jugador


class Juego:
    pantalla = None
    enemigos = []
    disparos = []
    prededor = False

    def __init__(self,ancho,alto):
        pygame.init()
        self.ancho = ancho
        self.alto = alto
        self.pantalla = pygame.display.set_mode(( ancho, alto))
        self.reloj = pygame.time.Clock()
        terminado = False

        jugar = jugador.Jugador(self, ancho / 2, alto - 20)
        generar = generador.Generador(self)
        disparo = None
        while not terminado:

            pulsar = pygame.key.get_pressed()
            if pulsar[pygame.K_LEFT]:
                jugador.Jugador.x -= 2 if jugador.Jugador.x > 20 else 0
            if pulsar[pygame.K_RIGHT]:
                jugador.Jugador.x += 2 if jugador.Jugador.x < ancho-20 else 0
            if len(self.enemigos) == 0:
                self.displayText("VICTORY ACHIEVED")
            for evento in pygame.event.get():
                if evento.type == pygame.quit():
                    hecho = True
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and not self.prededor:
                    self.disparos.append(disparoJugador.DisparoJugador(self,jugador.Jugador.x,jugador.Jugador.y))
            for alien in self.enemigos:
                alien.colision(self)
                if (alien.y > alto):
                    self.lost = True
                    self.displayText("YOU DIED")

            for disparo in self.disparos:
                disparo.draw()

            if not self.prededor:
                jugar.aparecer()
        pygame.display.flip()
        self.reloj.tick(60)
        self.pantalla.fill(0,0,0)

    def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.pantalla.blit(textsurface, (110, 160))


