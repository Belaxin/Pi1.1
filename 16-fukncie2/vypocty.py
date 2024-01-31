def sucet(x, y):
    return x + y


# jednoduch parne
# def parne(cislo):
#   return cislo%2==0
#
def prvocislo(cislo):
    for i in range(2, 10):
        return not cislo % i == 0 and cislo != i or cislo == 1



def parnce(cislo):
    if cislo % 2 == 0:
        return "parne"
    else:
        return "neparne"


a = int(input("zadaj a: "))
b = int(input("zadaj b: "))
print(f"sucet {a} a {b} je {sucet(a, b)}")
print(f"cislo {a} je {parnce(a)}")
print(f"cislo {b} je {parnce(b)}")
if prvocislo(a) == True:
    print(f"cislo {a} je prvocislo")
else:
    print(f"cislo {a} nieje prvocislo")
if prvocislo(b) == True:
    print(f"cislo {b} je prvocislo")
else:
    print(f"cislo {b} nieje prvocislo")