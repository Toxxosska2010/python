def elerte(pont):
    return(pont >= 48)

while True:
    vizsgazo = input("Adja meg a vizsgazo nevet : ")
    if vizsgazo == "":
        break

    pontszam = int(input("Adj meg a pontszamat : "))

    if elerte(pontszam):
        print(f"Sikeres")
    else:
        print(f"Szopas")
    break

