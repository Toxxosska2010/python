class negyzet:
    def __init__(self,a):
        self.a = a

    def kerulet(self):
        return(4*self.a)

    def terulet(self):
        return(self.a**2)

a = float(input("A négyzet szama : "))
n = int(input("A negyzetek oldalhossza : "))
lista = []

for i in range(0,n):
    lista.append(negyzet(i*a))
    
for i in range(0,n):
    print(f"A {i} negyzet kerulete : {lista.[i].kerulet()}.")
    print(f"A {i} negyzet terulete : {lista.[i].terulet()}.")


