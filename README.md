# JUEGO BOMBAS

Ejemplo didáctico de juego de adivinación usando PyGame y SenseHat

## Objetivo

Descubrir la totalidad de los casilleros sin BOMBAS (color ROJO), utilizando solamente la suerte.

1. Al comenzar el juego, se nos avisa cuántas bombas hay sembradas
2. Iniciamos con 7 vidas, y cada vez que elegimos una bomba, perdemos una.
3. Deben quedar sin descubrir la mayor cantidad de BOMBAS

## Implementación

Se muestra un tablero en pantalla y se replica en la matriz de LEDs de la SenseHat.
Para moverse entre los casilleros pueden emplearse tanto las flechas del teclado como el joystick de la SenseHat.
La selección se hace con la barra espaciadora.

## TODO

- Implementación con clases (OOP)
- Indicación de bombas adyacentes (como en el buscaminas)
- Agregar pantallas de inicio y fin de juego
- Incorporar más sonidos (por el momento, solamente se reproducen sonidos de explosión de la bomba y al finalizar)