def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Divisão por zero não é permitida"

def potencia(x, y):
    return x ** y

print("Operações disponíveis: adição, subtração, multiplicação, divisão e potência")
op = input("Escolha a operação desejada: ")
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if op == "adição":
    print(f"O resultado é: {adicionar(num1, num2)}")
elif op == "subtração":
    print(f"O resultado é: {subtrair(num1, num2)}")
elif op == "multiplicação":
    print(f"O resultado é: {multiplicar(num1, num2)}")
elif op == "divisão":
    print(f"O resultado é: {dividir(num1, num2)}")
elif op == "potência":
    print(f"O resultado é: {potencia(num1, num2)}")
else:
    print("Operação inválida")
