# Solicita o capital inicial
capital_inicial = float(input("Informe o capital inicial: "))

# Solicita a taxa de juros (%)
taxa_percentual = float(input("Informe a taxa de juros (%): "))

# Solicita o tempo em períodos
tempo_periodos = float(input("Informe o tempo: "))

# Verifica se os valores são válidos
if capital_inicial >= 0 and taxa_percentual >= 0 and tempo_periodos >= 0:
    # Converte a taxa de percentual para decimal
    taxa_decimal = taxa_percentual / 100
    
    # Calcula juros simples
    juros = capital_inicial * taxa_decimal * tempo_periodos
    
    # Calcula montante final
    montante = capital_inicial + juros
    
    # Exibe resultados
    print("Juros calculados:", juros)
    print("Montante final:", montante)
else:
    print("Erro: todos os valores devem ser positivos.")
  
