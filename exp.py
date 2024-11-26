xp = float(input("Digite o seu tempo de experiência: "))

if float(xp) <= 5:
    print("Você é um desenvolvedor júnior")
elif float(xp) >= 6 and float(xp) <= 9:
    print("Você é um desenvolvedor pleno")
else:
    print("Você é um desenvolvedor sênior")