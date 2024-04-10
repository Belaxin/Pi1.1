retazec = 'Ahoj svet'
print(retazec)
print(retazec[0])
print(retazec[len(retazec) - 1])
# for i in range(len(retazec)):
#     print(i , retazec[i])


# retazec[0] = 'a'    toto nieje dovolene


# i = 0
# for znak in retazec:
#     print(i, znak)
#     i+=1
#


for i, znak in enumerate(retazec):
    print(i, znak)

print(retazec[-1])
