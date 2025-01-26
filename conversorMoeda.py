print("\t\t\t\t\tConversor de Moeda: Real --> Dólar\n\n")

print("Dólar no dia 26/01/2025 R$5,91\n")

dolar = 5.91

valor = float(input("insira o valor que você quer converter: "))

def conversor(dolar, valor):
    
    resultado = dolar * valor
    
    print("O valor convertido é de: " + str(resultado))

print()

conversor(dolar, valor)
