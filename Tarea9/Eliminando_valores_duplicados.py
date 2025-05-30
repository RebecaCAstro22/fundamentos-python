'''
Clase:        9. 
Tema:         Manejo de listas
Ejercicio:   6.2.1
Descripción:  Eliminando valores duplicados

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-05-30
Estado:       [Terminado ]
'''

#Elimina los valores duplicados 
lista_str = input(" ")
newlist = lista_str.split()
sin_duplicados = []  

for i in newlist:
    sin_duplicados.append(int(i))

lista_final = sorted(set(sin_duplicados))  

for numero in lista_final:
    print(numero, end=" ") 