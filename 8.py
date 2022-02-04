szamok = []

paratlan = []

paros = []

d = 1

v = 0

i = 0

while d < 6:
    number = int(input("adj meg egy számot : "))
    if d <= number <= 99:
        print("Jó a szám ")
        szamok.append(number)
        if (number % 2) == 0:
            paros.append(number)
            d += 1

        if (number % 2) != 0:
            paratlan.append(number)
            i += 1
    elif 1 > number > 99:
        print("Rossz a szám")
    else :
        print("Írd be újra a számot : ")

if v == 0:
    paros.append("Nincsen benne paros szam")
if i == 0:
    paratlan.append("Nincsen benne paratlan szam")


print(

