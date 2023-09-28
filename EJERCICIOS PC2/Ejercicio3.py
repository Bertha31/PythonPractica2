numeros_total= []
pares =0
impares=0
while True:
    numero1= input('Desea ingresar un número?: ')
    numero1= numero1.lower()
    while numero1 != 'si' and numero1 != 'no':
        numero1=input('Digitación incorrecta. Vuelva a ingresar: ')
    if numero1 == 'si': 
        try:
            numero2= float(input('Ingrese número: '))
            numeros_total.append(numero2)
            if numero2 %2 == 0:
                pares += 1
            else:
                impares += 1

        except ValueError:
            print("Por favor, ingrese un número válido.")
    if numero1 == 'no':
        break
print(f"Números ingresados: {numeros_total}")
print(f"La cantidad de numeros pares son: {pares}")
print(f"La cantidad de numeros impares son: {impares}")
