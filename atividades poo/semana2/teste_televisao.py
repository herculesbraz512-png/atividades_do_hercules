from televisao import Televisao

tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

televisores = [tv1, tv2, tv3]

tv1.ligada = True
tv2.ligada = True

tv1.canal = 5
tv1.volume = 25

tv2.canal = 12
tv2.volume = 70

quantidade_ligadas = 0
maior_televisor = None
soma_polegadas = 0

for tv in televisores:
    soma_polegadas += tv.polegadas
    if tv.ligada:
        quantidade_ligadas += 1
        print(f"{tv.marca} {tv.polegadas}\" | Ligada | Canal {tv.canal} | Volume {tv.volume}")
    else:
        print(f"{tv.marca} {tv.polegadas}\" | Desligada")
    if maior_televisor is None or tv.polegadas > maior_televisor.polegadas:
        maior_televisor = tv

media = soma_polegadas / len(televisores)      

print("\nTelevisores ligados:", quantidade_ligadas)
print(f"Maior televisor: {maior_televisor.marca} {maior_televisor.polegadas}\"")
print(f"Média de polegadas: {media:.2f}")