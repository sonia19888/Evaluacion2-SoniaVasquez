from parcela import Parcela
from datetime import datetime

class ParcelaConRiego(Parcela):
    def __init__(self, id_parcela, superficie_ha, cultivo_actual, tasa_riego=0, umbral_min_litros=0):
        super().__init__(id_parcela, superficie_ha, cultivo_actual)
        self._litros_disponibles = 0
        self._tasa_riego_I_ha = tasa_riego
        self._umbral_min_litros = umbral_min_litros
        self._estado_riego = "habilitado" if self.estado == "activa" else "inhabilitado"
        self._eventos_riego = []

    @property
    def eventos_riego(self):
        return self._eventos_riego.copy()

    def configurar_tasa(self, tasa):
        if tasa <= 0:
            raise ValueError("Tasa debe ser mayor a cero.")
        self._tasa_riego_I_ha = tasa

    def configurar_umbral(self, litros):
        if litros < 0:
            raise ValueError("Umbral no puede ser negativo.")
        self._umbral_min_litros = litros

    def habilitar_riego(self):
        self._estado_riego = "habilitado"

    def inhabilitar_riego(self):
        self._estado_riego = "inhabilitado"

    def cargar_agua(self, litros):
        if litros <= 0:
            raise ValueError("Cantidad debe ser positiva.")
        saldo_antes = self._litros_disponibles
        self._litros_disponibles += litros
        self._eventos_riego.append({
            "fecha": datetime.now().isoformat(),
            "litros_solicitados": litros,
            "litros_aplicados": 0,
            "saldo_antes": saldo_antes,
            "saldo_despues": self._litros_disponibles,
            "modo": "carga"
        })

    def regar_automatico(self, modo):
        if self.estado != "activa" or self._estado_riego != "habilitado" or self._tasa_riego_I_ha <= 0:
            raise Exception("Riego no permitido por estado o configuración.")
        demanda = self.superficie_ha * self._tasa_riego_I_ha
        saldo_antes = self._litros_disponibles

        if modo == "estricto":
            if saldo_antes - demanda >= self._umbral_min_litros:
                self._litros_disponibles -= demanda
                aplicados = demanda
            else:
                raise Exception("No hay suficiente agua para riego estricto.")
        elif modo == "parcial":
            aplicables = max(0, saldo_antes - self._umbral_min_litros)
            aplicados = min(demanda, aplicables)
            self._litros_disponibles -= aplicados
        else:
            raise ValueError("Modo inválido.")

        self._eventos_riego.append({
            "fecha": datetime.now().isoformat(),
            "litros_solicitados": demanda,
            "litros_aplicados": aplicados,
            "saldo_antes": saldo_antes,
            "saldo_despues": self._litros_disponibles,
            "modo": modo
        })