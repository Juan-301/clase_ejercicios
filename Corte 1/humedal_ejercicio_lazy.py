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


def filtrar_por_estado_lazy(fileName, estado):
    """
    Retorna los registros cuyo 'estado' coincide con el parámetro dado
    (comparación insensible a mayúsculas/minúsculas y espacios).
    """

    generador_filt = filter(
        lambda registro:
            registro["estado"].strip().lower()
            == estado.strip().lower(),
        LoadData_lazy(fileName)
    )

    return generador_filt


# ---------------------------------------------------------------------------
# Punto 2


def extraer_nombres_lazy(fileName):
    """
    Retorna un generador con los nombres de todos los humedales.
    """

    generador_ext = map(
        lambda registro: registro["nombre"],LoadData_lazy(fileName)
    )

    return generador_ext


# ---------------------------------------------------------------------------
# Punto 3


def total_hectareas_lazy(fileName):
    """
    Retorna la suma total de hectáreas de todos los humedales,
    utilizando los datos cargados de forma lazy y reduce().
    """

    generador = LoadData_lazy(fileName)

    total = reduce(
        lambda acumulado, registro:acumulado + registro["hectareas"],generador,0)

    return total


# ---------------------------------------------------------------------------
# Punto 4

def promedio_biodiversidad(dataset):
    """
    Retorna el promedio de (aves + flora) por humedal,
    usando reduce (no usar sum() directamente).
    """

    total = reduce(
        lambda acumulado, registro:
            acumulado + registro["aves"] + registro["flora"],
        dataset,
        0
    )

    promedio = round(total / len(dataset), 3)

    return promedio


# ---------------------------------------------------------------------------
# Punto 5

def extraer_estados(dataset):
    """
    Función de apoyo: retorna el conjunto (set) de estados distintos
    presentes en el dataset.
    """

    estados = set(
        map(
            lambda registro: registro["estado"],
            dataset
        )
    )

    return estados


def resumen_por_estado(fileName):
    """
    Retorna un diccionario:
    {estado: cantidad_de_humedales_en_ese_estado},
    construido con una comprensión de diccionarios.
    """

    dataset = LoadData(fileName)

    estados = extraer_estados(dataset)

    resumen = {
        estado: len(
            list(
                filter(
                    lambda registro:
                        registro["estado"] == estado,
                    dataset
                )
            )
        )
        for estado in estados
    }

    return resumen


# ---------------------------------------------------------------------------
# Punto 6


def humedales_criticos_lazy(fileName, hectareas_min):
    """
    Retorna un generador con los humedales que:
    - estén en estado deteriorado
    O
    - tengan menos hectáreas que el mínimo indicado.
    """

    generador = filter(
        lambda registro:
            registro["estado"].strip().lower() == "deteriorado"
            or registro["hectareas"] < hectareas_min,
        LoadData_lazy(fileName)
    )

    return generador


# ---------------------------------------------------------------------------
# Punto 7 (BONUS)


def componer(*funciones):
    """
    BONUS:
    Retorna una nueva función que aplica las funciones recibidas
    en cadena, de derecha a izquierda.

    componer(f, g)(x) == f(g(x))
    """

    pass


# ---------------------------------------------------------------------------
# PROGRAMA PRINCIPAL

if __name__ == "__main__":

    archivo = "D:\Python\General\clase\dataset1.csv"

    # Dataset normal
    dataset = LoadData(archivo)
    

    # -----------------------------------------------------------------------
    # Punto 1

    print("Humedales en estado Deteriorado:")

    gen_1 = filtrar_por_estado_lazy(
        archivo,
        "deteriorado"
    )

    print(list(gen_1))


    # -----------------------------------------------------------------------
    # Punto 2

    print("\nNombres de todos los humedales:")

    gen_2 = extraer_nombres_lazy(archivo)

    print(list(gen_2))


    # -----------------------------------------------------------------------
    # Punto 3

    print(
        "\nTotal de hectáreas:",
        total_hectareas_lazy(archivo)
    )


    # -----------------------------------------------------------------------
    # Punto 4

    print(
        "\nPromedio de biodiversidad (aves+flora):",
        promedio_biodiversidad(dataset)
    )


    # -----------------------------------------------------------------------
    # Punto 5

    print("\nResumen por estado:")

    print(
        resumen_por_estado(archivo)
    )


    # -----------------------------------------------------------------------
    # Punto 6

    print(
        "\nGenerador perezoso "
        "(humedales críticos, hectareas_min=3.0):"
    )

    gen = humedales_criticos_lazy(
        archivo,
        3.0
    )

    print(next(gen))
    print(next(gen))


    # -----------------------------------------------------------------------
    # Punto 7 - BONUS

    # pipeline = componer(
    #     sorted,
    #     extraer_nombres,
    #     lambda d: filtrar_por_estado(d, "bueno")
    # )

    # print("\nNombres de humedales en buen estado, ordenados:")
    # print(pipeline(dataset))