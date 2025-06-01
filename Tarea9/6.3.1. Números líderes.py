'''
Clase:        9. 
Tema:         Manejo de listas
Ejercicio:   6.3.1
Descripción: Un número en una lista es "líder" si es
estrictamente mayor que todos los
elementos a su derecha. Dada una lista de
números ingresada por el usuario, imprime
todos los números líderes.

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-06-1
Estado:       [Terminado ]
'''

numeros = list(map(int, input().split()))
lideres = []

for i in range(len(numeros) - 1):
    if numeros[i] > numeros[i + 1]:
        lideres.append(numeros[i])


print(*lideres)