from sys import getsizeof

def ver1():
    decisao = True
    while(decisao == True):
        
        try:
            steak_temperature= int(input("Digite a temperatura do bife: "))
            
            if (steak_temperature < 48):
                print("Deixe a carne continuar por mais tempo")
            elif (steak_temperature >= 48 and steak_temperature < 54) :
                print("Rare (Selada)")
            elif (steak_temperature >= 54 and steak_temperature < 60) :
                print("Medium Rare (Ao ponto para o mal)")
            elif(steak_temperature >= 60 and steak_temperature < 65) :
                print("Medium (ao ponto)")
            elif(steak_temperature >= 65 and steak_temperature < 71) :
                print("Medium Well (Ao ponto, bem passado)")
            else:
                print("Well done (bem passada)")
        except:
            print("ocorreu um erro ao medir a temperatura...")
        
        resp = input("Deseja medir outra carne? ")
        decisao = False if resp.lower() == "n" else True
    
def ver2():
    decisao = True
    while(decisao == True):
        
        try:
            steak_temperature= int(input("Digite a temperatura do bife: "))
            
            if (steak_temperature < 48):
                print("Deixe a carne continuar por mais tempo")
            elif (steak_temperature in range(48,53)) :
                print("Rare (Selada)")
            elif (steak_temperature in range(54,59)) :
                print("Medium Rare (Ao ponto para o mal)")
            elif(steak_temperature in range(60,64)) :
                print("Medium (ao ponto)")
            elif(steak_temperature in range(65,71)) :
                print("Medium Well (Ao ponto, bem passado)")
            else:
                print("Well done (bem passada)")
        except:
            print("ocorreu um erro ao medir a temperatura...")
        
        resp = input("Deseja medir outra carne? ")
        decisao = False if resp.lower() == "n" else True
        