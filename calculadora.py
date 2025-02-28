def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    resultado = a / b
    return f"{a} / {b} = {resultado}"

def restoDiv(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    resultado = a % b
    return f"{a} % {b} = {resultado}"

def fatorial(a):
    if a < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i
    return f"O fatorial de {a} é {resultado}"

def primos(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def primosAte(a):
    resultado = 0
    for i in range(2, a + 1):  
        if primos(i):
            resultado += i  
    return f"A soma dos números primos até {a} é {resultado}"

def calculadora():
    print("Calculadora simples")
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Escolha a operação (+, -, *, /, %, !, P): ")

            if operacao == "!":
                print(fatorial(int(num1)))

            elif operacao.lower() == "p":  
                print(primosAte(int(num1)))  

            else:
                num2 = float(input("Digite o segundo número: "))
                if operacao == "+":
                    print(f"{num1} + {num2} = {soma(num1, num2)}")
                elif operacao == "-":
                    print(f"{num1} - {num2} = {subtracao(num1, num2)}")
                elif operacao == "*":
                    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
                elif operacao == "/":
                    print(divisao(num1, num2))
                elif operacao == "%":
                    print(restoDiv(num1, num2))
                else:
                    print("Operação inválida!")

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos.")

if __name__ == "__main__":
    calculadora()
