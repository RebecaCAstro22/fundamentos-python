'''
Clase:        2. 
Tema:         Bloque condicional
Ejercicio:   2.3.1
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Rebeca Michelle Castro Pineda
Fecha:        2025-05-22
Estado:       [Terminado ]
'''

contraseña = input("Ingrese una contraseña: ")

if len(contraseña) < 8:
    print("Contraseña no segura")
else:
    tiene_mayuscula = any(caracter.isupper() for caracter in contraseña)
    tiene_numero = any(caracter.isdigit() for caracter in contraseña)

    if tiene_mayuscula and tiene_numero:
        print("Contraseña segura")
    else:
        print("Contraseña no segura")
