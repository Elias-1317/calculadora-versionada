def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b
    
print("Calculadora Simples")
print("-"*30)
print("""
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
      """)

escolha = int(input("Escolha uma opção acima: "))

a = float(input("Digite o primerio número: "))

b = float(input("\nDigite o segundo número: "))

if escolha == 1:
    resultado = soma(a, b)
    print(f"{a} + {b} = {resultado:.2f}")

elif escolha == 2:
    resultado = subtrair(a, b)
    print(f"{a} - {b} = {resultado:.2f}")

elif escolha == 3:
    resultado = multiplicacao(a, b)
    print(f"{a} x {b} = {resultado:.2f}")

elif escolha == 4:
    try:
        b == 0
        resultado = divisao(a, b)
        print(f"{a} / {b} = {resultado:.2f}")

    except ZeroDivisionError:
        print("Erro: Não existe divisão por 0.")
        