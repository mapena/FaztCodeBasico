def hello(var="cachirulo"): # var="cachirulo" se define un valor x defaul en caso de invocar a la funcion
    print("hola:",var)      # sin parametros

hello("marce")
hello()

def sumar(n1,n2): # retorna un valor al funcion
    return n1+n2

print(sumar(10,5))

add2 = lambda n1,n2 : n1+n2 # funcion lambda se define en el momento
print(add2(5,3))            # add2 = nombre de la funcion
                            # n1,n2 = variables de entrada
                            # : fin de los
                            # n1+n2 es lo que tiene que hacer la funcion

def sumar(number1, number2=20):
    print (number1) # 15
    print (number2) # 10
    print (number1 + number2)

sumar(number2=10, number1=15) # 25 se le pasa a la funcion los parametros con sus valores

def sumar(**numbers):  # se recibe dictionarios como parametros
    print (numbers) # {'number1' : 10, 'number2' : 20}
    print (numbers['number1'] + numbers['number2'])

sumar(number1=10, number2=20) # 30   
#---------------------------------------------------------------
#---------------------------------------------------------------
def standard_arg(arg):  # funcion comun se le puede pasar el valor o el nombre del parametro con su valor
    print("standard_arg")
    print(arg)

def pos_only_arg(arg, /): # funcion con parametros posisiconales
    print("pos_only_arg")
    print(arg)

def kwd_only_arg(*, arg): # funcion con parametros x palabra
    print("kwd_only_arg")
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print("combined_example")
    print(pos_only, standard, kwd_only)

#
standard_arg(2)     # solo el valor del parametro
standard_arg(arg=2) # se pasa el nombre del parametro con el valor (nombre del parametro=variable)

#
pos_only_arg(1)
#pos_only_arg(arg=1) # ==> Generea error porque al ser posicional no se le pasa el parametro solo el valor

#
kwd_only_arg(arg=3)
#kwd_only_arg(3) # ==> Generea error porque se le debe pasar el aparametro con el valor

#combined_example(1, 2, 3) # genera error porque el 3er parametro es x con el nombre del parametro
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # genera error x que el 2do parametro es posicional 
                                                    # y no se debe mandar el nombre del parametro
def foo(name, /, **kwds):
    print("foo")
    return 'name' in kwds

foo(1, **{'name': 2})                                                
#----------------------------------------------------------------------------------
def concat(*args, sep="|"):
     return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

