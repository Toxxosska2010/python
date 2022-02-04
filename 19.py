ora = int(input("Mennyi az idő:"))

if ora >= 8 and ora <= 16:
    print("A bolt nyitva van még {0} órád van odaérni!".format(16-ora))

else:
    if (ora < 8 ):
         print("A bolt zárva van".format(8-ora))
    else:
        print("A bolt nyitva van".format(+8(24-ora)))

