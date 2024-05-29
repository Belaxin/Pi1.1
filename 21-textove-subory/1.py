fmena = open('mena.txt','r', encoding='utf-8')  # Otvori subor mena.txt na citanie 'r' je read only, 'w' je write only
fpriez = open('priezviska.txt','r', encoding='utf-8')
# fmena = open('C:/dokumenty/mena.txt','r')    absolutna cesta k suboru
while True:
    riadok = fmena.readline()
    riadok2 = fpriez.readline()

    print(riadok[:-1], riadok2[:-1]) # Vypise vsetky znaky od nulteho po -1 (predposledny)
    if riadok ==  '':
        break

fmena.close() # zatvori file, vzdy robit