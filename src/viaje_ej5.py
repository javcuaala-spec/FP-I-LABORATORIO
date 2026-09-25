
distancia_km = float(input("Introduce la distancia"))
velocidad_kmh = float(input("Introduce la velocidad"))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {int(tiempo_dias)} días en llegar.")
repetir=input("¿Desea hacer otra simulación?(s/n)")
while repetir!= "s" and repetir != "n":
    repetir=input("Responda con estas letras Si(s) o No(n)")
if repetir== "s":
    distancia_km = float(input("Introduce la distancia"))
    velocidad_kmh = float(input("Introduce la velocidad"))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas // 24
    print(f"Tardarías {int(tiempo_dias)} días en llegar.")

#También se puede hacer definiendo una variable 
