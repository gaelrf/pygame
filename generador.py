import enemigoBasico


class Generador:

    def __init__(self,juego):
        margen = 30
        ancho = 50

        for x in range(margen, juego.ancho - margen, ancho):
            for y in range(margen, int (juego.alto/2), ancho):
                juego.enemigos.append(enemigoBasico.EnemigoBasico(juego, x, y))