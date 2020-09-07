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
