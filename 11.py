
# modulok

beker = int(input("Adjon meg egy számot 1 től 100-ig : "))

# függvények

def beker(v):
    for i in range(0,100):
        

def kiir(v):
    for i in range(0,len(v)):
        print(v[i], end='\t')

def osszeg(v):
    s = 0
    for i in range(0,len(v)):
        s += v[i]
    return(s)

def paros(x):
    return((x % 2) == 0)

def paratlan(x):
    return((x % 2) > 0)

def paros_kiir(v):
    for i in range(0,len(v)):
        if paros(v[i]) :
            print(v[i], end=" ")
    print()

def paratlan_kiir(v):
    for i in range(0,len(v)):
        if paratlan(v[i]) :
            print(v[i], end=" ")
    print()

# programtörzs

v = []

beker(v)
kiir(v)

print("A számok összege : {0}.".format(osszeg(v)))

print("A páros számok: ")
paros_kiir(v)
print("A páratlan számok: ")
paratlan_kiir(v)
