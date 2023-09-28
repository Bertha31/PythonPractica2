def omitir_vocales(texto):
    vocales = 'aeiouAEIOU'
    resultado = ''
    for letra in texto:
        if letra not in vocales:
            resultado += letra
    
    return resultado

texto1 = input("Ingrese el texto: ")
resultado = omitir_vocales(texto1) 
print("Resultado:", resultado)
