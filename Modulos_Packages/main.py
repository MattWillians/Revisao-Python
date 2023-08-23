# import funcoes_legais
# from funcoes_legais import carregar_bateria
# from funcoes_legais import alertar_bateria

from funcoes_legais import carregar_bateria as carregar, alertar_bateria as alertar
from package import ligar_telefone

print("programa principal")
alertar()
carregar()
ligar_telefone.ligar_aparelho()
ligar_telefone.apresentar_logo()