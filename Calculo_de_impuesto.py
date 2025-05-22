'''
Clase:        2. 
Tema:         Bloque condicional
Ejercicio:    2.3.2
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. 

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-05-22
Estado:       [Terminado ]
'''

unidades_consumidas = int(input("Ingrese las unidades consumidas: "))

if unidades_consumidas <= 100:
    impuesto = 0  
elif unidades_consumidas <= 200:
    impuesto = (unidades_consumidas - 100) * 0.5  
else:
    impuesto = (100 * 0.5) + ((unidades_consumidas - 200) * 0.7)

print(f"Impuesto aplicado: ${impuesto}")