numeros = []

for i in range(6):
    num = float(input("Digite um número: "))
    numeros.append(num)

def verificarPares():
    print("Pares:")
    for j in numeros:
        if j % 2 == 0:
            print(j)

def verificarImpares():
    print("Ímpares:")
    for y in numeros:
        if y % 2 != 0:
            print(y)

verificarPares()
verificarImpares()
