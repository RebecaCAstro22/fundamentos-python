'''
Clase:        1. 
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.2
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Rebeca MIchelle Castro Pineda
Fecha:        2025-05-22
Estado:       [Terminado ]
'''

print("Bienvenido, creemos tu nuevo correo Key")
primer_nombre = input("Ingresa tu primer nombre: ")
primer_apellido = input("Ingresa tu primer apellido: ")

primer_nombref =primer_nombre.casefold()
primer_apellidof =primer_apellido.casefold()

print(f"El correo que se debe asignar al usuario ingresado es: {primer_nombref}.{primer_apellidof}@keyinstitute.edu.sv")