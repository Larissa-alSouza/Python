contador = 0

while True:
    print(f"Contador: {contador}")
    acao = input("Digite '+' para aumentar, '-' para diminuir ou 'sair' para encerrar: ")

    if acao == "+":
        contador += 1
    elif acao == "-":
        contador -= 1
    elif acao.lower() == "sair":
        break
    else:
        print("Comando inválido! Use '+' ou '-'.")

print("Programa encerrado.")
