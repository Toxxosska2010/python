def mivan(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

a_oldal = float(input('Írd be az a oldalat : '))
b_oldal = float(input('Írd be a b oldalat : '))
c_oldal = float(input('Írd be a c oldalat : '))
d_oldal = float(input('Írd be a d oldalat : '))

if mivan(a_oldal, b_oldal, c_oldal):
    print('A háromszög lehet.')
else:
    print('A háromszög lehetetlen.')

    x = input("(TERÜLET)A téglalap A oldala : ")
x = int(x)

y = input("(TERÜLET)A téglalap B oldala : ")
y = int(y)

z = x * y
print("A területe :")
print (z)


a = input("(KERÜLET)A téglalap A oldala : ")
a = int(a)

b = input("(KERÜLET)A téglalap B oldala : ")
b = int(b)

c = (a + y)*2 
print("A kerülete :")
print (c)
