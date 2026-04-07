# Solicita ao usuário um valor em segundos e converte para inteiro
segundos = int(input("Digite o tempo em segundos: "))

# Verifica se o valor digitado é positivo
if segundos >= 0:
    # Calcula quantas horas existem no total de segundos
    horas = segundos // 3600  # 1 hora = 3600 segundos
    
    # Calcula o restante de segundos após retirar as horas
    resto = segundos % 3600
    
    # Calcula quantos minutos existem no restante
    minutos = resto // 60  # 1 minuto = 60 segundos
    
    # Calcula os segundos restantes finais
    segundos_restantes = resto % 60
    
    # Exibe o resultado da conversão
    print("Tempo convertido: ")
    print(horas, "hora(s),", minutos, "minuto(s) e", segundos_restantes, "segundo(s)")
    
else:
    # Exibe mensagem de erro caso o valor seja negativo
    print("Erro, o tempo não pode ser negativo.")
