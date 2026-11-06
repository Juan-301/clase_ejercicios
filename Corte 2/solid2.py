from abc import ABC, abstractmethod


class Estudiante:
    def __init__(self, nombre, valor_matricula, id):
        self.nombre = nombre
        self.valor_matricula = valor_matricula
        self.id = id



class IDescuento(ABC):
    @abstractmethod
    def calcular(self, valor_matricula: float) -> float:
        pass


# ─────────────────────────────────────────────
# BAJO NIVEL: implementaciones concretas de IDescuento
# ─────────────────────────────────────────────
class MatriculaHonor(IDescuento):
    def __init__(self, porcentaje=0.50):
        self.porcentaje = porcentaje

    def calcular(self, valor_matricula):
        return valor_matricula * self.porcentaje


class Familiar(IDescuento):
    def __init__(self, porcentaje=0.15):
        self.porcentaje = porcentaje

    def calcular(self, valor_matricula):
        return valor_matricula * self.porcentaje


class Convenio(IDescuento):
    def __init__(self, porcentaje=0.20):
        self.porcentaje = porcentaje

    def calcular(self, valor_matricula):
        return valor_matricula * self.porcentaje



class AplicadorDescuento:
    def __init__(self, descuentos: list[IDescuento]):   # ← Dependency Injection
        self.descuentos = descuentos

    def aplicar(self, estudiante: Estudiante) -> float:
        total_descuento = sum(d.calcular(estudiante.valor_matricula) for d in self.descuentos)
        total_descuento = min(total_descuento, estudiante.valor_matricula)  # nunca negativo
        return estudiante.valor_matricula - total_descuento


# ─────────────────────────────────────────────
# SRP: única responsabilidad → mostrar el resultado
# ─────────────────────────────────────────────
class ReporteLiquidacion:
    def imprimir(self, estudiante: Estudiante, descuentos: list[IDescuento], total: float) -> None:
        print(f"Estudiante: {estudiante.nombre} (ID {estudiante.id})")
        print(f"Matrícula base: ${estudiante.valor_matricula:,.0f}")
        for d in descuentos:
            print(f"  - {type(d).__name__}: -${d.calcular(estudiante.valor_matricula):,.0f}")
        print(f"Total a pagar: ${total:,.0f}")


# ─────────────────────────────────────────────
# Composición: aquí se deciden las clases concretas
# ─────────────────────────────────────────────
if __name__ == "__main__":
    reporte = ReporteLiquidacion()

    est = Estudiante("Juan", 5_000_000, 1)
    descuentos = [MatriculaHonor(), Familiar()]
    total = AplicadorDescuento(descuentos).aplicar(est)
    reporte.imprimir(est, descuentos, total)

  