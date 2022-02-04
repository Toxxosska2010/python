szamok = []
harommal = []

for i in range(5):
    szamocska = int(input("Adj meg egy szamt 100 es -100 kozott : "))

    if -100 <= szamocska <= 100:
        szamok.append(szamocska)
        atlaga = (sum(szamok)) /len(szamok)
        if (szamocska % 3) == False:
            harommal.append(szamocska)
           
    else:
        print("Rossz probald meg ujra : ")
i = i - 1         

print("Az alabbi szamokat adtad meg : {0} ".format(szamok))
print("Az alabbi szamok kozul ennyi oszthato 3-al : {0} ".format(len(harommal)))
print("Az alabbi szamok kozul a legkisebb : {0} ".format(min(szamok)))
print("Az alabbi szamok kozul a legnagyobb : {0} ".format(max(szamok)))
print("Az alabbi szamok atlaga : {0} ".format(atlaga))
