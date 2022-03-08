a = input("Adj meg egy szot : ")

x = set()
eredmeny = ''

for i in a:
    if i not in x:
        x.add(i)
        eredmeny=eredmeny+str(a.count(i))+i

print("A szoba ennyi betu van : "+eredmeny)
