def fibonacci(n):
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def main():
    print("Bem-vindo ao gerador da sequência de Fibonacci!")
    while True:
        entrada = input("Quantos termos você quer gerar? (Digite 'sair' para terminar): ")
        if entrada.lower() == 'sair':
            break
        try:
            n = int(entrada)
            if n <= 0:
                print("Por favor, digite um número inteiro positivo.")
            else:
                sequencia = fibonacci(n)
                print(f"A sequência de Fibonacci com {n} termos é: {sequencia}")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
if __name__ == "__main__":
    main()
