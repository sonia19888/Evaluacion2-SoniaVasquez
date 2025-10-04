from datetime import datetime

class Vehiculo:
    def __init__(self, id_vehiculo, patente, peso_kg):
        if not patente or peso_kg <= 0:
            raise ValueError("Patente inválida o peso no válido.")
        self.id_vehiculo = id_vehiculo
        self._patente = patente
        self._peso_kg = peso_kg
        self._estado = "habilitado"
        self._historial_eventos = []

    @property
    def patente(self):
        return self._patente

    @property
    def peso_kg(self):
        return self._peso_kg

    @property
    def estado(self):
        return self._estado

    @property
    def historial_eventos(self):
        return self._historial_eventos.copy()

    def _registrar_evento(self, usuario, tipo_evento, detalle):
        evento = {
            "fecha": datetime.now().isoformat(),
            "usuario": usuario,
            "tipo_evento": tipo_evento,
            "detalle": detalle
        }
        self._historial_eventos.append(evento)

    def actualizar_peso(self, nuevo_peso_kg, usuario="sistema"):
        if self._estado != "habilitado":
            raise Exception("Vehículo inhabilitado. No se puede actualizar peso.")
        if nuevo_peso_kg <= 0:
            raise ValueError("Peso debe ser mayor a cero.")
        anterior = self._peso_kg
        self._peso_kg = nuevo_peso_kg
        self._registrar_evento(usuario, "actualizar_peso", f"{anterior} → {nuevo_peso_kg}")

    def habilitar(self, motivo, usuario="sistema"):
        self._estado = "habilitado"
        self._registrar_evento(usuario, "habilitar", motivo)

    def inhabilitar(self, motivo, usuario="sistema"):
        self._estado = "inhabilitado"
        self._registrar_evento(usuario, "inhabilitar", motivo)

    def consultar_ficha(self):
        return {
            "id": self.id_vehiculo,
            "patente": self._patente,
            "peso_kg": self._peso_kg,
            "estado": self._estado,
            "últimos_eventos": self._historial_eventos[-3:]
        }