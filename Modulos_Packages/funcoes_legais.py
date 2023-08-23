from time import sleep


def carregar_bateria():
    for i in range(5):
        print("Carregando...")
        sleep(1)
    print("Carregado!")

def alertar_bateria():
    print("Bateria baixa, carregue o telefone.")