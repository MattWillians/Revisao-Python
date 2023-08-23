from math import pow
print("Calculadora de IMC (indice de massa corporal)")   

decisao = True
while(decisao == True):
    try:
        peso = float(input("Digite seu peso: "))
        altura = float(input("Digite sua altura: "))
        imc = peso / pow(altura, 2)

        print("-> Seu IMC é: %.2f \n" % imc)
        
        if imc < 18.5:
            print("IMC < 18,5kg/m2 - baixo peso")
        elif imc > 18.5 and imc <= 24.9:
            print("IMC > 18,5 até 24,9kg/m2 - eutrofia (peso adequado)")
        elif imc >= 25 and imc <= 29.9:
            print("IMC ≥ 25 até 29,9kg/m2 - sobrepeso")
        elif imc >= 30.0 and imc <= 34.9:
            print("IMC > 30,0kg/m2 até 34,9kg/m2 - obesidade grau 1")
        elif imc >= 35.0 and imc <= 39.9:
            print("IMC > 35kg/m2 até 39,9kg/m2 - obesidade grau 2")
        else:
            print("IMC > 40kg/m2 - obesidade extrema")
            
        resp = input("Deseja medir novamente?")
        decisao = False if resp.lower() == "n" else True

    except ZeroDivisionError:
        print("Não é possivel calcular o IMC usando valores nulos.")
    except ValueError:
        print("Algo digitado não é um numero, use ponto para separar valores.")
    except: 
        print("Erro encontrado...")