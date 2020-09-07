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