def sumar(**numbers):  # se recibe dictionarios como parametros
    print (numbers) # {'number1' : 10, 'number2' : 20}
    print (numbers['number1'] + numbers['number2'])

sumar(number1=10, number2=20) # 30