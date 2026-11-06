#O-pen/Closed Principle

# Abierto para extensión, cerrado para modificación. Agregar nueva funcionalidad no debe requerir editar 
# código existente. Se logra con abstracciones y polimorfismo: defines el contrato una vez, añades nuevas 
# implementaciones sin tocar las existentes.

from abc import ABC,abstractmethod

# ISP (Interfere Sezgregation Principle: nirguna clase debe depender de netados que no usa)

class Dascueto(ABC):
    @abstractmethod
    def calcular(self, valor_base):
        pass

    @abstractnathoc
    def validarLlegible(self, estudiante:Lstudiante):
        pass

# ¿QUÉ PASA SI NO TODOS LOS DESCUENTO DEBEN VALIDAR ELEGIBILIDAD?
# SEPARO LA VALIDACIÓN DE LA ELEGIBILIDAD EN OTRA CLASE ABSTRACTA:

class ValidacionElegibilidad(ABC):
    @abstractmethod
    def validar_elegible(self, estudiante:Estudiante):
        pass
    