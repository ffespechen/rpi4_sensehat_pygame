# En Raspberry Pi usar python -m venv env --system-site-packages 
# Sonidos https://mixkit.co/free-sound-effects/game-over/
# Fuente https://fonts.google.com/specimen/Rubik 
import random
import sys
import time
import pygame
from pygame.locals import *
from sense_hat import SenseHat
from colores import * 

FPS = 30
CONVERSOR_X = 50
CONVERSOR_Y = 50
RADIO = 20
FILAS = 8
COLUMNAS = 8

PANTALLA_ANCHO = (COLUMNAS + 1) * CONVERSOR_X
PANTALLA_ALTURA = (FILAS + 1 ) * CONVERSOR_Y

LISTA_COLORES = [RED, BLUE, GREEN, YELLOW]
BOMBA = RED

# Variables auxiliares del juego
pos_x = 0
pos_y = 0
vidas = 7
cantidad_bombas = 0

# Modelo del Tablero de Juego
tablero = []
for i in range(COLUMNAS):
    for j in range(FILAS):
        color_casillero = random.choice(LISTA_COLORES)
        tablero.append([i, j, color_casillero, False])
        if color_casillero == BOMBA:
            cantidad_bombas += 1

# Inicializar PyGame
pygame.init()
PANTALLA = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTURA))
pygame.display.set_caption('Bombas')
fpsclock = pygame.time.Clock()

# Sonidos
pygame.mixer.init()
explosion = pygame.mixer.Sound('sonidos/mixkit-bomb-drop-impact-2804.wav')
fin_juego = pygame.mixer.Sound('sonidos/mixkit-funny-game-over-2878.wav')

# Generar una instancia de SenseHat
sense = SenseHat()

# Funciones auxiliares
def convertir_unidades_pantalla(x, y):
    return ((x + 1) * CONVERSOR_X, (y + 1) * CONVERSOR_Y)

def obtener_posicion(px, py):
    return ((px / CONVERSOR_X) - 1, (py / CONVERSOR_Y) - 1)

def terminar_juego():
    sense.clear(GRAY)
    pygame.mixer.Sound.play(fin_juego)
    time.sleep(3)
    pygame.quit()
    sys.exit()

print(F'Cantidad de Bombas >> {cantidad_bombas}')

while True:
    # Banderas
    seleccionado = False

    if vidas == 0:
        print('JUEGO TERMINADO')
        terminar_juego()

    # Eventos de PyGame
    for event in pygame.event.get():
        if event.type == QUIT:
            terminar_juego()
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                pos_y += 1
            if event.key == K_UP:
                pos_y -= 1
            if event.key == K_LEFT:
                pos_x -= 1
            if event.key == K_RIGHT:
                pos_x += 1

            # Validación de posiciones en el tablero
            pos_x = pos_x if pos_x < COLUMNAS else 0
            pos_x = pos_x if pos_x >= 0 else COLUMNAS - 1
            pos_y = pos_y if pos_y < FILAS else 0
            pos_y = pos_y if pos_y >= 0 else FILAS - 1

            if event.key == K_SPACE:
                print(pos_x, pos_y)
                seleccionado = True

    PANTALLA.fill(BLACK)

    # Detecto cuál de los objetos fue seleccionado y si se trata de una bomba
    for objeto in tablero:
        if seleccionado:
            if objeto[0] == pos_x and objeto[1] == pos_y:
                print(objeto)
                objeto[3] = True 
                if objeto[2] == BOMBA:
                    pygame.mixer.Sound.play(explosion)
                    vidas -= 1
                    print(f'BOMBA!!! >> Te quedan {vidas} vidas ')

        # Dibujo del tablero en Pantalla
        color_objeto = objeto[2] if objeto[3] else GRAY
        px, py = convertir_unidades_pantalla(objeto[0], objeto[1])
        pygame.draw.circle(PANTALLA, color_objeto, (px, py), RADIO)
        
        # Tablero en la SenseHat
        sense.set_pixel(objeto[0], objeto[1], color_objeto)

    # Posición del selector
    pygame.draw.circle(PANTALLA, PURPLE, convertir_unidades_pantalla(pos_x, pos_y), RADIO, 3)

    pygame.display.update()
    fpsclock.tick(FPS)