import pygame  # Importamos la biblioteca pygame para crear el juego
import sys  # Importamos sys para manejar la salida del programa

# Inicializamos pygame
pygame.init()

# Definimos los elementos del juego
PARED = 3
PISO = 4
JUGADOR = 0
CAJA = 1
META = 2
JUGADOR_META = 5
CAJA_META = 6

# Creamos el nivel basado en el diseño que se tiene en el archivo "niveles.txt"

nivel = [
    [PARED, PARED, PARED, PARED, PISO, PISO, PISO, PISO, PISO, PISO], 
    [PARED, PISO, PISO, PARED, PARED, PARED, PISO, PISO, PISO, PISO],
    [PARED, PISO, PISO, PISO, PISO, PARED, PISO, PISO, PISO, PISO],
    [PARED, PISO, CAJA, PISO, PISO, PARED, PISO, PISO, PISO, PISO],
    [PARED, PARED, PARED, PISO, PARED, PARED, PARED, PISO, PISO, PISO],
    [PISO, PISO, PARED, PISO, PISO, PISO, PARED, PISO, PISO, PISO],
    [PARED, PISO, CAJA, PISO, CAJA, PISO, PARED, PISO, PISO, PISO],
    [PARED, PISO, PISO, META, META, JUGADOR, META, META, PISO, PISO],
    [PARED, PISO, PISO, PISO, CAJA, PISO, PISO, PISO, PISO, PISO],
    [PARED, PARED, PARED, PISO, PISO, PARED, PARED, PISO, PISO, PISO],
    [PISO, PISO, PISO, PARED, PARED, PISO, PISO, PISO, PISO, PISO]
]

# Configuramos la pantalla

ANCHO = 400  # Ancho de la ventana del juego
ALTO = 440  # Alto de la ventana del juego
TAMANO_CELDA = 40  # Tamaño de cada celda en el juego
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Creamos la ventana del juego
pygame.display.set_caption('Sokoban')  # Título de la ventana del juego

# Colores

NEGRO = (0, 0, 0)  # Color negro
BLANCO = (255, 255, 255)  # Color blanco
ROJO = (255, 0, 0)  # Color rojo
VERDE = (0, 255, 0)  # Color verde
AZUL = (0, 0, 255)  # Color azul
GRIS = (200, 200, 200)  # Color gris

# Función para dibujar el nivel

def dibujar_nivel(nivel):
    VENTANA.fill(NEGRO)  # Rellenamos la ventana con color negro
    for i, fila in enumerate(nivel):  # Recorremos cada fila del nivel
        for j, elemento in enumerate(fila):  # Recorremos cada elemento de la fila
            x = j * TAMANO_CELDA  # Calculamos la posición x
            y = i * TAMANO_CELDA  # Calculamos la posición y
            if elemento == PARED:
                pygame.draw.rect(VENTANA, GRIS, (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujamos una pared
            elif elemento == PISO:
                pygame.draw.rect(VENTANA, NEGRO, (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujamos el piso
            elif elemento == JUGADOR:
                pygame.draw.rect(VENTANA, AZUL, (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujamos al jugador
            elif elemento == CAJA:
                pygame.draw.rect(VENTANA, ROJO, (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujamos una caja
            elif elemento == META:
                pygame.draw.rect(VENTANA, VERDE, (x, y, TAMANO_CELDA, TAMANO_CELDA))  # Dibujamos una meta
    pygame.display.flip()  # Actualizamos la pantalla

# Función para encontrar la posición del jugador

def encontrar_jugador(nivel):
    for i, fila in enumerate(nivel):  # Recorremos cada fila del nivel
        for j, elemento in enumerate(fila):  # Recorremos cada elemento de la fila
            if elemento == JUGADOR:
                return i, j  # Devolvemos la posición del jugador
    return None

# Función para mover al jugador

def mover_jugador(nivel, direccion):
    i, j = encontrar_jugador(nivel)  # Encontramos la posición actual del jugador
    if direccion == 'w' and nivel[i-1][j] in (PISO, META):
        nivel[i][j], nivel[i-1][j] = PISO, JUGADOR  # Movemos al jugador hacia arriba
    elif direccion == 's' and nivel[i+1][j] in (PISO, META):
        nivel[i][j], nivel[i+1][j] = PISO, JUGADOR  # Movemos al jugador hacia abajo
    elif direccion == 'a' and nivel[i][j-1] in (PISO, META):
        nivel[i][j], nivel[i][j-1] = PISO, JUGADOR  # Movemos al jugador hacia la izquierda
    elif direccion == 'd' and nivel[i][j+1] in (PISO, META):
        nivel[i][j], nivel[i][j+1] = PISO, JUGADOR  # Movemos al jugador hacia la derecha

# Bucle principal del juego

jugando = True
while jugando:
    eventos = pygame.event.get()  # Obtenemos todos los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False  # Salimos del bucle si se cierra la ventana
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                mover_jugador(nivel, 'w')  # Movemos al jugador hacia arriba
            elif evento.key == pygame.K_s:
                mover_jugador(nivel, 's')  # Movemos al jugador hacia abajo
            elif evento.key == pygame.K_a:
                mover_jugador(nivel, 'a')  # Movemos al jugador hacia la izquierda
            elif evento.key == pygame.K_d:
                mover_jugador(nivel, 'd')  # Movemos al jugador hacia la derecha
    
    dibujar_nivel(nivel)  # Dibujamos el nivel

pygame.quit()  # Cerramos pygame
sys.exit()  # Salimos del programa

