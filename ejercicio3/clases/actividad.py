from datetime import datetime

class Actividad:
    def __init__(self, id_actividad, nombre, duracion_min):
        if not nombre or duracion_min < 1:
            raise ValueError("Nombre vacío o duración inválida.")
        self.id_actividad = id_actividad
        self._nombre = nombre
        self._duracion_min = duracion_min
        self._historial_eventos = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def duracion_min(self):
        return self._duracion_min

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

    def actualizar_duracion(self, nueva_duracion):
        if nueva_duracion < 1:
            raise ValueError("Duración debe ser al menos 1 minuto.")
        anterior = self._duracion_min
        self._duracion_min = nueva_duracion
        self._registrar_evento("duracion_min", anterior, nueva_duracion)