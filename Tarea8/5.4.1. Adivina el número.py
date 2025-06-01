'''
Clase:        8. 
Tema:         Estructuras Iterativas
Ejercicio:   5.4.1  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-05-31
Estado:       [Terminado ]
'''


import random

secreto = random.randint(1, 100)

while True:
    intento = int(input("Ingresa un numero entre 1 y 100: "))

    if intento < secreto:
        print("El número secreto es mayor")
    elif intento > secreto:
        print("El número secreto es menor")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto: {secreto}")
        print("Fin del juego")
        break
