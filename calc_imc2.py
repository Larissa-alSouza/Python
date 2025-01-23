print("\t\t\t\t\t\t Calculadora de IMC \n\n")

peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / altura**2

if imc <= 18.5:
    print("Seu IMC é de: " + str(imc) + ". Você está abaixo do seu peso normal")
elif imc >= 18.6 and imc <= 24.9:
    print("Seu IMC é de: " + str(imc) + ". Você está no seu peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Seu IMC é de: " + str(imc) + ". Você está com sobrepeso")
elif imc >= 30 and imc <= 34.9:
    print("Seu IMC é de: " + str(imc) + ". Você está com obesidade grau I")
elif imc >= 35 and imc <= 39.9:
    print("Seu IMC é de: " + str(imc) + ". Você está com obesidade grau II")
else:
    print("Seu IMC é de: " + str(imc) + ". Você está com obesidade grau III")
