k = []

f = open("15 szoveg.txt", "r")

def tavolsag(k):
    return(((k[0]**2)+(k[1]**2))**0,5)

while True:
        sor = f.readline()
        if sor == "":
            break
        koordinatak = sor.rstrip("\n").split(";")
        k.append([float(koordinatak[0]), float(koordinatak[1])])

fir i in k:
    print("({{0},{1}} - {2}".format(i[0], i[0] tavolsag(i)))



f.close()
print(k)

