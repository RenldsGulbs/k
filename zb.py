dati_ievads=input("Ievadi savu vārdu un uzvārdu:")

with open ('ziemat.txt', 'w', encoding='utf8') as bams:
    bams.write(dati_ievads)