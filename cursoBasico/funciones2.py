
# se define un dictionario que por default tiene 2 valores
# la moneda y su valor de cambio
#
divisas = {"PEN": 3.256 , "MXN":20}

def definir_tipo_cambio(tipo_moneda, valor_cambio):
    divisas[tipo_moneda]=valor_cambio
    return

def convertir(monto_inicial,tipo_moneda="PEN"):
    valor=divisas.get(tipo_moneda) # usa el metodo get por que esta definido en la clase dictionary
                                   # es lo mismo que referenciarlo asi:
                                   # divisas[tipo_moneda]
    
    monto_final=monto_inicial / valor
    return monto_final

print("ingrese la moneda y tipo de cambio separado por coma:") # Ingrasar=Ar$,102 
                                                               # (102 por que es el valor del dolar turista)
texto=str(input()).split(",") # genero una lista con 2 elementos, 1) Ar$ y 2) 102
moneda=texto[0]
valor_cambio=float(texto[1])

definir_tipo_cambio(moneda,valor_cambio)
print("ver divisas:")
print(divisas)
print("ingrese el monto a convertir de " + moneda + " a U$$")
monto=float(input())
resultado=convertir(monto,moneda)
print(str(monto) + " " + str(moneda) + " en u$$ es:" + str(resultado))
