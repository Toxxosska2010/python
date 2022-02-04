szo1 = input("Adj meg egy szót : ")
szo2 = input("Adj meg egy másik szót: ")

hosszu1 = len(szo1)
hosszu2 = len(szo2)

print("Az elso szo hossza : ",hosszu1)
print("Az masodik szo hossza : ",hosszu2)

i = 1

while i < 2:
    if hosszu1 > hosszu2:
        print("A hosszaab szo az elso")
        i += 1
        
    elif hosszu1 < hosszu2:
        print("A hosszabb szo a masodik")
        i += 1
        
    elif hosszu1 == hosszu2:
        print("A szo hossza ugyan az")
        i += 1
