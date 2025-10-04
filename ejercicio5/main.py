from clases.planeta import Planeta

# Crear cuerpo celeste
estrella = Planeta("C001", "Estrella X", 2e30, 1000000, 0)

# Crear planetas
tierra = Planeta("P001", "Tierra", 5.97e24, 6371, 149_600_000)
marte = Planeta("P002", "Marte", 6.42e23, 3389, 227_900_000)

# Calcular densidad
print("Densidad Tierra:", tierra.calcular_densidad(), "kg/km³")

# Comparar distancias
print(tierra.comparar_distancia(marte))

# Intentar crear planeta con radio 0
try:
    error_planeta = Planeta("P003", "Error", 1e24, 0, 100000)
except Exception as e:
    print("Error esperado:", e)

# Actualizar masa
tierra.actualizar_masa(6e24)

# Mostrar historial
print("\nHistorial de eventos:")
for evento in tierra.historial_eventos:
    print(evento)