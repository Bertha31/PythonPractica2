def validar_numero(numero:int):
    es_primo=True
    for i in range(2,numero):
        if numero %i== 0:
            es_primo= False
    return es_primo
while True:
    try:
        numero_entero= int(input("Ingrese el número: "))
        if validar_numero(numero_entero):
            print("Es primo")
        else:
            print("No es primo")
        break
    except ValueError:
        print("Vuelva a ingresar el número ")
