#Criando as funções de cada operação
def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    #Iniciando o tratamento de erro
    try:
        return a / b
    
    #Fazendo o tratamento de erro se o segundo número for 0
    except ZeroDivisionError:
        return "Erro: Não existe divisão por 0."


#Iniciando o loop
while True:
    try:
        #Criação do Menu
        print("\n")
        print("Calculadora Simples")
        print("-"*30)
        print("""1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair""")
        print("-"*30)
        
        #Recebendo a operação do usúario
        escolha = int(input("Escolha uma opção acima: "))

        #Iniciando o tratamento das operações
        if 1 <= escolha <= 5:
            
            #Saindo do programa caso o usúario escolha 5
            if escolha == 5:
                print("Saindo do Programa...")
                break

            #Recebendo os números para fazer a operação escolhida
            a = int(input("\nDigite o primerio número: "))

            b = int(input("\nDigite o segundo número: "))
        
            #Fazendo o calculo e exibindo o resultado na tela
            if escolha == 1:
                resultado = soma(a, b)
                print("-"*30)
                print(f"{a} + {b} = {resultado}")
                print("-"*30)

            #Fazendo o calculo e exibindo o resultado na tela
            elif escolha == 2:
                resultado = subtrair(a, b)
                print("-"*30)
                print(f"{a} - {b} = {resultado}")
                print("-"*30)

            #Fazendo o calculo e exibindo o resultado na tela
            elif escolha == 3:
                resultado = multiplicacao(a, b)
                print("-"*30)
                print(f"{a} x {b} = {resultado}")
                print("-"*30)

            #Fazendo o calculo e exibindo o resultado na tela
            elif escolha == 4:
                resultado = divisao(a, b)
                print("-"*30)
                print(f"{a} / {b} = {resultado}")
                print("-"*30)

        #Tratando caso a pessoa não escolha uma das opções desejadas
        else:
            print("\nErro! Insira um número referente a uma operação.")

    #Tratamento de erro caso a pessoa não digite um número
    except ValueError:
        print("\nInsira apenas números.")
        