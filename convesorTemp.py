print("\t\t\t\t\tConversor de Temperatura\n")

def celsiusFahrenheit(num):
    return (num * 9/5) + 32
    
def celsiusKelvin(num):
    return num + 273.15
    
def fahrenheitCelsius(num):
    return (num - 32) * 5/9
    
def fahrenheitKelvin(num):
    return (num - 32) * 5/9 + 273.15

def kelvinCelsius(num):
    return num - 273.15

def kelvinFahrenheit(num):
    return (num - 273.15) * 9/5 + 32
    
print("""
1. Celsius para Fahrenheit
2. Celsius para Kelvin
3. Fahrenheit para Celsiu
4. Fahrenheit para Kelvin
5. Kelvin para Celsius
6. Kelvin para Fahrenheit
""")

op = int(input("Escolha uma opção: "))

if op < 1 or op > 6:
    print("Escolha uma opção válida")
else:
    num = int(input("Insira o valor a ser convertido: "))
    if op == 1:
        print(f"{num}ºC é igual a {celsiusFahrenheit(num):.2f}ºF")
    elif op == 2:
        print(f"{num}ºC é igual a {celsiusKelvin(num):.2f}K")
    elif op == 3:
        print(f"{num}ºF é igual a {fahrenheitCelsius(num):.2f}ºC")
    elif op == 4:
        print(f"{num}ºF é igual a {fahrenheitKelvin(num):.2f}K")
    elif op == 5:
        print(f"{num}K é igual a {kelvinCelsius(num):.2f}ºC")
    elif op == 6:
        print(f"{num}K é igual a {kelvinFahrenheit(num):.2f}ºF")

