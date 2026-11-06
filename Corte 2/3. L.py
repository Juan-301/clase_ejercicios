#L-iskov Substitution Principle


# Una subclase debe poder reemplazar a su clase padre sin romper el programa. Si en algún punto 
# tienes que preguntar "¿es un Perro o un Gato?" para comportarte diferente, algo está mal. 
# El ejemplo clásico: un Cuadrado hereda de Rectangulo — parece lógico, pero viola LSP.


# ✗ VIOLACIÓN: Cuadrado hereda de Rectángulo
class RectanguloMalo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

class CuadradoMalo(RectanguloMalo):
    def __init__(self, lado):
        super().__init__(lado, lado)

    # Problema: cambiar ancho obliga a cambiar alto
    @RectanguloMalo.ancho.setter
    def ancho(self, v): self._ancho = self._alto = v


def duplicar_ancho(r: RectanguloMalo):
    r.ancho *= 2
    print(f"Esperado alto=5, obtenido: {r.alto}")  # ¡CuadradoMalo devuelve 10!


# ✓ SOLUCIÓN: jerarquía correcta con abstracción compartida
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def perimetro(self) -> float: ...

class Rectangulo(Forma):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto
    def area(self) -> float: return self.ancho * self.alto
    def perimetro(self) -> float: return 2 * (self.ancho + self.alto)

class Cuadrado(Forma):  # hermano de Rectangulo, no hijo
    def __init__(self, lado: float):
        self.lado = lado
    def area(self) -> float: return self.lado ** 2
    def perimetro(self) -> float: return 4 * self.lado

# Ahora sí — cualquier Forma puede sustituir a otra en esta función
def describir_forma(f: Forma) -> None:
    print(f"{type(f).__name__}: área={f.area():.2f}, perímetro={f.perimetro():.2f}")

for forma in [Rectangulo(4, 5), Cuadrado(4), Rectangulo(10, 2)]:
    describir_forma(forma)  # funciona perfectamente para todos