'''
Clase:        1. 
Tema:         Manejo de matrices
Ejercicio:    10.2.1
Descripción:  Extraer la diagonal principal y secundaria de una matriz 

Autor:        Rebeca MIchelle Castro Pineda
Fecha:        2025-06-14
Estado:       [Terminado ]
'''


def obtener_diagonales(n, matriz):
    diagonal_principal = [matriz[i][i] for i in range(n)]
    diagonal_secundaria = [matriz[i][n - i - 1] for i in range(n)]
    return diagonal_principal, diagonal_secundaria


n = int(input("Ingrese el tamaño de la matriz: "))
matriz = [list(map(int, input(f"Ingrese la fila {i + 1}: ").split(','))) for i in range(n)]


diag_principal, diag_secundaria = obtener_diagonales(n, matriz)

print(diag_principal)
print(diag_secundaria)