# Solicita ao usuário o valor da base do triângulo e converte para float
base = float(input("Digite o valor da base do triângulo: "))

# Solicita ao usuário o valor da altura do triângulo e converte para float
altura = float(input("Digite o valor da altura do triângulo: "))

# Verifica se os valores são positivos (condição necessária para cálculo válido)
if base > 0 and altura > 0:
    # Calcula a área do triângulo usando a fórmula (base * altura) / 2
    area = (base * altura) / 2
    
    # Exibe o resultado da área
    print("A área do triângulo é:", area)
else:
    # Exibe mensagem de erro caso os valores sejam inválidos
    print("Erro: base e altura devem ser valores positivos.")
  
