x = int(input("Meddig szamoljon vissza ? : "))
p = x

while x > 0:
    print(f"Visszaszamlalas : {x} ")
    a = input("Fel akarja adni a visszaszamlalast(i/n) ? : ")

    if a == 'i':
        p += 1
        x -= 1
    else:
        x -= 1

print(f"A visszaszamlalas ennyi oraval indult : {p} ")
        
