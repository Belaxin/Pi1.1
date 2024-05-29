fmena = open('mena.txt','r', encoding='utf-8')
fpriezviska = open('priezviska.txt','r', encoding='utf-8')
fmenapriezviska = open('mena_priezviska.txt', 'w', encoding='utf-8')  # W otvori subor na zapis, ak neexistuje tak sa vytvori, ak existuje vymaze contents
for meno in fmena:
    priezvisko = fpriezviska.readline()
    print(f'{meno.strip()} {priezvisko.strip()}')
    fmenapriezviska.write(f'{meno.strip()} {priezvisko.strip()}\n')

fmena.close()
fpriezviska.close()
fmenapriezviska.close()