mystr = "hello word" 
#dir nos dice que osas se puede hacer con un string
""" dir nos dice metodos y clases
    aparece metodo 
    'upper'  para pasar a mayuscula
    'title'  para por mayucula 1er letra de cada palabra """
print(dir(mystr))

print(mystr.upper())
print(mystr.title())
print(mystr.replace("hello","hola pedorro"))
print(mystr.replace("hello","hola pedorro").upper())
print(mystr.count("l"))  # cuantes veces esta la letra "l"

print(mystr.startswith("h")) # retorna True por que el valor de la variable comienza con "h"
print(mystr.endswith("word")) # retorna True por que el valor de la variable termina con"word"

mystr = "hello word amigos" 
print(mystr.split()) # separa el texto en palabras separador blano x default

mystr = "hello,word amigos" 
print(mystr.split(",")) # separa el texto en palabras defino separador = ","

print(mystr.find("o")) # fusca la primera posicion que aparece la "o"
print(len(mystr))  #v largo de la cadana
print(mystr.index("e")) #dice el nro de posicion de la "e"
print(mystr.isnumeric())  # retorna true/false
print(mystr.isalpha()) # retorna true/false

print(mystr[1]) # retorna la letra de la posicion 1, comienza con la cero.
print(mystr[-1]) # con -1 comienza de atras para adelante.

mystr="marcelo"
print("hola" + mystr) # cocante la mystr con la cadena hola
print("hola", mystr)
print(f"hola como estas: {mystr}") # con la f se le indica que en el texto hay una variable
print("1-hola :{0} {1}".format(mystr,mystr)) # reemplaza x cada variable dentro del format por lo que esta en la llave
                                             # respetando el orden secuencial

                                             