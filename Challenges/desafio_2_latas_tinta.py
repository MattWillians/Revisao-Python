def qtd_latas_tinta(altura_parede, largura_parede, litragem_lata):
    area_total = altura_parede * largura_parede
    print("O total de latas de tinta para uma parede com essas metragens é: ", area_total / litragem_lata, " Latas de tinta")

print("Por favor passe as seguintes informações:")

while True:
    try:
        altura_parede = int(input("Digite a altura da sua parede: "))
        largura_parede = int(input("Digite a largura da sua parede: "))
        litragem_lata = int(input("Digite quantos litros tem em uma lata de tinta: "))
    except:
        print("Digite apenas numeros inteiros...")
        continue
    break
qtd_latas_tinta(altura_parede, largura_parede, litragem_lata)

    
    