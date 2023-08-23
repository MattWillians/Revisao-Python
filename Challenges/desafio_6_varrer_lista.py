lista_carros = [
    "Gol",
    "HB20",
    "Onix",
    "Mobi",
    "Argo",
]

opcao = input("Qual carro esta procurando? ")
if lista_carros.__contains__(opcao):
    print(f"O carro: {opcao} foi encontrado na base.")
else:
    print("Carro não encontrado.")
    
"""
Opção alternativa:
if opcao in lista_carros:
    print(f"O carro: {opcao} foi encontrado na base.")
else:
    print("Carro não encontrado.")
"""
