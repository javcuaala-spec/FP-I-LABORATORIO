distancia_km = float(input("Introduce la distancia"))
velocidad_kmh = float(input("Introduce la velocidad"))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {int(tiempo_dias)} días en llegar.")