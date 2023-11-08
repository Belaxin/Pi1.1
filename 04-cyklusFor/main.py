n = int(input("Zadaj pocet opakovani: "))
slovo = input("Co chces opakovat: ")

for i in range(n): # cislo v zatvorke za range je pocet opakovani
    print(slovo,  i+1)
    i+=1