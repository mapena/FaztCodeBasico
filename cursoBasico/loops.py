numeros=[10,5,20,25,30,50,60]
for x in numeros:
    print("numeros", x)
    if x == 20:
        print("salgo")
        break

for x in numeros:
    if x == 20:
        continue # vuelve al bucle salteando las instrucciones sig.
    print("numeros", x)

numeros=range(1,10)
for x in numeros:
    print("x=",x )

letras="marcelo"
for x in letras:
    print("x=",x )
print("while")
x = 1
while x < 10:
    print("x",x)
    x += 1  #  += es igual a x= x + 1

for x in range(3):
    print("Iteración N° " + str(x))
    if x == 1:
        print("Se corto la interación N° " + str(x))
        break

for x in "Mit0C0de":
    if x.isdigit():
        print("Es número")
    print(x, end="\n")