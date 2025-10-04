from vehiculo import Vehiculo
from datetime import datetime

class Auto(Vehiculo):
    def __init__(self, id_vehiculo, patente, peso_kg, asientos_totales, sistema_retencion_infantil="no"):
        super().__init__(id_vehiculo, patente, peso_kg)
        if asientos_totales < 1:
            raise ValueError("Debe tener al menos un asiento.")
        self._asientos_totales = asientos_totales
        self._ocupantes_actuales = 0
        self._sistema_retencion_infantil = sistema_retencion_infantil
        self._eventos_ocupacion = []

    @property
    def ocupantes_actuales(self):
        return self._ocupantes_actuales

    @property
    def eventos_ocupacion(self):
        return self._eventos_ocupacion.copy()

    def _registrar_ocupacion(self, accion, cantidad, motivo=""):
        evento = {
            "fecha": datetime.now().isoformat(),
            "accion": accion,
            "cantidad": cantidad,
            "ocupantes_antes": self._ocupantes_actuales,
            "ocupantes_despues": self._ocupantes_actuales,
            "motivo": motivo
        }
        self._eventos_ocupacion.append(evento)

    def subir_personas(self, n):
        if self.estado != "habilitado":
            raise Exception("Vehículo inhabilitado.")
        if n < 1 or self._ocupantes_actuales + n > self._asientos_totales:
            raise ValueError("No se puede subir esa cantidad.")
        self._ocupantes_actuales += n
        self._registrar_ocupacion("subir", n)

    def bajar_personas(self, n):
        if self.estado != "habilitado":
            raise Exception("Vehículo inhabilitado.")
        if n < 1 or self._ocupantes_actuales - n < 0:
            raise ValueError("No se puede bajar esa cantidad.")
        self._ocupantes_actuales -= n
        self._registrar_ocupacion("bajar", n)

    def reconfigurar_asientos(self, nuevo_total, motivo):
        if nuevo_total < 1 or nuevo_total < self._ocupantes_actuales:
            raise ValueError("No se puede reducir por debajo de ocupantes actuales.")
        anterior = self._asientos_totales
        self._asientos_totales = nuevo_total
        self._registrar_evento("sistema", "reconfigurar_asientos", f"{anterior} → {nuevo_total} | Motivo: {motivo}")

    def vaciar_auto(self, motivo):
        self._registrar_ocupacion("vaciar", self._ocupantes_actuales, motivo)
        self._ocupantes_actuales = 0

    def consultar_ocupacion(self):
        tasa = (self._ocupantes_actuales / self._asientos_totales) * 100
        return {
            "ocupantes": self._ocupantes_actuales,
            "asientos_libres": self._asientos_totales - self._ocupantes_actuales,
            "tasa_ocupacion": round(tasa, 2)
        }