def fatorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado

print(fatorial(3))