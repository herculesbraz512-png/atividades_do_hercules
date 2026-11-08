from televisao import Televisao

tv1 = Televisao("Samsung", 43)
tv2 = Televisao("LG", 50)
tv3 = Televisao("Philco", 32)

televisores = [tv1, tv2, tv3]

tv1.ligar()
tv2.ligar()

tv1.trocar_canal(5)
tv1.aumentar_volume(15)

tv2.trocar_canal(12)
tv2.aumentar_volume(60)

if not tv3.trocar_canal(8):
    print("Trocar canal com a TV desligada: False")

if not tv1.ligar():
    print("Ligar de novo a TV 1: False")

if not tv2.trocar_canal(150):
    print("canal 150 na TV 2: False")
    
for tv in televisores:
    print(tv)