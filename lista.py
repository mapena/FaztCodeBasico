mylista=list((1,2,3,4)) # la funcion list es para crear una lista o array de numeros. los numeros estan 
                        # entre doble parentesis por que la funcion lista solo acpeta 1 elemento y como se le
                        # pasa una tupla porque esta entre () lo ve como un solo elemento.
print(mylista)

mylista2=list(range(1,10)) # se arma una lista partiendo de la funcion rango para que cargue numero del 1 al 9
print(mylista2)
print(dir(mylista2)) # devuelve que metodos se puede ejecutar para las listas

print(len(mylista2))  # dice cuantos elementos tiene la lista
colores=["rojo","verde","azul"]
print(colores)
print(colores[2]) # muestra el tercer elemento de la lista, la lista la 1ra posicion es cero.
print(colores[-1]) # muestra el ultimo elemento de la lista
print("rojo" in colores) # devuelve true indicando que rojo esta en la lista de colores
colores[1]="violeta" # reemplazo un elemento de la lista

print(colores)

colores=["rojo","verde","azul"]
colores.append("naranja") # agrego un elemento al final de la lista (solo se puede agregar 1 elemento a la vez)
print(colores)

colores.extend(["gris","negro"]) # a diferencia del apend es que por medio de una lista puedo agregar
                                 # mas de 1 elemento  a la lista
print(colores)

colores=["rojo","verde","azul"]
colores.insert(1,"marron") # se le indica que inserte "marron" en la posicion 1, rojo es posicion cero.
print(colores)

colores=["rojo","verde","azul"]
colores.insert(-1,"marron") # se le indica que inserte "marron" en la ultima posicion a partir de la  1, azul es posicion cero.
print(colores)

colores.pop() # borro ultimo elemento de la lista
print(colores)

colores.remove("verde") # se elimiena de la ista el elemento "verde"
print(colores)

colores.clear() # borra todos lo elemento de  la lista
print(colores)

colores=["rojo","verde","azul"]
colores.sort() # ordena la lista
print(colores)
colores.sort(reverse=True) # ordena la lista alrreves
print(colores)

print(colores.index("azul")) # devuelve la posicion del elemento azul
colores=["rojo","verde","azul","rojo"]
print(colores.count("rojo")) # devuelve la cantidada de elemento que existe = "rojo"

