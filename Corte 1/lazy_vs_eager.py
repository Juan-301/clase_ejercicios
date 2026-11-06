
# Evaluacion hambrienta: Calcula el resultado completo inmediatamente y lo almacena completamente en la memoria.
# Este es el comportamiento predeterminado de Python para estructuras de datos estandar como listas, conjuntos y diccionarios.
# [1] (https://paths.grasp.study/modules/ec733c04-c287-47f5-88b3-6af6687e98c4/lessons/2eb9f0b3-f126-4038-977b-f33b7d01605f),
# [2] (https://khaisastudio.medium.com/eager-vs-lazy-approach-0b4b7ba63cda),
# [3](https://levelup.gitconnected.com/evaluation-strategy-in-python-22eb454202e2), 
# [4] (https://www.youtube.com/watch?v=906KhLWVmnQ)Eval

from dataset1 import * 

#Funcion para un consumidor hambriento

def eager():
    numbers = []
    for i in range(100000):
        numbers.append(i)
    return numbers

#Funcion perezosa genera valores bajo demanda

def lazy_generator():
    for i in range(100000):
        yield i

#consumo con  "evaluacion hambrienta":

# nuevos_numeros = eager()
# print(nuevos_numeros)



#Consumo con evaluación perezosa:
gen = lazy_generator()



# try:

#     while True:
#         #El consumidor perezoso consume solo un elemento a la vez:
#         print(next(gen))
# except StopIteration:
#     print("El generador ya no tiene mas números") 



# Generador "Eager": genera todo el dataset, haciendo esperar al consumidor:
def LoadData(fileName):
    dataset = []
    with open(fileName,encoding='utf-8') as f:
        for line in f: #iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            dataset.append(registro)    
    return dataset

# Generador "Lazy": genera un nuevo registro solo si se lo piden:
def LoadData_lazy(fileName):
    with open(fileName,encoding='utf-8') as f:
        for line in f: #iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre":values[0],
                        "direccion":values[1],
                        "hectareas":float(values[2]),
                        "aves":int(values[3]),
                        "flora":int(values[4]),
                        "estado":values[5]}
            yield registro  

eager_eval = LoadData("dataset1.csv")
print("Todos los registros:\n",eager_eval)

lazy_eval = LoadData_lazy("dataset1.csv")
print("Primer registro: ", next(lazy_eval))
print("segundo registro: ", next(lazy_eval))