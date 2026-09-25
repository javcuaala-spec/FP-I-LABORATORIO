distancia=int(input("Introduce distancia total en km"))
paradas=distancia//150000
repostaje_prim=150000
print(f"Parada en el km {repostaje_prim}")
while (repostaje_prim+150000) < distancia :
    repostaje_prim+=150000
    print(f"Parada en el km {repostaje_prim}")
print(f"Total de paradas para repostar {paradas}")
    
