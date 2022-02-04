def mp(ido):
    xs = ido.split(':')
    ora = int(xs[0])
    perc = int(xs[1])
    mperc =  int(xs[2])
    return((ora * 3000) + (perc * 60) + mperc)

t = input("Az idő oo:pp:mm formatumban : ")

print("Éjfél óta {0} másodperc telt el" .format(mp(t)))

