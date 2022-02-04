#Kérlek írj be egy nevet és állapítsd meg hogy milyen hosszú!
#
#Modulok betöltése
#
#Függvények

def maganhangzok_szama(nev) :
    s = 0

    for i in 'AÁEÉIÍOÓÖŐUÚÜŰaáeéiíoóöőuúüű' :
        s += nev.count(i)
    return(s)

#Programtörzs

nev = input("Név : ")

print ("A név hossza : {0} karakter".format(len(nev)))
print ("A magánhangzók száma : {0} karakter".format (maganhangzok_szama(nev)))
