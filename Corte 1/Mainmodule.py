from modulo import *


#Salida por consola:
print("Hola, Mundo")

# #Petición de datos por consola:

# #Tipado dinámico (como javascript) vs. tipado estático de otros lenguajes (C, C#, Java)

# #------- Tipos de datos en Pyton:
# '''
# Text Type:  str
# Numeric Types:  int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:   dict
# Set Types:  set, frozenset
# Boolean Type:   bool
# Binary Types:   bytes, bytearray, memoryview
# None Type:  NoneType ("null")
# '''

# current_year = 2026
# tallest_person_height = 2.3
# name = input("Cuál es tu nombre?:\n")
# #OJO CON EL INPUT: siempre devuelve un dato de tipo str, debo convertirlo al tipo que quiero asignar
# #a mi variables:

# b_year = int(input("Cuál es tu año de nacimiento?:\n"))
# height = float(input("Cuál es tu estatura?:\n"))

# age = current_year - b_year
# height_difference = (tallest_person_height - height)*100
# #Cómo redondeamos a 1 decimal?


# #Impresión con formato:
# print(f" Te llamas {name}  y tienes {age} años. Bienvenido a lenguajes de programación  ")
# print(f"La persona más alta, te lleva {height_difference} cm.")

# #----- COLECCIONES DE DATOS:
# # (en otros lenguajes existen arreglos, matrices, etc)

# # 1. Listas [] (mutable)
# empty_list = []
# empty_list.append(1)
# empty_list.append("Uno")
# empty_list.append(1.0)
# empty_list.append(True)


# not_empty_list = empty_list


# reversed_list = not_empty_list.reverse() #¿?

# print(f"La lista quedó así: {not_empty_list}")
# print(f"La lista al revés:{reversed_list}")

# # 2. Tuplas (,) - *,* (datos inmutables)

# coord_1 = 1,5
# coord_2 = (8,5)
# students = ("Jhon Stiven","Gabriela","Andrea") #Tupla (es inmutable, los valores no se pueden cambiar)
# students_list = ["Jhon Stiven","Gabriela","Andrea"]
# print( f"\nPrimero se matriculó: {students[0]}")
# print(f"\nLuego se matriculó: {students[1]}")
# print(f"\nFinalmente se matriculó: {students[2]}")

# # ¡¡¡
# #students[1] = "Gabriela Rico" # NO SE PUEDE ALTERAR EL VALOR DE UNA TUPLA:
# students_list[1] = "Gabriela Rico"
# students_list = agregar(students_list, "Diego")

# print("Con el elemento eliminado:")
# print(students_list)

# ####   UNIDAD 1: PROGRAMACIÓN FUNCIONAL EN PYTHON
# '''
# Ayuda a escribir código
# * más limpio,
# * fácil de probar y
# * libre de errores ocultos al tratar las "funciones como elementos principales"
# (FUNCIONES COMO CIUDADANOS DE PRIMER ORDEN) y evitar cambios en los datos (INMUTABILIDAD Y FUNCIONES PURAS).
# '''
# # CONCEPTOS BÁSICOS DE PROGRAMACIÓN FUNCIONAL EN PYTHON (EN PAUSA, VOLVEMOS A LAS 8:40 PM)

# # 1. FUNCIONES COMO OBJETOS O CIUDADANOS DE PRIMER ORDEN:

# #menu condicional para elegir que función operar sobre la lista:

# while True:
#     opcion = int(input("Qué operación desea aplicar? 1. Agregar 2. Eliminar 3.buscar 4. Salir: "))
#     if opcion == 1:
#         funcion = agregar #FUNCION COMO OBJETO DE PRIMER ORDEN
#     elif opcion == 2:
#         funcion = eliminar

#     elif opcion == 3:
#         funcion = buscar

#     else:
#         break

#     valor = input("Ingrese el valor que desea agregar,eliminar o buscar: ")
#     students_list = funcion(students_list,valor)
#     print(students_list)


#EJERCICIO: vamos a agregar la función "BUSCAR"

####

# lista=["3,6,9,12"]

valor_ususario = int(input("Ingrese el valor que: "))

# print(f"El doble de {valor_ususario} es: {duplicar(valor_ususario)}")

# print(f'Multiplicando cada elemento de la lista {lista} por 3: {multiplicar_elementos(lista,3)}')

operacion = int(input("Qué operación desea aplicar? 1. Cuadrado 2. Cubo 3. Potencia: "))

if operacion == 1:
    print(f"El cuadrado de {valor_ususario} es: {aplicar_funcion(cuadrado, valor_ususario, 0)}")
elif operacion == 2:
    print(f"El cubo de {valor_ususario} es: {aplicar_funcion(cubo, valor_ususario, 0)}")
elif operacion == 3:
    potencia = int(input("Ingrese la potencia a la que desea elevar el número: "))
    print(f"{valor_ususario} elevado a la {potencia} es: {aplicar_funcion(pow, valor_ususario, potencia)}")
       
       
list1000 = list(range(1000))
#print(list1000)

list1000_cuadrado = list(map(cuadrado, list1000))
print(f"Los cuadrados de los números del 1 al 1000 son: {list1000_cuadrado}")

#
#EJERCICIO:
lista_palabras = ["muchos", "AÑOS","DESPUÉS","frente","AL","PELOTÓN", "DE","FUSILAMIENTO,","EL", "CORONEL"]

# 1. Vamos a mapear una función que permita crear una lista con las palabras con las mayúsculas correctas:

# 2. "reduce" la lista usando una función de concatenación, para armar la primera oración de la palabra:

#

#3.1.2 la función "reduce", reduce o consolida una lista:
# Aplica la función suma por pares de elementos, hasta que sume todos los números de la lista
# suma_numeros = reduce( suma, list1000 )

# print(f"la suma total de los numeros es {suma_numeros}")