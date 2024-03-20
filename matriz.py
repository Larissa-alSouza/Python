linhas = 3
colunas = 3
B = [[0 for j in range(colunas)] for i in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        B[i][j] = int(input('Digite o elemento da matriz: '))

print(B)
