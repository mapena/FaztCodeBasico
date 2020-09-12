def funcion1():
    print("fun1")
    try:
        5/0
    except ZeroDivisionError:
        print("Division no permitida")
    return


def funcion2():
    print("fun2")
    try:
        f = open("c:\\Users\mp\Desktop\Archivo.txt", "r")
    except IOError:
        print("No existe archivo")
       # raise si se habilita la sentencia raise el programa cancela
    return

def funcion3():
    print("fun3")
    archivo = None
    try:
        # 5/0
        archivo = open("c:\\Users\mp\Desktop\Archivo.txt", "r")
        # float("MitoCode")
    except ZeroDivisionError:
        print("División no válida")
    except (IOError, ValueError):
        print("Lectura/Escritura Error")
    except ValueError:
        print("Tipo dato no válido")
    except Exception:
        print("Excepción general")
    finally:
        if archivo is not None:
            archivo.close()
    return


def funcion4():
    print("fun4")
    try:
        # open("/home/mitocode/no_file.txt", "r")
        ## raise ValueError()
        #raise TypeError("...type error...")
        raise Exception("...exception...")
        
    except ValueError as ex:
        # print(ex)
        raise
    except Exception as ex:
        print(ex)
    return


funcion1()
funcion2()
funcion3()
funcion4()
