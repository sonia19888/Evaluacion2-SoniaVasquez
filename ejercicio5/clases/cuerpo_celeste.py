from datetime import datetime

class CuerpoCeleste:
    def __init__(self, id_celeste, nombre, masa_kg):
        if not nombre or masa_kg <= 0:
            raise ValueError("Nombre vacío o masa inválida.")
        self.id_celeste = id_celeste
        self._nombre = nombre
        self._masa_kg = masa_kg
        self._historial_eventos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def masa_kg(self):
        return self._masa_kg

    @property
    def historial_eventos(self):
        return self._historial_eventos.copy()

    def _registrar_evento(self, campo, anterior, nuevo):
        evento = {
            "fecha": datetime.now().isoformat(),
            "campo": campo,
            "valor_anterior": anterior,
            "valor_nuevo": nuevo
        }
        self._historial_eventos.append(evento)

    def actualizar_nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("Nombre no puede estar vacío.")
        anterior = self._nombre
        self._nombre = nuevo_nombre
        self._registrar_evento("nombre", anterior, nuevo_nombre)

    def actualizar_masa(self, nueva_masa):
        if nueva_masa <= 0:
            raise ValueError("Masa debe ser positiva.")
        anterior = self._masa_kg
        self._masa_kg = nueva_masa
        self._registrar_evento("masa_kg", anterior, nueva_masa)

    def consultar_ficha(self):
        return {
            "id": self.id_celeste,
            "nombre": self._nombre,
            "masa_kg": self._masa_kg,
            "últimos_eventos": self._historial_eventos[-3:]
        }