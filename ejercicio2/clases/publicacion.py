from datetime import datetime

class Publicacion:
    def __init__(self, id_publicacion, titulo, anio):
        if not titulo or anio < 1450:
            raise ValueError("Título vacío o año inválido.")
        self.id_publicacion = id_publicacion
        self._titulo = titulo
        self._anio = anio
        self._historial_eventos = []

    @property
    def titulo(self):
        return self._titulo

    @property
    def anio(self):
        return self._anio

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

    def actualizar_titulo(self, nuevo_titulo):
        if not nuevo_titulo:
            raise ValueError("El título no puede estar vacío.")
        anterior = self._titulo
        self._titulo = nuevo_titulo
        self._registrar_evento("titulo", anterior, nuevo_titulo)

    def actualizar_anio(self, nuevo_anio):
        if nuevo_anio < 1450:
            raise ValueError("Año inválido.")
        anterior = self._anio
        self._anio = nuevo_anio
        self._registrar_evento("anio", anterior, nuevo_anio)