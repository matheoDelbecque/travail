#exercice 1

range(2,9)
range(0,25,4)
maChaine = "informatique"
print(list(range(maChaine)))

#exercice 2

for i in range(11):
    print("Pour progresser en programmation, la pratique est le plus important")

#exercice 3

for i in range(1,11):
    print(7*i)
    
for i in range(1,11):
    print("7 *",i,"=",7*i)
    
def tableMultiplication(nb):
    for i in range(1,11):
        print(nb,"*",i,"=",nb*i)
tableMultiplication(3)

def tableMultiplication(nb):
    for i in range(1,11):
        print(nb,"*",i,"=",nb*i)
def plusieursTablesMultiplication(a,b):
    for i in range(a,b+1):
        print(tableMultiplication(i))
plusieursTablesMultiplication(5,9)

#exercice 4

def nombreCaracteres(chaine):
    compteur = 0
    for i in chaine :
        compteur = compteur + 1
    print(compteur)
nombreCaracteres("bonjour")
