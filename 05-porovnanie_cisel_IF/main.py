a = float(input("Napis prosim cislo 1 "))
b = float(input("Napis prosim cislo 2 "))
c = float(input("Napis prosim cislo 3 "))
d = float(input("Napis prosim cislo 4 "))
e = float(input("Napis prosim cislo 5 "))
# Inputy

"""
###
if a==b==c:
    print("Vsetku su rovne")
else:
    if a < b:
        if a == b == c:
            print("Vsetky su rovne")
        else:
            if b > c:
                print("Najvecsie je ",b)
            else:
                print("Najvacsie je ",c)
    else:
        print("Najvacsie je ",a)

# kontroluje velkost
"""

Max = a


if Max < b:
    Max = b
if Max < c:
    Max = c
if Max < d:
    Max = d
if Max < e:
    Max = e

def printMax():
    print("Najvacsie je ", Max)
