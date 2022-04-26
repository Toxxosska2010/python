szam = int(input("Adj meg egy szamot : "))  
if szam > 1: 
   for i in range(2,szam):
       if (szam % i) == 0:
               print(szam,"Nem primszam")
               break
   else:
       print(szam,"Ez egy primszam")
            

else:
   print(szam,"Ez nem egy primszam")
