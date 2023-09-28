numeros_total= []
pares =0
impares=0
while True:
    ingreso= input('¿Desea ingresar un número? (SI/NO): ')
    ingreso= ingreso.lower()
    while ingreso != 'si' and ingreso != 'no':
        ingreso=input('Digitación incorrecta. Vuelva a ingresar: ')
    if ingreso == 'si': 
        try:
            numero= float(input('Ingrese número: '))
            numeros_total.append(numero)
            if numero %2 == 0:
                pares += 1
            else:
                impares += 1

        except ValueError:
            print("Por favor, ingrese un número válido.")
    if ingreso == 'no':
        break
print(f"Números ingresados: {numeros_total}")
print(f"La cantidad de numeros pares son: {pares}")
print(f"La cantidad de numeros impares son: {impares}")
