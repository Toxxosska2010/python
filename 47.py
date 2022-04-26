a = int(input("A 1. megállónál felszállók száma:"))
b = int(input("A 2. megállónál felszállók száma:"))
c = int(input("A 3. megállónál felszállók száma:"))
d  = int(input("A 4. megállónál felszállók száma:"))
e  = int(input("A 5. megállónál felszállók száma:"))
f  = int(input("A 6. megállónál felszállók száma:"))
g  = int(input("A 7. megállónál felszállók száma:"))
h = int(input("A 8. megállónál felszállók száma:"))
i  = int(input("A 9. megállónál felszállók száma:"))
j = int(input("A 10. megállónál felszállók száma:"))

osszes = a + b + c + d + e + f + g + h + i + j ;
atlag = osszes / 10 ;

print ("Az iskolánál {0} tanuló fog leszállni a buszról.".format(osszes))
print ("A megállókban az átlagosan felszálló tanulók száma {0} fő.".format(atlag))
