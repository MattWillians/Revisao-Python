dict_pais_capital = ({
                     "Brasil": "Brasilia", 
                     "Estados Unidos": "Washington D.C", 
                     "Portugal": "Lisboa", 
                     "França": "Paris", 
                     "México": "Cidade do México"
                    })

pais_procurado = input("Qual pais você deseja conhecer a capital? ")
pais_encontrado = dict_pais_capital.get(pais_procurado)

if pais_encontrado:
    print(f"A capital de {pais_procurado} é {pais_encontrado}")
else:
    print("Pais não encontrado...")