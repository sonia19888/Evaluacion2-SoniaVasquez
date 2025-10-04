from datetime import datetime

class Parcela:
    def __init__(self, id_parcela, superficie_ha, cultivo_actual):
        if superficie_ha <= 0 or not cultivo_actual:
            raise ValueError("Datos inválidos para la parcela.")
        self.id_parcela = id_parcela
        self._superficie_ha = round(superficie_ha, 2)
        self._cultivo_actual = cultivo_actual
        self._estado = "activa"
        self._historial_eventos = []

    @property
    def superficie_ha(self):
        return self._superficie_ha

    @property
    def cultivo_actual(self):
        return self._cultivo_actual

    @property
    def estado(self):
        return self._estado

    @property
    def historial_eventos(self):
        return self._historial_eventos.copy()

    def _registrar_evento(self, tipo, detalle):
        evento = {
            "fecha": datetime.now().isoformat(),
            "tipo": tipo,
            "detalle": detalle
        }
        self._historial_eventos.append(evento)

    def actualizar_cultivo(self, nuevo_cultivo):
        if self._estado != "activa":
            raise Exception("No se puede actualizar cultivo en parcela inactiva.")
        if not nuevo_cultivo:
            raise ValueError("Cultivo no puede estar vacío.")
        anterior = self._cultivo_actual
        self._cultivo_actual = nuevo_cultivo
        self._registrar_evento("actualizar_cultivo", f"{anterior} → {nuevo_cultivo}")

    def activar(self, motivo):
        self._estado = "activa"
        self._registrar_evento("activar", motivo)

    def desactivar(self, motivo):
        self._estado = "inactiva"
        self._registrar_evento("desactivar", motivo)

    def rectificar_superficie(self, nueva_superficie, motivo):
        if nueva_superficie <= 0:
            raise ValueError("Superficie debe ser mayor a cero.")
        anterior = self._superficie_ha
        self._superficie_ha = round(nueva_superficie, 2)
        self._registrar_evento("rectificar_superficie", f"{anterior} → {nueva_superficie} | Motivo: {motivo}")