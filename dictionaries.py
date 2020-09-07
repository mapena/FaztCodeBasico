productos = {
    "nombre": "libro1",
    "cantida": 4,
    "precio": 4.99
}
print(productos) # imprimo productos que es un tipo dictionary, formado por variables clave,valor
print(dir(productos))

print(productos.keys()) # nos da las claves ==> nombre, cantidad y precio

# una lista formada por dictionarios

listprod=[
    {"nombre": "libro1", "cantida": 4},
    {"nombre": "libro2", "cantida": 6}
]
print(listprod)