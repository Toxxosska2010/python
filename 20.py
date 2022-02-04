i = 0

while True:
    szam = float(input("Mennyit ittál ma?"))
    i += szam
    print("Eddig {0:.0f} deciliter folyadékot ittál meg!".format(i))
    if i >= 25:
        print("Megittál 2,5 liter folyadékot!")

    if i >= 35:
        print("Megittál 3,5 liter folyadékot!")
        print("Szia")

    if i == 0:
        print("Igyál még 2,5 liter folyadékot!")
        break
