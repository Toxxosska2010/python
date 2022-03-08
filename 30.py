import random

def feltoltes (a):
    for i in range(0,100):
        a.append(random.randint(0,100))

def kiiras(a):
    n = len(a)
    for i in range(0,n):
        print(a[i], end = ",")

def osszegzes(a):
    n = len(a)
    s = 0
    for i in range(0,n):
        s += a[i]
    return(s)

def tulfugg(x):
    return((x>90) and ((x%2) == 0))

def eldontes(a,T):
    n = len(a)
    i = 0
    while((i<n) and (not T(a[i]))):
        i += 1
    return(i<n)

def megszamlalas(a,T):
    n = len(a)
    s = 0
    for i in range(0,n):
        if(T(a[i])):
            s += 1
    return(s)

a = []

feltoltes(a)
kiiras(a)
print()
print("Az elemek osszege : {0} ".format(osszegzes(a)))

if eldontes(a,tulfugg):
    print("Van ilyen elem!")
else:
    print("Nincs ilyen elem!")


print("A felteteleknek megfelelnek : {0} ".format(megszamlalas(a,tulfugg)))
