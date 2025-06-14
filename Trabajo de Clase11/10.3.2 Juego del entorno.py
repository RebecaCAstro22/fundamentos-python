'''
Clase:        11. 
Tema:         Manejo de matrices
Ejercicio:    10.3.2
Descripción:  Juego del entorno  

Autor:        Rebeca MIchelle Castro Pineda
Fecha:        2025-06-14
Estado:       [Terminado ]
'''

def contar_vecinos_unos(matriz, n, m):
    resultado = [[0] * m for _ in range(n)]
    direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(n):
        for j in range(m):
            cuenta = 0
            for dx, dy in direcciones:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and matriz[x][y] == 1:
                    cuenta += 1
            resultado[i][j] = cuenta
    return resultado

n = int(input("N:"))
m = int(input("M:"))
matriz = [list(map(int, input().split(','))) for _ in range(n)]

matriz_resultante = contar_vecinos_unos(matriz, n, m)

for fila in matriz_resultante:
    print(fila)