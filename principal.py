from functools import reduce
from modulo import *
import random


lista_palabras = [
    "muchos", "AÑOS", "DESPUÉS", "frente", "AL",
    "PELOTÓN", "DE", "FUSILAMIENTO,", "EL", "CORONEL"
]


palabras_correctas = list(map(corregir_mayusculas, lista_palabras))

print("Lista con las palabras corregidas:")
print(palabras_correctas)


oracion = reduce(concatenar, palabras_correctas)

print("\nPrimera oración:")
print(oracion)


list1000 = list(range(1000))
suma_numeros = reduce(suma, list1000)
print("\nSuma de los números:")
print(f"La suma total de los números es {suma_numeros}")

#-------------------------------------------------------------------#


lista_impares1000 = list(filter(es_impar, list1000))
#print(f"Primeros 1000 números impares: {lista_impares1000}")


#EJERCICIO EN CLASE:
#1. Tenemos . una. lista .de . temperaturas .capturadas .desde-un sensor, pero .vienen .en . °F.

numero_float=random.uniform(0.0,100.0)
random_temps_f= []
#generar una lista de varios numeros aleatorios(100):

for _ in range(10):
     random_temps_f.append(random.uniform(0.0,100.0))

#2. Vamos . a . convertir .a ℃
temps_c = list(map(convert_f_to_c, random_temps_f))
#temps_c = list(map(lambda f:(temp - 32)*(5/9), random_temps_f))


#3. Vamos a·filtrar aquellas .que . sean .mayores .a .32° .C

temps_M_32 =list(filter(filtrar_mayores,temps_c))
#temps_M_32 =list(filter(lambda f:(temp > 32),temps_c))


print(f"Temperaturas aleatorias:{temps_c}")
print(f"Temperaturas{temps_M_32}")

#suma_temps=list(reduce(lambda x,y:x+y,temps_M_32))
#print(f"La suma de temperaturas es:{suma_temps}")

#--------------------------------------------------#
#ejercicio Map,Filter,reduce, lambda
producto1={ "nombre":"camisa","precio":15000}
producto1={ "nombre":"par de zapatos","precio":250000}

#Lista de productos, con precios en dólares:

productos = [
{"nombre": "Camisa", "precio": 30},
{"nombre": "Zapatos", "precio": 120},
{"nombre": "Gorra", "precio": 15},
{"nombre": "Pantalón", "precio": 80},
{"nombre": "Calcetines", "precio": 10},
]

print(f"\nproductos con valor en pesos:{productos}")

print("\n--- 1. Map ---")
#conversion de dolares a pesos:

productos_pesos = list(
    map(
        lambda p:{
            "nombre":p["nombre"],
            "precio":round(p["precio"]*3200,2)
        },
        productos
    )
)

print(f"\nproductos con valor en pesos:{productos_pesos}")

#Aplicar un descuento del 10%

productos_con_descuento_10=list(map(lambda p:{"nombre":p["nombre"],"precio":round(p["precio"]*0.9,2)},productos_pesos))

print(f"productos en pesos con descuento del 10%{productos_con_descuento_10}")


#FILTRAR PRODUCTOS CON PRECIO > 50000:
print("\n--- 2.Filter ---")

productos_caros = list(
    filter(
        lambda producto:producto["precio"]>50000,
        productos_con_descuento_10
    )
)

print(f"Productos caros:{productos_caros}")



total_carrito = reduce(
lambda acum,p:acum + p["precio"],
productos_caros,
0
)
print("\nEl total del carrrito de compras es", total_carrito)




