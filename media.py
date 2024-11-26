notas = []

for i in range(5):
    ra = input("Digite o R.A. do aluno: ")
    p1 = float(input("Digite a nota da p1 do aluno: "))
    p2 = float(input("Digite a nota da p2 do aluno do aluno: "))
    qz = float(input("Digite a nota de quiz do aluno: "))
    ot = float(input("Digite a nota de outros do aluno: "))
    mf = (p1 * 0.3) + (p2 * 0.3) + (qz * 0.2) + (ot * 0.2)

    if mf < 5:
        print("O aluno está reprovado com a média de: {:.2f}".format(mf))
    elif 5 <= mf < 7:
        print("O aluno está de recuperação com a média de: {:.2f}".format(mf))
    else:
        print("O aluno foi aprovado com a média de: {:.2f}".format(mf))

    notas.append(mf)

print("As médias dos alunos foram: ", notas)