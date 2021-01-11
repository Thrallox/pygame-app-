import pygame as pg 
import sys
import random

#Se crea la clase de nuestro juego 
class Game:
    def __init__(self): #Metodo init para iniciar la clase 
        self.pantalla = pg.display.set_mode((800,600))
        pg.display.set_caption("Futuro Arkanoid")

#Bucle principal que mantiene nuestro juego activo y procesando eventos 
    def bucle_principal(self):
        game_over = False
        while not game_over: 
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.pantalla.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            pg.display.flip()



#Inicia todos los modulos de pygame necesarios para que funcione
if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_principal()