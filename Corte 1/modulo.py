def agregar(lista, elemento):
    lista.append(elemento)
    return lista
 
def eliminar(lista, elemento):
    lista.remove(elemento)
    return lista  

def buscar(lista, elemento):
    if elemento in lista:
        print(f"El elemento '{elemento}' sí se encuentra en la lista.")
    else:
        print(f"El elemento '{elemento}' no se encuentra en la lista.")
    
    return lista

def duplicar(x):
    return x * 2

def agregar_pura(lista, elemento):
    copia= lista.copy()
    copia.append(elemento)
    return copia
    
def multiplicar_elementos(lista, mult):
#Quiero que la función multiplique cada valor de la lista por el multiplicador
  
    return [elemento * mult for elemento in lista]

def cuadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

def pow(num, pot):
    return num ** pot

def suma(a, b):
    return a + b    

# Función de orden superior que aplica una determinada funcion a un valor y devuelve un número:
def aplicar_funcion(funcion, valor, pot):
    # Validar si la funcion es cuadrado, cubo, o pow:
    # is, isInstance, type
    if funcion is cuadrado:
        return cuadrado(valor)
    elif funcion is cubo:
        return cubo(valor)
    elif funcion is pow:
        return pow(valor, pot)




def corregir_mayusculas(palabra):
    return palabra.capitalize()

def concatenar(palabra1, palabra2):
    return palabra1 + " " + palabra2

def es_impar(numero):
    if numero % 2 ==0:
        return False
    else:
        return True

def convert_f_to_c(temp):

    return (temp - 32)*(5/9)

def filtrar_mayores(temp):
    return temp > 32