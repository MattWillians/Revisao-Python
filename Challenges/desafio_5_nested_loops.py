lista_frutas = [
    "Abacate",
    "Abacaxi",
    "Açaí",
    "Acerola",
    "Amora",
    "Araticum",
    "Bacaba",
    "Banana",
]

lista_vegetais = [
    "Abóbora", 
    "abobrinha", 
    "acelga", 
    "agrião", 
    "aipo", 
    "alface", 
    "alho", 
    "almeirão"
]

for fruta in lista_frutas:
    for vegetal in lista_vegetais:
        print(f"Eu gosto de comer {fruta} e tambem {vegetal}")
        print(f"Eu Gosto de comer {vegetal} e tambem {fruta}")