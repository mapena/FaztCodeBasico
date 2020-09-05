# comentario
""" comentario
    comentario
"""
# string todos diferentes
print("helloword")
print("""helloword""")
print('helloword')
print('''helloword''')
print("hola" + "mundo")  # concatena texto
print(type('''helloword'''))  # type dice que tipo de datos es

# numeros int
print(type(100))  # type dice que tipo de datos es
# numeros float
print(type(100.5))  # type dice que tipo de datos es

# bool de booleano
print(type(False))

# lista
# [10,20,30]
print(type([10, 20, 30]))
print(type(["a", "b", "c"]))
print(type(["a", 1, "b", 2]))

# tuples las tuples no puede ser modiciados como si fuese constantes.
print(type((10, 20, 30)))
print(type(("a", "b", "c")))
print(type(("a", 1, "b", 2)))

# dictectories
# {
#    "nombre": "marcelo"
#    "allias": "twity"
# }

print(type({
    "nombre": "marcelo",
    "allias": "twity" ,
    "edad": 48
    }
))
