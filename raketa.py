i = int(input("Hány órás visszaszámlálást tervezünk? "))

v = i
u = i
for v in range(i):
    print("Visszaszámlálás : {0}".format(i))
    i = i - 1
    szam = str(input("Felfüggesszük a számlálást (i/n)"))
    if szam == "i":
        u = u + 1
    elif szam == "n":
        u = u

print("Az eltelt idő {0} óra volt".format(u))
