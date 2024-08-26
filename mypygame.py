import pygame


ANCHO = 1000 #ancho de la ventana
ALTO = 800 #alto de la ventana
VENTANA = pygame.display.set_mode
([ANCHO,ALTO])

jugando = True #mientras sea True se estará ejecutando el juego

pygame.init()

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode([ANCHO,ALTO])

jugando = True


while jugando:
    eventos = pygame.event.get()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False # cuando sea False dejará de ejecutar el juego 

    pygame.display.update()


quit()

def is_valid_value(self,char):
        if ( char == ' ' or #piso
            char == '#' or #muro
            char == '@' or #trabajador en el piso
            char == '.' or #muelle  
            char == '*' or #caja en el muelle
            char == '$' or #caja
            char == '+' ): #trabajador en el 
                return False
        

nivel_1


