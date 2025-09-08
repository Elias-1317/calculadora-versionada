def soma(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

print("Calculadora Simples")
print("-"*30)
print("""
1. Soma
2. Subtração
3. Multiplicação
      """)

escolha = input("Escolha uma opção acima: ").lower

a = float(input("Digite o primerio número: "))

b = float(input("\nDigite o segundo número: "))

if escolha == "soma" or "1":
    resultado = soma(a, b)
    print(f"{a} + {b} = {resultado:.2f}")

elif escolha == "subtrair" or "2":
    resultado = subtrair(a, b)
    print(f"{a} - {b} = {resultado:.2f}")

elif escolha == "multiplicação" or "3":
    resultado = multiplicacao(a, b)
    print(f"{a} x {b} = {resultado:.2f}")

