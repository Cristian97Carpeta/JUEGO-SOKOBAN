import pygame
from paredes import Cubo

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode
([ANCHO,ALTO])

jugando = True
cubo = Cubo(100,100)

while jugando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    cubo.dibujar(VENTANA)
    pygame.display.update()

quit()

