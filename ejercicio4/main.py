from clases.auto import Auto

# Crear vehículo
auto = Auto("V001", "ABCD12", 1450, 5)
auto.actualizar_peso(1500)

# Inhabilitar y probar rechazo
auto.inhabilitar("mantención")
try:
    auto.actualizar_peso(1600)
except Exception as e:
    print("Error esperado:", e)

auto.habilitar("mantención finalizada")

# Subir personas
auto.subir_personas(3)
try:
    auto.subir_personas(3)
except Exception as e:
    print("Error esperado:", e)

# Bajar personas
auto.bajar_personas(2)
try:
    auto.bajar_personas(5)
except Exception as e:
    print("Error esperado:", e)

# Reconfigurar asientos
auto.reconfigurar_asientos(2, "reparación")
try:
    auto.reconfigurar_asientos(0, "error")
except Exception as e:
    print("Error esperado:", e)

# Vaciar auto
auto.vaciar_auto("fin de turno")

# Inhabilitar y probar rechazo
auto.inhabilitar("bloqueo")
try:
    auto.subir_personas(1)
except Exception as e:
    print("Error esperado:", e)

# Mostrar auditoría
print("\nHistorial de eventos:")
for evento in auto.historial_eventos:
    print(evento)

print("\nEventos de ocupación:")
for evento in auto.eventos_ocupacion:
    print(evento)