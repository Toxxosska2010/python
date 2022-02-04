import random

szam = random.randrange(0,100)

kitalal = int(input("Irj be egy szamot 0 es 100 kozott : "))

while kitalal != szam:
    if kitalal < szam :
        print("A szám nagyobb probald ujra ")
        kitalal = int(input("\nIrj be egy szamot 0 es 100 kozott : "))
    else:
         print("A szám kisebb probald ujra ")
         kitalal = int(input("\nIrj be egy szamot 0 es 100 kozott : "))

print("A szamot kitalaltad")
