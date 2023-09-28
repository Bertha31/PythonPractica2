h= int(input('Ingrese la altura del triangulo: '))
while h<0:
    print('Número incorrecto')
    h=int(input('Vuelva a ingressar el numero: '))
    pass
else:
    for i in range(h):
        print('*'*(i+1))
    for i in range(h,0,-1):
        print('*'*(i))
