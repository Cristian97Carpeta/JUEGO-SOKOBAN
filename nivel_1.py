import pygame
import sys 

# Inicializar Pygame

pygame.init()

# Configuramos la pantalla

ANCHO = 400  # Ancho de la ventana del juego
ALTO = 440  # Alto de la ventana del juego
TAMANO_CELDA = 40  # Tamaño de cada celda en el juego
VENTANA = pygame.display.set_mode([ANCHO, ALTO])  # Creamos la ventana del juego
pygame.display.set_caption('Sokoban')  # Título de la ventana del juego

# Definimos los colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255) 
VERDE = (0, 255, 0)

# Fuente del texto

fuente = pygame.font.Font(None, 74) 
fuente_pequena = pygame.font.Font(None, 36)

# Función para mostrar el menú principal

def mostrar_menu():
    menu = True
    while menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if ANCHO // 2 - 100 <= mouse_x <= ANCHO // 2 + 100 and ALTO // 2 - 75 <= mouse_y <= ALTO // 2 - 25:
                    menu = False  # Iniciar juego
                elif ANCHO // 2 - 100 <= mouse_x <= ANCHO // 2 + 100 and ALTO // 2 + 25 <= mouse_y <= ALTO // 2 + 75:
                    mostrar_instrucciones()
                elif ANCHO // 2 - 100 <= mouse_x <= ANCHO // 2 + 100 and ALTO // 2 + 125 <= mouse_y <= ALTO // 2 + 175:
                    pygame.quit()
                    sys.exit()
                    
        VENTANA.fill(NEGRO)
        titulo = fuente.render("Sokoban", True, VERDE)
        VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))
        
        jugar_texto = fuente_pequena.render("Jugar", True, BLANCO)
        instrucciones_texto = fuente_pequena.render("Instrucciones", True, BLANCO)
        salir_texto = fuente_pequena.render("Salir", True, BLANCO)
        
        pygame.draw.rect(VENTANA, VERDE, (ANCHO // 2 - 100, ALTO // 2 - 75, 200, 50))
        pygame.draw.rect(VENTANA, VERDE, (ANCHO // 2 - 100, ALTO // 2 + 25, 200, 50))
        pygame.draw.rect(VENTANA, VERDE, (ANCHO // 2 - 100, ALTO // 2 + 125, 200, 50))
        
        VENTANA.blit(jugar_texto, (ANCHO // 2 - jugar_texto.get_width() // 2, ALTO // 2 - 65))
        VENTANA.blit(instrucciones_texto, (ANCHO // 2 - instrucciones_texto.get_width() // 2, ALTO // 2 + 35))
        VENTANA.blit(salir_texto, (ANCHO // 2 - salir_texto.get_width() // 2, ALTO // 2 + 135))
        
        pygame.display.update()

# Función para mostrar las instrucciones
def mostrar_instrucciones():
    instrucciones = True
    while instrucciones:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    instrucciones = False
        
        VENTANA.fill(NEGRO)
        texto = fuente_pequena.render("Usa WASD para mover al jugador.", True, BLANCO)
        VENTANA.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - 50))
        texto2 = fuente_pequena.render("Presiona ESC para regresar.", True, BLANCO)
        VENTANA.blit(texto2, (ANCHO // 2 - texto2.get_width() // 2, ALTO // 2))
        
        pygame.display.update()

mostrar_menu()
        
# Variables iniciales

direccion_jugador = 'abajo'  # Dirección inicial del jugador

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
    [PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED], 
    [PARED, PISO, PISO, PARED, PARED, PARED, PISO, PISO, PISO, PARED],
    [PARED, PISO, PISO, PISO, PISO, PARED, PISO, PISO, PISO, PARED],
    [PARED, PISO, CAJA, PISO, PISO, PARED, PISO, PISO, PISO, PARED],
    [PARED, PARED, PARED, PISO, PARED, PARED, PARED, PISO, PISO, PARED],
    [PARED, PISO, PARED, PISO, PISO, PISO, PARED, PISO, PISO, PARED],
    [PARED, PISO, CAJA, PISO, CAJA, PISO, PARED, PISO, PISO, PARED],
    [PARED, PISO, PISO, META, META, JUGADOR, META, PISO, PISO, PARED],
    [PARED, PARED, PARED, PISO, PISO, PARED, PARED, PISO, PISO, PARED],
    [PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED, PARED]
]

# Cargar texturas

textura_pared = pygame.image.load('TEXTURAS/PARED.png')
textura_piso = pygame.image.load('TEXTURAS/PISO_1.png')
textura_jugador_arriba = pygame.image.load('TEXTURAS/JUGADOR_ARRIBA.png')
textura_jugador_abajo = pygame.image.load('TEXTURAS/JUGADOR_ABAJO.png')
textura_jugador_izquierda = pygame.image.load('TEXTURAS/JUGADOR_IZQUIERDA.png')
textura_jugador_derecha = pygame.image.load('TEXTURAS/JUGADOR_DERECHA.png')
textura_caja = pygame.image.load('TEXTURAS/CAJA_1.png')
textura_meta = pygame.image.load('TEXTURAS/META.png')

# Redimensionar texturas al tamaño de las celdas

textura_pared = pygame.transform.scale(textura_pared, (TAMANO_CELDA, TAMANO_CELDA))
textura_piso = pygame.transform.scale(textura_piso, (TAMANO_CELDA, TAMANO_CELDA))
textura_jugador_arriba = pygame.transform.scale(textura_jugador_arriba, (TAMANO_CELDA, TAMANO_CELDA))
textura_jugador_abajo = pygame.transform.scale(textura_jugador_abajo, (TAMANO_CELDA, TAMANO_CELDA))
textura_jugador_izquierda = pygame.transform.scale(textura_jugador_izquierda, (TAMANO_CELDA, TAMANO_CELDA))
textura_jugador_derecha = pygame.transform.scale(textura_jugador_derecha, (TAMANO_CELDA, TAMANO_CELDA))
textura_caja = pygame.transform.scale(textura_caja, (TAMANO_CELDA, TAMANO_CELDA))
textura_meta = pygame.transform.scale(textura_meta, (TAMANO_CELDA, TAMANO_CELDA))

def dibujar_nivel(nivel, direccion_jugador):
    VENTANA.fill(NEGRO)  # Rellenamos la ventana con color negro
    for i, fila in enumerate(nivel):  # Recorremos cada fila del nivel
        for j, elemento in enumerate(fila):  # Recorremos cada elemento de la fila
            x = j * TAMANO_CELDA  # Calculamos la posición x
            y = i * TAMANO_CELDA  # Calculamos la posición y
            
            # Dibujamos el piso en todas las celdas
            VENTANA.blit(textura_piso, (x, y))
            
            if elemento == PARED:
                VENTANA.blit(textura_pared, (x, y))  # Dibujamos una pared
            elif elemento == CAJA:
                VENTANA.blit(textura_caja, (x, y))  # Dibujamos una caja
            elif elemento == META:
                VENTANA.blit(textura_meta, (x, y))  # Dibujamos una meta
            elif elemento == JUGADOR:
                if direccion_jugador == 'arriba':
                    VENTANA.blit(textura_jugador_arriba, (x, y))
                elif direccion_jugador == 'abajo':
                    VENTANA.blit(textura_jugador_abajo, (x, y))
                elif direccion_jugador == 'izquierda':
                    VENTANA.blit(textura_jugador_izquierda, (x, y))
                elif direccion_jugador == 'derecha':
                    VENTANA.blit(textura_jugador_derecha, (x, y))
            elif elemento == JUGADOR_META:
                VENTANA.blit(textura_meta, (x, y))  # Dibujamos una meta
                if direccion_jugador == 'arriba':
                    VENTANA.blit(textura_jugador_arriba, (x, y))
                elif direccion_jugador == 'abajo':
                    VENTANA.blit(textura_jugador_abajo, (x, y))
                elif direccion_jugador == 'izquierda':
                    VENTANA.blit(textura_jugador_izquierda, (x, y))
                elif direccion_jugador == 'derecha':
                    VENTANA.blit(textura_jugador_derecha, (x, y))
            elif elemento == CAJA_META:
                VENTANA.blit(textura_meta, (x, y))  # Dibujamos una meta
                VENTANA.blit(textura_caja, (x, y))  # Dibujamos una caja encima de la meta


# Función para encontrar la posición del jugador

def encontrar_jugador(nivel):
    for i, fila in enumerate(nivel):  # Recorremos cada fila del nivel
        for j, elemento in enumerate(fila):  # Recorremos cada elemento de la fila
            if elemento == JUGADOR or elemento == JUGADOR_META:
                return i, j  # Devolvemos la posición del jugador
    return None

def verificar_victoria(nivel):
    for fila in nivel:
        for elemento in fila:
            if elemento == CAJA:  # Si hay alguna caja que no está en una meta
                return False
    return True  # Todas las cajas están en las metas

def mover_jugador(nivel, direccion):
    i, j = encontrar_jugador(nivel)  # Encontramos la posición actual del jugador
    if direccion == 'w':  # Mover hacia arriba
        if nivel[i-1][j] in (PISO, META):  # Movimiento del jugador
            nivel[i][j], nivel[i-1][j] = (PISO if nivel[i][j] == JUGADOR else META), (JUGADOR if nivel[i-1][j] == PISO else JUGADOR_META)
        elif nivel[i-1][j] in (CAJA, CAJA_META) and nivel[i-2][j] in (PISO, META):  # Movimiento de la caja
            nivel[i-2][j] = CAJA if nivel[i-2][j] == PISO else CAJA_META
            nivel[i-1][j] = JUGADOR if nivel[i-1][j] == CAJA else JUGADOR_META
            nivel[i][j] = PISO if nivel[i][j] == JUGADOR else META
    elif direccion == 's':  # Mover hacia abajo
        if nivel[i+1][j] in (PISO, META):
            nivel[i][j], nivel[i+1][j] = (PISO if nivel[i][j] == JUGADOR else META), (JUGADOR if nivel[i+1][j] == PISO else JUGADOR_META)
        elif nivel[i+1][j] in (CAJA, CAJA_META) and nivel[i+2][j] in (PISO, META):
            nivel[i+2][j] = CAJA if nivel[i+2][j] == PISO else CAJA_META
            nivel[i+1][j] = JUGADOR if nivel[i+1][j] == CAJA else JUGADOR_META
            nivel[i][j] = PISO if nivel[i][j] == JUGADOR else META
    elif direccion == 'a':  # Mover hacia la izquierda
        if nivel[i][j-1] in (PISO, META):
            nivel[i][j], nivel[i][j-1] = (PISO if nivel[i][j] == JUGADOR else META), (JUGADOR if nivel[i][j-1] == PISO else JUGADOR_META)
        elif nivel[i][j-1] in (CAJA, CAJA_META) and nivel[i][j-2] in (PISO, META):
            nivel[i][j-2] = CAJA if nivel[i][j-2] == PISO else CAJA_META
            nivel[i][j-1] = JUGADOR if nivel[i][j-1] == CAJA else JUGADOR_META
            nivel[i][j] = PISO if nivel[i][j] == JUGADOR else META
    elif direccion == 'd':  # Mover hacia la derecha
        if nivel[i][j+1] in (PISO, META):
            nivel[i][j], nivel[i][j+1] = (PISO if nivel[i][j] == JUGADOR else META), (JUGADOR if nivel[i][j+1] == PISO else JUGADOR_META)
        elif nivel[i][j+1] in (CAJA, CAJA_META) and nivel[i][j+2] in (PISO, META):
            nivel[i][j+2] = CAJA if nivel[i][j+2] == PISO else CAJA_META
            nivel[i][j+1] = JUGADOR if nivel[i][j+1] == CAJA else JUGADOR_META
            nivel[i][j] = PISO if nivel[i][j] == JUGADOR else META
    
    if verificar_victoria(nivel):
        mostrar_mensaje(VENTANA, "¡Has ganado!")
        mostrar_menu()

# Función para mostrar un mensaje en la ventana
def mostrar_mensaje(ventana, mensaje):
    ventana.fill(NEGRO)
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render(mensaje, True, BLANCO)
    ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  


            

# Variables iniciales
direccion_jugador = 'abajo'  # Dirección inicial del jugador

jugando = True
while jugando:
    eventos = pygame.event.get()  # Obtenemos todos los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False  # Salimos del bucle si se cierra la ventana
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                mover_jugador(nivel, 'w')  # Movemos al jugador hacia arriba
                direccion_jugador = 'arriba'
            elif evento.key == pygame.K_s:
                mover_jugador(nivel, 's')  # Movemos al jugador hacia abajo
                direccion_jugador = 'abajo'
            elif evento.key == pygame.K_a:
                mover_jugador(nivel, 'a')  # Movemos al jugador hacia la izquierda
                direccion_jugador = 'izquierda'
            elif evento.key == pygame.K_d:
                mover_jugador(nivel, 'd')  # Movemos al jugador hacia la derecha
                direccion_jugador = 'derecha'
    
    dibujar_nivel(nivel, direccion_jugador)  # Dibujamos el nivel
    pygame.display.update()  # Actualizar la pantalla

