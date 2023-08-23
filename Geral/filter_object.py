lista_de_valores = [554,567,343,565,545,332,]

resultado_bool = lambda x: x > 300

turno_noite = ['Pedro', 'Sophia', 'Bruno', 'Yasmin']
tem_carro = ['Marcos', 'Alice','Ana','Pedro']

print(list(map(resultado_bool, tem_carro))) # retorna os booleans
print(list(filter(resultado_bool, lista_de_valores))) # retorna os valores que bateram com verdadeiro