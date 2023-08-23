funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa', 'Yasmin']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno', 'Yasmin']
tem_carro = ['Marcos', 'Alice','Ana','Pedro']

funcionarios_carro_noite = set(turno_noite).intersection(tem_carro)
funcionarios_carro_dia = set(turno_dia).intersection(tem_carro)
funcionarios_sem_carro = set(funcionarios).difference(tem_carro)

print(funcionarios_carro_noite, "\n", funcionarios_carro_dia, "\n", funcionarios_sem_carro)