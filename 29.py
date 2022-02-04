szam1 = int(input("Add meg az 1. szamot : "))
szam2 = int(input("Add meg a 2. szamot : "))
szam3 = int(input("Add meg a 3. szamot : "))

if szam1 + szam2 == szam3 :
    print("Elso es a masodik szamnak az osszege : ",szam3)


elif szam2 + szam3 == szam1 :
    print("Masodik es a harmadik szamnak az osszege : ",szam1)


elif szam1 + szam3 == szam2 :
    print("Elso es a harmadik szamnak az osszege : ",szam2)


else :
    print("A szam nem lehet egyenlo eggyik szammalal se")
