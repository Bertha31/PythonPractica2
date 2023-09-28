def fibo(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

# Calculamos y mostramos los números de la serie hasta llegar a 50
x = 0
while fibo(x) <= 50:
    print(fibo(x))
    x += 1

