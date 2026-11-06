#S-ingle Responsibility Principle

# Una clase debe tener una sola razón para cambiar. Si una clase hace demasiadas cosas,
# un cambio en una funcionalidad puede romper otra. El truco mental: si describes la clase 
# con "y" en la mitad ("guarda datos Y envía emails"), la estás dividiendo.


from dataclasses import dataclass, field
from typing import Protocol

@dataclass
class LineaFactura:
    descripcion: str
    cantidad: int
    precio_unitario: float

    @property
    def subtotal(self) -> float:
        return self.cantidad * self.precio_unitario


# Clase 1: solo representa la factura y su lógica de negocio
@dataclass
class Factura:
    numero: str
    cliente: str
    lineas: list[LineaFactura] = field(default_factory=list)

    def total(self) -> float:
        return sum(l.subtotal for l in self.lineas)

    def agregar_linea(self, linea: LineaFactura) -> None:
        self.lineas.append(linea)


# Clase 2: solo se encarga de imprimir/formatear
class ImpresoraFactura:
    def imprimir(self, factura: Factura) -> str:
        lineas = [f"FACTURA #{factura.numero}",
                  f"Cliente: {factura.cliente}",
                  "-" * 30]
        for l in factura.lineas:
            lineas.append(f"  {l.descripcion:{20}} ${l.subtotal:>8.2f}")
        lineas.append(f"  {'TOTAL':{20}} ${factura.total():>8.2f}")
        return "\n".join(lineas)


# Clase 3: solo se encarga de persistencia
class RepositorioFactura:
    def __init__(self):
        self._almacen: dict[str, Factura] = {}

    def guardar(self, factura: Factura) -> None:
        self._almacen[factura.numero] = factura

    def buscar(self, numero: str) -> Factura | None:
        return self._almacen.get(numero)


# Uso
factura = Factura("F-001", "Tech Corp")
factura.agregar_linea(LineaFactura("Laptop Pro", 2, 1500.00))
factura.agregar_linea(LineaFactura("Mouse inalámbrico", 3, 45.00))

repo = RepositorioFactura()
repo.guardar(factura)

impresora = ImpresoraFactura()
print(impresora.imprimir(factura))