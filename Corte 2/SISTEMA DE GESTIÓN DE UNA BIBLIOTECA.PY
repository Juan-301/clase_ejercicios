# # EJERCICIO PARA LA PRÓXIMA SEMANA :
# # SISTEMA DE GESTIÓN DE UNA BIBLIOTECA:
# # A) LIBROS FÍSICOS
# # B) E-BOOKS
# # C) AUDIOLIBROS

# # 1. ABSTRACCIÓN: QUÉ CLASE ABSTRACTA MODELA EL RECURSO BIBLIOGRÁFICO (título, autor, año)
# # 2. HERENCIA: CADA TIPO DE PUBLICACIÓN TIENE SUS ATRIBUTOS PROPIOS
# # 3. CADA PUBLICACIÓN TIENE SUS ATRIBUTOS PRIVADOS: USUARIO EN PRÉSTAMO, FECHA DE ENTREGA
# # 4. POLIMORFISMO: CADA TIPO DE PUBLICACIÓN TIENE SU PROPIA FORMA DE GESTIONAR PRÉSTAMO

# class Libro_Fisico:
#     def __init__(self,paginas,autor,genero,año):
#         self.paginas=paginas
#         self.autor=autor
#         self.genero=genero
#         self.año=año



# class Ebook(Libro_Fisico):
#     def __init__(self,paginas,autor,genero,año,peso):
#         super().__init__(paginas,autor,genero)
#         self.peso=peso


# class Audiolibro(Libro_Fisico):
#     def __init__(self,paginas,autor,genero,año,duracion):
#         super().__init__(paginas,autor,genero,año)
#         self.duracion=duracion

from abc import ABC, abstractmethod
from datetime import date, timedelta


# 1. ABSTRACCIÓN
class RecursoBibliografico(ABC):
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        # 3. ENCAPSULAMIENTO: atributos privados
        self.__usuario_prestamo = None
        self.__fecha_entrega = None

    @property
    def usuario_prestamo(self):
        return self.__usuario_prestamo

    @property
    def fecha_entrega(self):
        return self.__fecha_entrega

    def esta_disponible(self):
        return self.__usuario_prestamo is None

    def _registrar_prestamo(self, usuario, dias):
        """Único punto para modificar los atributos privados desde las subclases."""
        self.__usuario_prestamo = usuario
        self.__fecha_entrega = date.today() + timedelta(days=dias)

    def devolver(self):
        if self.esta_disponible():
            print(f"'{self.titulo}' no está prestado.")
            return
        print(f"'{self.titulo}' devuelto por {self.__usuario_prestamo}.")
        self.__usuario_prestamo = None
        self.__fecha_entrega = None

    @abstractmethod
    def prestar(self, usuario):
        pass

    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        if self.esta_disponible():
            estado = "Disponible"
        else:
            estado = f"Prestado a {self.__usuario_prestamo} hasta {self.__fecha_entrega}"
        return f"[{self.tipo()}] {self.titulo} - {self.autor} ({self.año}) | {estado}"


# 2. HERENCIA: cada tipo con sus atributos propios
class LibroFisico(RecursoBibliografico):
    DIAS_PRESTAMO = 15

    def __init__(self, titulo, autor, año, paginas, estante):
        super().__init__(titulo, autor, año)
        self.paginas = paginas
        self.estante = estante

    def tipo(self):
        return "Libro físico"

    # 4. POLIMORFISMO
    def prestar(self, usuario):
        if not self.esta_disponible():
            print(f"'{self.titulo}' no está disponible. Lo tiene {self.usuario_prestamo}.")
            return
        self._registrar_prestamo(usuario, self.DIAS_PRESTAMO)
        print(f"{usuario} debe recoger '{self.titulo}' en el estante {self.estante}. "
              f"Devolver antes del {self.fecha_entrega}.")



class Ebook(RecursoBibliografico):
    DIAS_PRESTAMO = 7

    def __init__(self, titulo, autor, año, tamaño_mb, formato):
        super().__init__(titulo, autor, año)
        self.tamaño_mb = tamaño_mb
        self.formato = formato

    def tipo(self):
        return "E-book"

    def prestar(self, usuario):
        if not self.esta_disponible():
            print(f"La licencia de '{self.titulo}' está en uso por {self.usuario_prestamo}.")
            return
        self._registrar_prestamo(usuario, self.DIAS_PRESTAMO)
        print(f"Enlace de descarga enviado a {usuario} ({self.formato}, {self.tamaño_mb} MB). "
              f"La licencia expira el {self.fecha_entrega}.")

    def devolver(self):
        print(f"Licencia de '{self.titulo}' revocada del dispositivo.")
        super().devolver()


class Audiolibro(RecursoBibliografico):
    DIAS_PRESTAMO = 21

    def __init__(self, titulo, autor, año, duracion_min, narrador):
        super().__init__(titulo, autor, año)
        self.duracion_min = duracion_min
        self.narrador = narrador

    def tipo(self):
        return "Audiolibro"

    def prestar(self, usuario):
        if not self.esta_disponible():
            print(f"'{self.titulo}' ya está en reproducción por {self.usuario_prestamo}.")
            return
        self._registrar_prestamo(usuario, self.DIAS_PRESTAMO)
        horas, minutos = divmod(self.duracion_min, 60)
        print(f"Acceso en streaming activado para {usuario}: '{self.titulo}' "
              f"narrado por {self.narrador} ({horas}h {minutos}min). "
              f"Disponible hasta el {self.fecha_entrega}.")


# PRUEBA
if __name__ == "__main__":
    catalogo = [
        LibroFisico("Cien años de soledad", "Gabriel García Márquez", 1967, 471, "A-12"),
        Ebook("Clean Code", "Robert C. Martin", 2008, 4.5, "PDF"),
        Audiolibro("El principito", "Antoine de Saint-Exupéry", 1943, 95, "Juan Pérez"),
    ]

    print("=== Préstamos ===")
    for recurso in catalogo:           # misma llamada, comportamiento distinto
        recurso.prestar("Juan")

    print("\n=== Intento de préstamo repetido ===")
    catalogo[0].prestar("María")

    print("\n=== Estado del catálogo ===")
    for recurso in catalogo:
        print(recurso)

    print("\n=== Devoluciones ===")
    for recurso in catalogo:
        recurso.devolver()

    # print(catalogo[0].__usuario_prestamo)  -> AttributeError (es privado)
    # RecursoBibliografico("x", "y", 2000)   -> TypeError (es abstracta)

 

