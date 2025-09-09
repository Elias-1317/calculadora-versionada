def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b!=0:
        resultado = a / b
        
        return resultado
    else:
        return "Erro: Não existe divisão por 0."
   
    

while True:
    try:
        print("\nCalculadora Simples")
        print("-"*30)
        print("""
        1. Soma
        2. Subtração
        3. Multiplicação
        4. Divisão
        5. Sair
          """)

        escolha = int(input("Escolha uma opção acima: "))

        if 1 <= escolha <= 5:

            if escolha == 5:
                print("Saindo do Programa...")
                break
                
            a = float(input("Digite o primerio número: "))

            b = float(input("\nDigite o segundo número: "))
        
            if escolha == 1:
                resultado = soma(a, b)
                print(f"{a} / {b} = {resultado:.2f}")

            elif escolha == 2:
                resultado = subtrair(a, b)
                print(f"{a} / {b} = {resultado:.2f}")

            elif escolha == 3:
                resultado = multiplicacao(a, b)
                print(f"{a} / {b} = {resultado:.2f}")

            elif escolha == 4:
                resultado = divisao(a, b)
                print(f"{a} / {b} = {resultado:.2f}")

            
        else:
            print("Erro! Insira um número referente a uma operação.")

    except ValueError:
        print("Insira apenas números.")
        