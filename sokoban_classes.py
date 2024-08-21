import pygame
from sokoban_classes import *

class sokoban_game:

    def __init__(self):
        pygame.init()
        self.initialize_screen()
        self.levels = self.load_niveles()
        self.running = True
        print(self.levels)

    def initialize_screen(self):
        pygame.display.set_mode(("WIDTH, HEIGHT"))
        pygame.display.set_caption("SOKOBAN")
        icon = pygame.image.load("imagenes/cara.png")
        pygame.display.set_icon(icon)

    def load_niveles(self):
        with open("niveles") as file:
            levels = []
            for line in file:
                line = line.rstrip()
                if line:
                    if line.star_swith("LEVEL"):
                        LEVEL = {"map":[], "jugador":[], "crates": []}
                    elif line.startswith("P: "):
                        x,y = map(int, line[3:].split(","))
                        LEVEL["jugador"].append((x,y)) 
                    elif line.startswith("C: "):
                        crates = line[3:].split()
                        for crate in crates:
                            x,y = map(int, crate)
                            LEVEL["crates"].append((x,y))
                    elif line == "FINAL NIVEL":
                        levels.append(LEVEL)
                    else:
                        LEVEL["map"].append(line)
        return tuple(levels)
            

        
    

    def launch(self):
        while self.running:
            self.handle_events()
            self.update.logic()
            self.update_screen()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type.QUIT:
                self.running = False

    def update_logic(self):
        ...

    def update_screen(self):
        ...
        

    def __init__(cls) -> None:
        pygame.quit()
        