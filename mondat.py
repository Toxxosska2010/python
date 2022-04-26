mondat = input("Kérem írjon be egy mondatot: ")
hossz = len(mondat)

def szabalyos(mondat):
    a = 1
    t = mondat.capitalize()
    
    if mondat == t:
        if mondat[-1] == "?" or "!" or ".":
            a += 1
    else:
        pass

    if a == 1:
        print("A mondat nem szabályos.")
    else:
        print("A mondat szabályos.")


print("A mondat hossza: {0} karakter".format(hossz))

szabalyos(mondat)
