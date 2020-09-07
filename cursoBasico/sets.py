# los sets son para definir una colleccion pero no tienen indices.

a={"rojo","verde","azul"}
print(type(a))
print("verde" in a) # devuelve true si "verde" esta dentro de la collecion de set llamado "a"

colores={"rojo","verde","azul"}
colores.add("marron") # agrega un elemento a  la lista y lo inserta al principio
print(colores)

colores.remove("verde") # borra un elemento de la lista
print(colores)

colores.clear() # borra todos los elementos de la lista
print("clear:",colores)