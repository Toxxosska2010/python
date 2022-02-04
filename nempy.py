#Feladat
#Miskolc 2021.09.29
#Készítette Héring Máté (10/A)

szám = int(input("Adj meg egy számot : "))
print("A szám : {0}".format(szám))

print("A szám tizenhatos számrendszerben : {0:10x} .".format(szám))
print("A ketets számrendszerben : {0:20b} ." .format(szám))
print("A szám négyzete : {0:10.2f} ." .format(szám ** 2))
if ((szám % 2) ==0) :
        print("A szám páros.")
else:
        print("A szám páratlan.")
