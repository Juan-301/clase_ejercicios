#I—Segregación de Interfaces

# Ninguna clase debe depender de métodos que no usa. Prefiere muchas interfaces pequeñas sobre 
# una interfaz grande. Si una clase implementa una interfaz y tiene que dejar métodos vacíos o 
# lanzar NotImplementedError, es señal de que la interfaz es demasiado grande.

from abc import ABC, abstractmethod

# Interfaces pequeñas y enfocadas
class Imprimible(ABC):
    @abstractmethod
    def imprimir(self, documento: str) -> None: ...

class Escaneable(ABC):
    @abstractmethod
    def escanear(self) -> str: ...

class Faxeable(ABC):
    @abstractmethod
    def enviar_fax(self, numero: str, doc: str) -> None: ...


# Cada dispositivo implementa solo lo que puede hacer
class ImpresoraBasica(Imprimible):
    def imprimir(self, documento: str) -> None:
        print(f"[ImpresoraBasica] Imprimiendo: {documento[:40]}...")


class EscanerSimple(Escaneable):
    def escanear(self) -> str:
        return "[EscanerSimple] Documento escaneado"


class ImpresoraMultifuncion(Imprimible, Escaneable, Faxeable):
    def imprimir(self, documento: str) -> None:
        print(f"[Multifunción] Imprimiendo en alta calidad: {documento[:30]}")

    def escanear(self) -> str:
        return "[Multifunción] Escaneado a 600 DPI"

    def enviar_fax(self, numero: str, doc: str) -> None:
        print(f"[Multifunción] Fax enviado a {numero}")


# Funciones que dependen solo de la interfaz que necesitan
def imprimir_reporte(imp: Imprimible, reporte: str) -> None:
    imp.imprimir(reporte)

def digitalizar(scan: Escaneable) -> str:
    return scan.escanear()


impresora = ImpresoraBasica()
multifuncion = ImpresoraMultifuncion()

imprimir_reporte(impresora, "Reporte Q3 2024")
imprimir_reporte(multifuncion, "Reporte Q3 2024")
print(digitalizar(multifuncion))
# imprimir_reporte(EscanerSimple(), ...)  ← error de tipos: no implementa Imprimible