print("Adj meg egy szamot : ")



cel = float(input())
fah = (cel - 32)/1.8


inp = input("Valaszd az 1-est ha celsiusba es valaszd a 2-est ha Fahrenheitba : ")
if inp == "1":
    print(cel)
    # whatevercodeyouwant_1()
elif inp == "2":
    print(fah)
    # whatevercodeyouwant_2()
else:
    print("You must choose between 1 or 2")
