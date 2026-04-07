# Realiza operações básicas (+, -, *, /)
# Solicita ao usuário o primeiro número e converte para float
num1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número e converte para float
num2 = float(input("Digite o segundo número: "))

# Mostra ao usuário as operações disponíveis
print("\nOperações disponíveis:")
print("+  -=> Soma")
print("-  -=> Subtração")
print("*  -=> Multiplicação")
print("/  -=> Divisão")

# Solicita ao usuário qual operação deseja realizar
operacao = input("Digite a operação desejada: ")

# Verifica se a operação é soma
if operacao == "+":
    # Calcula a soma dos números
    resultado = num1 + num2
    
    # Mostra o resultado da soma
    print("Resultado:", resultado)

# Verifica se a operação é subtração
elif operacao == "-":
    # Calcula a subtração
    resultado = num1 - num2
    
    # Mostra o resultado da subtração
    print("Resultado:", resultado)

# Verifica se a operação é multiplicação
elif operacao == "*":
    # Calcula a multiplicação
    resultado = num1 * num2
    
    # Mostra o resultado da multiplicação
    print("Resultado:", resultado)

# Verifica se a operação é divisão
elif operacao == "/":
    # Verifica se o segundo número é diferente de zero
    if num2 != 0:
        # Calcula a divisão
        resultado = num1 / num2
        
        # Mostra o resultado da divisão
        print("Resultado:", resultado)
    else:
        # Mostra erro caso haja tentativa de divisão por zero
        print("Erro: divisão por zero não é permitida.")

# Caso o usuário digite uma operação inválida
else:
    # Exibe mensagem de erro
    print("Operação inválida.")
#Código também já feito no meu VsCode.
