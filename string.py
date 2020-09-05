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

