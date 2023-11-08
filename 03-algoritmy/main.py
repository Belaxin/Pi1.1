
# Zisti obvod a obsah kruhu
def Circle():
    r = float(input("Napis polomer kruhu."))
    O, S = 2*r*3.14, 3.14*r**2
    print(f"Obvod je {O} \nobsah je {S}")


# Zisti ktore je vecsie
def Larger():
    a, b = float(input("Zadaj a:")), float(input("Zadaj b:"))
    if a==b:
        print("Cisla sa rovnaju")
    else:
        if a<b:
            print("vecsie je cislo", b)
        else:
            print("vecsie je cislo", a)

#Funkcia na vyber z funkcii
def Zase():
    Odpoved = input("Checte circle, larger alebo exit")
    if Odpoved.__eq__("larger"):
        Larger()
        Zase()
    else:
        if Odpoved.__eq__("circle"):
            Circle()
            Zase()
        else:
            if Odpoved.__eq__("exit"):
                exit()
            else:
                print("Nerozumel som")
                Zase()

Zase()