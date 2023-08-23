lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
segunda_lista_de_numeros = [10,9,8,7,6,5,4,3,2,1]
num_fix = 9

somaNum = lambda x, y: x * y

result = map(somaNum, lista_de_numeros, [num_fix] * 10)
print(list(result))