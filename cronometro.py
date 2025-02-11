import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"⏳ {i} segundos restantes...", end="\r")
        time.sleep(1)
    print("⏰ Tempo esgotado!")

tempo = int(input("Digite o tempo em segundos: "))
cronometro(tempo)
