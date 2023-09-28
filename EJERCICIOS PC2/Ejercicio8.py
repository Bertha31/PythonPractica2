def calcular_factorial(numero):
    fact=1
    for i in range(1,numero+1):
        fact *= i
    return fact
while True:
    try:
        facto= int(input("Ingrese el número requerido: "))
        while facto<=0:
            facto=int(input("Numero negativo, ingrese el número de nuevo: "))
            pass
        else:
            factorial=calcular_factorial(facto)
            print(f"El factorial del número {facto} es {factorial}")
        break
    except ValueError:
        print("Vuelva a ingresar el número ")
