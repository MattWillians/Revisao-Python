 

import datetime
class frutas:  
    
    # nome: str
    # sobrenome: str
    # ano_nasc: str

    def __init__(self, nome, sobrenome, ano_nasc): 
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc

    def imprimir_nome(self):
        print("O nome deste usuario e: "+ self.nome)

    def idade_funcionario(self):
        ano = datetime.date.today().year
        print("O funcionario tem: ", int(ano - self.ano_nasc), " Anos")
    
usuarios = []
usuarios.append(frutas("Jacke", "Nascimento", 2003))

usuarios[0].imprimir_nome()
usuarios[0].idade_funcionario()