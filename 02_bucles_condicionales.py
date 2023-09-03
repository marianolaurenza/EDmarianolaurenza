#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      gmoya
#
# Created:     03/09/2023
# Copyright:   (c) gmoya 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
Ejercicio 2.
"""

# Pedir al usuario que ingrese dos nros
nro1 = int(input('Ingrese un nro: '))
nro2 = int(input('Ingrese otro nro: '))

# Luego imprimir 3 opciones (1. sumar, 2. restar y 3. multiplicar)
print(" 1. sumar\n 2. restar\n 3. multiplicar")

# Pedir al usuario que ingrese una opción
opcion = int(input('Seleccione una opción: '))

# Verificar la opción del usuario
# Mientras que el usuario no ingrese una opción correcta se volverá a pedir que
# ingrese una opción

opciones = [1, 2, 3]

while (opcion not in opciones) :
    opcion = int(input('Seleccione una opción: '))

# Ejecutar la operación
if (opcion == 1) :
    resultado = nro1 + nro2
    operacion = '+'
elif (opcion == 2) :
    resultado = nro1 - nro2
    operacion = '-'
elif (opcion == 3) :
    resultado = nro1 * nro2
    operacion = '*'

# Mostrar por pantalla el resultado
print(f'{nro1} {operacion} {nro2} = {resultado}')
