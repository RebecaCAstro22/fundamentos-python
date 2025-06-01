'''
Clase:        8. 
Tema:         Estructuras Iterativas
Ejercicio:   5.4.2 Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. Ejemplo:
Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-05-31
Estado:       [Terminado ]
'''
numero = int(input("Ingresa un número: "))
original = numero

print(f"\nProceso de reducción para {original}:")

while numero >= 10:
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    print(f"{numero} = {suma}")
    numero = suma

print(f"\nEl resultado final es: {numero}")
