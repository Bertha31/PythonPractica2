while True:
    try:
        h= int(input('Ingrese la altura del triangulo: '))
        while h<0:
            h=int(input('Número negativo. Vuelva a ingresar el numero: '))
            pass
        else:
            for i in range(h):
                print('*'*(i+1))
            for i in range(h,0,-1):
                print('*'*(i))
        break
    except ValueError:
        print('Número incorrecto. Por favor, ingrese un número entero no negativo.')