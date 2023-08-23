from math import factorial


numero_a_fatorar = 600
# Solução rapida
print(factorial(numero_a_fatorar))

# Solução logica
def fatorar(numero):
        
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorar(numero - 1) 

print(fatorar(numero_a_fatorar))