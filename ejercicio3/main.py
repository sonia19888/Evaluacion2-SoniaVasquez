from clases.carrera import Carrera

# Crear actividad válida
yoga = Carrera("ACT001", "Yoga", 60, 0)  # No se usa distancia en Yoga

# Intentar crear actividad con duración inválida
try:
    error_act = Carrera("ACT002", "Error", 0, 5)
except Exception as e:
    print("Error esperado:", e)

# Crear carrera válida
carrera = Carrera("CAR001", "10K", 50, 10)
print("Ritmo:", carrera.calcular_ritmo(), "min/km")

# Intentar registrar distancia negativa
try:
    carrera.registrar_distancia(-3)
except Exception as e:
    print("Error esperado:", e)

# Actualizar duración
carrera.actualizar_duracion(55)

# Mostrar historial
print("\nHistorial de eventos:")
for evento in carrera.historial_eventos:
    print(evento)

print("\nEventos de registro:")
for evento in carrera.eventos_registro:
    print(evento)