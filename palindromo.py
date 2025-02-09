def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower() 
    return palavra == palavra[::-1]

palavra = input("Digite uma palavra ou frase: ")

if verificar_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo!')
else:
    print(f'"{palavra}" não é um palíndromo.')
