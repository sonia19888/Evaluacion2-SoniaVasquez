from clases.parcela_con_riego import ParcelaConRiego

# Crear parcela
parcela = ParcelaConRiego("P001", 10.50, "Trigo")
parcela.actualizar_cultivo("Maíz")

# Configurar riego
parcela.configurar_tasa(1500)
parcela.configurar_umbral(2000)
parcela.cargar_agua(20000)

# Riego estricto
parcela.regar_automatico("estricto")

# Desactivar parcela y probar riego
parcela.desactivar("Fin de temporada")
try:
    parcela.regar_automatico("estricto")
except Exception as e:
    print("Error esperado:", e)

# Riego parcial con saldo limitado
parcela.habilitar("Reactivación")
parcela.cargar_agua(3000)
parcela.regar_automatico("parcial")

# Mostrar historial
print("Historial de eventos:")
for evento in parcela.historial_eventos:
    print(evento)

print("\nEventos de riego:")
for evento in parcela.eventos_riego:
    print(evento)