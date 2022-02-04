i = 1
while i < 2:
    nev = input("Add meg a vizsgazo nevet : ")
    pont = int(input("Add meg a pontszamat : "))

    if nev == "":
        print("Add meg a vizsgazo nevet : ")
        break

    if pont < 100 :
        print(nev," vizsgaja sikertelen")
        break

    if pont > 100 :
        print(nev," vizsgaja sikeres")
        break
