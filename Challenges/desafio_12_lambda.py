cubo = lambda x: x**3
quadrado = lambda x: x**2

multiplicar = lambda x, y: x * y
par_ou_impar = lambda x: "Par" if (x % 2 == 0) else "Impar"

print(cubo(2))
print(multiplicar(2,2))
print(par_ou_impar(4))
print(par_ou_impar(9))

lista_numero = [1,2,3,4,5,6,7,8,9,10]
lista_ao_quadrado = [quadrado(num) for num in lista_numero]

print("", lista_numero,"\n",lista_ao_quadrado)