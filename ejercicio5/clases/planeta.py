from cuerpo_celeste import CuerpoCeleste
import math

class Planeta(CuerpoCeleste):
    def __init__(self, id_celeste, nombre, masa_kg, radio_km, distancia_sol_km):
        super().__init__(id_celeste, nombre, masa_kg)
        if radio_km <= 0 or distancia_sol_km <= 0:
            raise ValueError("Radio y distancia deben ser mayores a cero.")
        self._radio_km = radio_km
        self._distancia_sol_km = distancia_sol_km

    @property
    def radio_km(self):
        return self._radio_km

    @property
    def distancia_sol_km(self):
        return self._distancia_sol_km

    def actualizar_radio(self, nuevo_radio):
        if nuevo_radio <= 0:
            raise ValueError("Radio debe ser positivo.")
        anterior = self._radio_km
        self._radio_km = nuevo_radio
        self._registrar_evento("radio_km", anterior, nuevo_radio)

    def actualizar_distancia_sol(self, nueva_distancia):
        if nueva_distancia <= 0:
            raise ValueError("Distancia debe ser positiva.")
        anterior = self._distancia_sol_km
        self._distancia_sol_km = nueva_distancia
        self._registrar_evento("distancia_sol_km", anterior, nueva_distancia)

    def calcular_densidad(self):
        volumen = (4/3) * math.pi * (self._radio_km ** 3)
        densidad = self.masa_kg / volumen
        return round(densidad, 2)

    def comparar_distancia(self, otro_planeta):
        if not isinstance(otro_planeta, Planeta):
            raise TypeError("Solo se puede comparar con otro planeta.")
        if self._distancia_sol_km < otro_planeta.distancia_sol_km:
            return f"{self.nombre} está más cerca del sol que {otro_planeta.nombre}."
        elif self._distancia_sol_km > otro_planeta.distancia_sol_km:
            return f"{otro_planeta.nombre} está más cerca del sol que {self.nombre}."
        else:
            return "Ambos planetas están a la misma distancia del sol."