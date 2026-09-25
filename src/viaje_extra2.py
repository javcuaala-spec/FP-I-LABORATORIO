#EJERCICIO 1

#distancia_km = 384400  # distancia Tierra - Luna
#velocidad_kmh = 5000
#tiempo_horas = distancia_km // velocidad_kmh
#tiempo_dias = tiempo_horas // 24
#if tiempo_dias>7:
 #   tiempo_semanas=tiempo_dias//7
  #  if tiempo_dias%7 > 0:
   #     dias=tiempo_dias%7
    #    print(f"Tardarías {tiempo_semanas} semanas y {dias} días en llegar.")
    #else:
     #   print(f"Tardarías {tiempo_semanas} semanas en llegar")
#print(f"Tardarías {tiempo_dias} días en llegar.")

distancia_km = float(input("Introduce la distancia"))
velocidad_kmh = float(input("Introduce la velocidad"))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
if tiempo_dias>7:
    tiempo_semanas=tiempo_dias//7
    if tiempo_dias%7 > 0:
        dias=tiempo_dias%7
        print(f"Tardarías {int(tiempo_semanas)} semanas y {int(dias)} días en llegar.")
    else:
        print(f"Tardarías {int(tiempo_semanas)} semanas en llegar")
else:
    print(f"Tardarías {int(tiempo_dias)} días en llegar.")