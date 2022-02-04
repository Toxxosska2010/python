szam1 = int(input('Adj meg egy szamot: '))

szam2 = int(input('Adj meg egy nagyobb szamot: '))

 
if szam1>szam2:

    print("Az elso szamnak kisebbnek kell lennie")



elif szam1<szam2 :

            print(list(range(szam1,szam2)))


else:

    print("Kezd ujra")
