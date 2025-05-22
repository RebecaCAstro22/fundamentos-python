'''
Clase:        1. 
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.1
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar.

Autor:        Rebeca MIchelle Castro Pineda
Fecha:        2025-05-22
Estado:       [Terminado ]
'''
cuenta= float(input("Dame el total de la cuenta:"))
porcentaje= int(input("Dame el porcentaje de propina:"))

propina = cuenta /porcentaje 
total = cuenta + cuenta /porcentaje 


print(f"Total de la cuenta: {cuenta}")
print(f"Propina:{propina}")
print(f"Total de la cuenta con propina ({porcentaje}%): {total}")


