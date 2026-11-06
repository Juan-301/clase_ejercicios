"""
Ejercicio: Programación funcional sobre datos de humedales de Cali.
Completar cada función marcada con # TODO.
No usar bucles for/while explícitos dentro de las funciones (sí se permiten
dentro de comprensiones, ya que no cuentan como bucle explícito).
"""

from functools import reduce


def LoadData(fileName):
    dataset = []
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            dataset.append(registro)
    return dataset


def LoadData_lazy(fileName):
    with open(fileName, encoding='utf-8') as f:
        for line in f:  # iterar x cada renglón del archivo
            values = line.split(sep=';')
            registro = {"nombre": values[0],
                        "direccion": values[1],
                        "hectareas": float(values[2]),
                        "aves": int(values[3]),
                        "flora": int(values[4]),
                        "estado": values[5].strip()}
            yield registro


# ---------------------------------------------------------------------------
# Punto 1

    """Retorna los registros cuyo 'estado' coincide con el parámetro dado
    (comparación insensible a mayúsculas/minúsculas y espacios)."""

def filtrar_por_estado(dataset, estado):

    filtrar_por_estado=list(filter(lambda est: est ['estado'].strip().lower() == estado.strip().lower(),dataset))
    return filtrar_por_estado

# def filtrar_por_estado_lazy(fileName, estado):

#     generador_filt=filter(lambda registro: registro ['estado'].strip().lower() == estado.strip().lower(),dataset)

#     return generador_filt




# ---------------------------------------------------------------------------
# Punto 2

def extraer_nombres(dataset):

      """Retorna una lista solo con los nombres de los humedales."""
    
      extraer_nombres=list(map(lambda ext: ext ['nombre'],dataset))
    
      return extraer_nombres





# ---------------------------------------------------------------------------
# Punto 3
def total_hectareas(dataset):
    """Retorna la suma total de hectáreas de todos los humedales."""
    

    total_hectareas=reduce(lambda acumulado, registro: acumulado + registro["hectareas"],dataset,0)

    return total_hectareas


# ---------------------------------------------------------------------------
# Punto 4
def promedio_biodiversidad(dataset):

    """Retorna el promedio de (aves + flora) por humedal, usando reduce
    (no usar sum() directamente)."""

    total = reduce(lambda acumulado, registro: acumulado + registro['aves'] + registro['flora'],dataset,0)

    promedio =round(total / len(dataset),3)

    return promedio
    
    
# ---------------------------------------------------------------------------
# Punto 5
def extraer_estados(dataset):
    """Función de apoyo: retorna el conjunto (set) de estados distintos
    presentes en el dataset."""

    estados = set(map(lambda registro: registro["estado"],dataset))

    return estados


def resumen_por_estado(fileName):
    """Retorna un diccionario {estado: cantidad_de_humedales_en_ese_estado},
    construido con una comprensión de diccionarios."""
    
    estados = extraer_estados(dataset)

    resumen = {estado: len(filtrar_por_estado(dataset, estado))

        for estado in estados
    }

    return resumen



# ---------------------------------------------------------------------------
# Punto 6
def humedales_criticos_lazy(fileName, hectareas_min):

    generador = filter(
        lambda registro:registro["estado"].strip().lower() == "deteriorado" or registro["hectareas"] < hectareas_min,        LoadData_lazy(fileName)
    )

    return generador

# ---------------------------------------------------------------------------
# Punto 7 (bonus)
def componer(*funciones):
    """Retorna una nueva función que aplica las funciones recibidas en
    cadena, de derecha a izquierda: componer(f, g)(x) == f(g(x))."""
    # TODO: implementar composición de funciones con reduce
    pass


# ---------------------------------------------------------------------------
if __name__ == "__main__":
    dataset = LoadData("D:\Python\General\clase\dataset1.csv")

    print("Humedales en estado Deteriorado:")
    print(filtrar_por_estado(dataset, "deteriorado"))
   
    

    print("\nNombres de todos los humedales:")
    print(extraer_nombres(dataset))
  

    
    print("\nTotal de hectáreas:", total_hectareas(dataset))

    print("\nPromedio de biodiversidad (aves+flora):", promedio_biodiversidad(dataset))

    print("\nResumen por estado:")
    print(resumen_por_estado("D:\Python\General\clase\dataset1.csv"))

    print("\nGenerador perezoso (humedales críticos, hectareas_min=3.0):")
    gen = humedales_criticos_lazy("D:\Python\General\clase\dataset1.csv", 3.0)
    print(next(gen))
    print(next(gen))



    # Punto 7 (bonus): pipeline con composición de funciones
    # pipeline = componer(sorted, extraer_nombres,
    #                      lambda d: filtrar_por_estado(d, "bueno"))
    # print("\nNombres de humedales en buen estado, ordenados:")
    # print(pipeline(dataset))


#map y filter no generan toda la lista