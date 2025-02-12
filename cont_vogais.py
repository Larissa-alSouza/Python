frase = input("Digite uma frase: ").lower()

vogais = ['a', 'e', 'i', 'o', 'u']
contador_vogais = 0

for letra in frase:
    if letra in vogais:
        contador_vogais += 1

print(f"A frase digitada tem {contador_vogais} vogais.")
