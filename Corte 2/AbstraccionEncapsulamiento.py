from abc import ABC, abstractmethod


#-------------------(1) ABSTRACCIÓN---------------------
# INTRODUCCIÓN AL ABSTRACCIÓN:

#Clase abstracta que define un metodo dde pago:

class MetodoPago(ABC):
    @abstractmethod


#los métodos que empiecen con una referencia a this, o self, son
#métodos de instancia

    def procesar_pago(this, monto:float):
        pass 

#clases concretas: methodos de pago, especificacion:

class TarjetaCredito(MetodoPago):
    def procesar_pago(this, monto):
        #return super().procesar_pago(monto)
        print("Procesando pago con tarjeta de credito por el monto ", monto)

class PagoMercadoPago(MetodoPago):
    def procesar_pago(this, monto):
        print("Procesando pago Mercado Pago por: ", monto)


#-------------(2) ENCAPSULAMIENTO------------------
# INTRODUCCIÓN AL ENCAPSULAMIENTO:


class Cuentabancaria:

    def __init__(this, titular:str, numero:int, saldo_inicial:float):
        #Todos los atributos de "this", "self", son atributos de instancia:
        this.titular = titular
        this.numero = numero
        this.saldo= saldo_inicial


        def obtener_saldo(this):
            return this.saldo

        def hacer_deposito(this, valor:float):
            
            if valor > 0:
                
                this.saldo += valor 

        def hacer_retiro(this, valor:float):

            if valor > 0 and this.saldo >= valor:
                this.saldo -= valor
            I

#-------------------(3)HERENCIA-------------------

# class Empleado (ABC):
#     def __init__(this, nombre:str, id:str, salario_base:float):
#     #completar
#         pass


#     @abstractmethod
#     def liquidar_pago(this):
#         pass

# class Administrativo(Empleado):

#     def __init_(this, nombre:str, id:str, salario_base:float):
#         pass

#     def liquidar_pago(this):
#         pass



#     return super().liquidar_pago()


# class Docente(Empleado):

#     def __init_(this, nombre:str, id:str, salario_base:float):
#         pass

#     def liquidar_pago(this):
#         #Liquidar pago sin el bono:
#         return super().liquidar_pago()



# -------------------(3) HERENCIA -------------------

class Empleado(ABC):

    def __init__(this, nombre: str, id: str, salario_base: float):
        this.nombre = nombre
        this.id = id
        this.salariO = salario_base

    @abstractmethod
    def liquidar_pago(this) -> float:
     
        return this.salario_base


class Administrativo(Empleado):

    def __init__(this, nombre: str, id: str, salario_base: float,
                 bono: float = 0, horas_extras: int = 0, valor_hora_extra: float = 0):

        super().__init__(nombre, id, salario_base)
        this.bono = bono
        this.horas_extras = horas_extras
        this.valor_hora_extra = valor_hora_extra

    def calcular_horas_extras(this) -> float:
        return this.horas_extras * this.valor_hora_extra

    def liquidar_pago(this) -> float:
        # Salario base + bono + horas extras
        return super().liquidar_pago() + this.bono + this.calcular_horas_extras()


    def liquidar_pago() -> float:
        
        return super().liquidar_pago() + this.bono


class Docente(Empleado):

    def __init__(this, nombre: str, id: str, salario_base: float):
        super().__init__(nombre, id, salario_base)

    def liquidar_pago(this) -> float:
        # Liquidar pago sin el bono
        return super().liquidar_pago()




# EJERCICIO PARA LA PRÓXIMA SEMANA :
# SISTEMA DE GESTIÓN DE UNA BIBLIOTECA:
# A) LIBROS FÍSICOS
# B) E-BOOKS
# C) AUDIOLIBROS

# 1. ABSTRACCIÓN: QUÉ CLASE ABSTRACTA MODELA EL RECURSO BIBLIOGRÁFICO (título, autor, año)
# 2. HERENCIA: CADA TIPO DE PUBLICACIÓN TIENE SUS ATRIBUTOS PROPIOS
# 3. CADA PUBLICACIÓN TIENE SUS ATRIBUTOS PRIVADOS: USUARIO EN PRÉSTAMO, FECHA DE ENTREGA
# 4. POLIMORFISMO: CADA TIPO DE PUBLICACIÓN TIENE SU PROPIA FORMA DE GESTIONAR PRÉSTAMO