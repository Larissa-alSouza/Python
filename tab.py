print("\t\t\t\t\t\tGerador de tabuada\n\n")

num = int(input("Insira um número: "))

for i in range(0, 11):
    tab = num * i
    print(str(num) + " X " + str(i) + " = " + str(tab))
