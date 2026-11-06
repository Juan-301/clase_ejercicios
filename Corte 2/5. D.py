#D—Inversión de Dependencias

# Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender
# de abstracciones. Esto se implementa con inyección de dependencias: en lugar de que una clase 
# cree sus propias dependencias con self.db = MySQL(), las recibe desde fuera. Facilita enormemente el testing.

from abc import ABC, abstractmethod

# Abstracciones (contratos)
class RepositorioUsuarios(ABC):
    @abstractmethod
    def buscar_por_id(self, uid: int) -> dict | None: ...
    @abstractmethod
    def guardar(self, usuario: dict) -> None: ...

class ServicioEmail(ABC):
    @abstractmethod
    def enviar(self, destino: str, asunto: str, cuerpo: str) -> bool: ...


# Implementaciones de bajo nivel
class RepositorioMemoria(RepositorioUsuarios):
    def __init__(self):
        self._datos: dict[int, dict] = {}

    def buscar_por_id(self, uid: int) -> dict | None:
        return self._datos.get(uid)

    def guardar(self, usuario: dict) -> None:
        self._datos[usuario["id"]] = usuario


class EmailConsola(ServicioEmail):
    """Para desarrollo/testing: imprime en consola."""
    def enviar(self, destino: str, asunto: str, cuerpo: str) -> bool:
        print(f"\n📧 Para: {destino}\n   Asunto: {asunto}\n   {cuerpo}")
        return True


# Módulo de alto nivel: depende SOLO de abstracciones
class ServicioRegistro:
    def __init__(self,
                 repo: RepositorioUsuarios,   # abstracción
                 email: ServicioEmail):          # abstracción
        self._repo = repo
        self._email = email
        self._siguiente_id = 1

    def registrar(self, nombre: str, email_addr: str) -> dict:
        usuario = {"id": self._siguiente_id, "nombre": nombre, "email": email_addr}
        self._siguiente_id += 1
        self._repo.guardar(usuario)
        self._email.enviar(
            email_addr,
            "Bienvenido",
            f"Hola {nombre}, tu cuenta ha sido creada."
        )
        return usuario


# Producción
repo = RepositorioMemoria()
mailer = EmailConsola()
servicio = ServicioRegistro(repo, mailer)  # inyección

u = servicio.registrar("Ana García", "ana@ejemplo.com")
print(repo.buscar_por_id(u["id"]))

# Testing: reemplaza dependencias con mocks sin tocar ServicioRegistro
class EmailMock(ServicioEmail):
    def __init__(self): self.enviados = []
    def enviar(self, d, a, c) -> bool:
        self.enviados.append({"destino": d, "asunto": a})
        return True

mock_email = EmailMock()
servicio_test = ServicioRegistro(RepositorioMemoria(), mock_email)
servicio_test.registrar("Test User", "test@mail.com")
print(mock_email.enviados)  # [{'destino': 'test@mail.com', 'asunto': 'Bienvenido'}]