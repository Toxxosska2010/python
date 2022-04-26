def monogram():

    nev = input('Add meg a neved : ')
    nev_lista = nev.split()

    for a in nev_lista:
        print(a[0].upper() + ". ", end="")
    print()

monogram()
