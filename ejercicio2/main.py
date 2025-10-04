from clases.libro import Libro

# Crear publicación válida
don_quijote = Libro("PUB001", "Don Quijote", 1605, 1000)

# Intentar crear publicación con año inválido
try:
    error_pub = Libro("PUB002", "Antiguo", 1400, 100)
except Exception as e:
    print("Error esperado:", e)

# Crear libro y leer páginas
libro = Libro("LIB001", "Cien años de soledad", 1967, 500)
libro.leer(120)
print("Progreso:", libro.consultar_progreso(), "%")

# Intentar leer más páginas que las restantes
try:
    libro.leer(400)
except Exception as e:
    print("Error esperado:", e)

# Actualizar año
libro.actualizar_anio(1970)

# Mostrar historial
print("\nHistorial de eventos:")
for evento in libro.historial_eventos:
    print(evento)

print("\nEventos de lectura:")
for evento in libro.eventos_lectura:
    print(evento)