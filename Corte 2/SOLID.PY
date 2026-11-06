'''PRINCIPIOS SOLID APLICADOS A LA PROGRAMACIÓN ORIENTADA A OBJETOS'''
from abc import ABC,abstractmethod

#calcular liquidacion matricula teniendo en cuenta distintos  tipos de descuento(matriculo de honor,convenio,monitorias)
# aplicando single responsability 

class Estudiante:

     def __init__(self,nombre,valor_matricula,id ):
         self.nombre = nombre
         self.valor_matricula = valor_matricula
         self.id= id


class Descuento(ABC):
     @abstractmethod
     def calcular(self, valor_matricula):
         pass


class MatriculaHonor(Descuento):
     def __init__(self, porcentaje=0.50):
         self.porcentaje = porcentaje

     def calcular(self, valor_matricula):
         return valor_matricula * self.porcentaje


class Matricula_Honor(Estudiante):
     def __init__(self,valor,matricula,nombre):
         super().__init__(self,matricula, nombre)
         self.valor= valor
     
class Convenio(Descuento):
     def __init__(self, porcentaje=0.20):
         self.porcentaje = porcentaje

     def calcular(self, valor_matricula):
         return valor_matricula * self.porcentaje


class Monitoria(Descuento):
    def __init__(self, horas, valor_hora=15000):
         self.horas = horas
         self.valor_hora = valor_hora

    def calcular(self, valor_matricula):
         return self.horas * self.valor_hora


#3. Responsabilidad: liquidar la matrícula aplicando los descuentos
class CalculadoraLiquidacion:
     def liquidar(self, estudiante, descuentos):
         total_descuento = sum(d.calcular(estudiante.valor_matricula) for d in descuentos)
         total_descuento = min(total_descuento, estudiante.valor_matricula)  # nunca negativo
         return estudiante.valor_matricula - total_descuento


#4. Responsabilidad: mostrar el resultado
class ReporteLiquidacion:
     def imprimir(self, estudiante, descuentos, total):
         print(f"Estudiante: {estudiante.nombre} (ID {estudiante.id})")
         print(f"Matrícula base: ${estudiante.valor_matricula:,.0f}")
         for d in descuentos:
             print(f"  - {type(d).__name__}: -${d.calcular(estudiante.valor_matricula):,.0f}")
         print(f"Total a pagar: ${total:,.0f}")





if __name__ == "__main__":
     est = Estudiante("Juan",5_000_000, 1)
     descuentos = [MatriculaHonor(), Convenio(0.10), Monitoria(horas=40)]

     total = CalculadoraLiquidacion().liquidar(est, descuentos)
     ReporteLiquidacion().imprimir(est, descuentos, total)
    
    
    
# Se podría iterar por la lista de descuentos y aplicarlos de forma acumulativa, sin problemas

# ISP (Interface Seggregation Principle: ninguna clase debe depender de métodos que no usa)

# ¿QUÉ PASA SI NO TODOS LOS DESCUENTO DEBEN VALIDAR ELEGIBILIDAD?
# SEPARO LA VALIDACIÓN DE LA ELEGIBILIDAD EN OTRA CLASE ABSTRACTA O INTERFAZ:

# Dependency Inversion Principle: Un módulo de alto nivel solo debe depender de abstracciones

# Sistema de notificaciones:  


# class Emailsender:
#     def sendEmail(self, message):
#         print(f"Enviando notificacion{message}")
        
# class NotificacionService:
#     def __init__(self):
#         #Ya estoy "amarrando" la funcionalidad a una implementación concreta
#         self.sender = EmailSender

#     def sendNotification(self, message):
#         self.snder

# #como lo solucionamos:

# #creamos una interfaz que define el contrato de las notificaciones
# class INotificationSender(ABC):
#     @abstractmethod
#     def send(self, message):
#         pass

# class EmailSender(INotificationService):
#     def send(self, message):
#         print(f"Enviando notificación: {message}, por email")

# class SMSSender(INotificationService):
#     def send(self, message):
#         print(f"Enviando notificacion: {message}, por email")

# class WhatsappSender(INotificationService):
#     def send(self, message):
#         print(f"Enviando notificación: {message}, por email")

# #ESTA ES LA CLASE DE ALTO NIVEL QUE DEPENDE DE LA ABSTRACCIÓN (LA INTERFAZ):
# class NotificationService:
#     #Aqui aplicamos inyección de dependencias:
#     def _init_(self, sender:INotificationsender):
#         self.sender = sender

#     def sendNotification(self, message):
#         self.sender.send(message)

# sender_via_sms = SMSSender()
# myNotificationService = NotificationService(sender_via_sms)
# myNotificationService.send("Hola! Ya llegó el pedido")

