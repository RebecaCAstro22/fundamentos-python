'''
Clase:        11. 
Tema:         Manejo de matrices
Ejercicio:    10.3.1
Descripción:  Matriz simetrica  

Autor:        Rebeca MIchelle Castro Pineda
Fecha:        2025-06-14
Estado:       [Terminado ]
'''
def es_simetrica(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return "La matriz no es simétrica"
    return "La matriz es simétrica"

n = int(input("N:"))
matriz = []

for _ in range(n):
    entrada = input().strip()
    if entrada:
        matriz.append(list(map(int, entrada.split(','))))
    else:
        print("Error: Se esperaba una fila de números separados por comas.")
        exit()

print(es_simetrica(matriz))