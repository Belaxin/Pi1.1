retazec = input("zadaj retazec: ")
# normalne
for i, znak in enumerate(retazec):
    print(i, znak)
# nenormalne
for i, znak in reversed(list(enumerate(retazec))):
    print("|", i, "|", znak)
#
# for i,znak in -enumerate(retazec):
#     print(i, znak)


