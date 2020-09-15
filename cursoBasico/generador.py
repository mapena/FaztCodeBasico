"""
--V esta i toma el valor de la i del for y lo multiplica *2
-----------V esta i iteran en el rango 0 a 9
--------------------------V el if estaria dentro del for, donde valida si i es multiplo de 3
"""
x=(i*2 for i in range(10) if i%3 == 0)
for elem in x:
    print(elem)

print("otro generador")
#-----------------------------------------------
x=(min(i,10) for i in range(10) if i%3 == 0)
for elem in x:
    print(elem)
