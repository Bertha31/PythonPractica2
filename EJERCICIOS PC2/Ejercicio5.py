def validacion(numero, digito):
    numero_str=str(numero)
    cantidad=numero_str.count(str(digito))
    return cantidad
while True:
    try:
        numero1 = int(input('Ingrese el número: '))
        digito1= int(input('Ingrese el digito: '))
        print(f"Número ingresado: {numero1}") 
        print(f"Digito: {digito1}") 
        print(f"Cantidad de veces {digito1} en el número: {validacion(numero1,digito1)}")
        break
    except ValueError:
        print('Digitación incorrecta. Ingrese el número de nuevo')