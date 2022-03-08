
szam = []
while True:
    sz= int(input("Adjon meg egy szamot : "))
    szam.append(sz)
    if sz == 0:
        break

print(szam[::-1])
