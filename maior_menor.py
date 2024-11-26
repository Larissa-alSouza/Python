num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def verificarNumeros(num1, num2):
    if num1 > num2:
        print("O maior número é: " + str(num1))
    else:
        print("O maior número é: " + str(num2))

verificarNumeros(num1, num2)
