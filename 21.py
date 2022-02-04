i = 1

while i < 2:
    nev = input("Add meg a felhasználó nevét: ")
    jelszo = input("Add meg a felhasználó jelszavát: ")

    if (nev == "bori99") and (jelszo == "Szivecske"):
        print("Belépés engedélyezve")
        i += 1

    else:
        print("Belépés megtagadva")
