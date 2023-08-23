
from array import array

import random
"""
ZIP EM LISTAS
"""

palavras = 'Matheus'
numeros = '1234567890'

lista1 = list(palavras)
lista2 = list(numeros)

print(list(zip(lista1, lista2)))

for palavra, numero in zip(lista1, lista2) :
    print(f'{palavra} + {numero}')
    
"""
USAR O SPLIT


lista_digitada = input("Digite a lista que deseja separada por virgulas ( , )")
lista_digitada = lista_digitada.replace(" ", "")
lista = lista_digitada.split(',')
print(lista)
"""

"""
ARRAYS
"""

palavras = 'escriba, escrivão, escrevente, copista, amanuense, escriturário, escrevedor, notário, escritor, escrevinhador'
lista3 = palavras.split(", ")
print(lista3)

arrau = array('u', ['a','b','c','d'])

print(arrau)

