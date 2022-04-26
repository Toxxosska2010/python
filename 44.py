import random

def fejiras(szamlalas):
    
    irasszam = 0
    fejszam = 0
    
    for i in range(szamlalas):
        rand = random.randint(1,2)

        if rand == 1:
            irasszam += 1
           
            print(irasszam, 'iras')
        
        else:
            fejszam += 1
            print(fejszam, 'fej')
   
    print('IRAS : ', irasszam)
    print('FEJ : ', fejszam)
    
fejiras(3)
