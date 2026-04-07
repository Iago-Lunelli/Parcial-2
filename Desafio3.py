# Função responsável por ler 5 nomes digitados pelo usuário
def ler_nomes():
    nomes = []  # Lista vazia que irá armazenar os nomes

    # Loop para pedir 5 nomes ao usuário
    for i in range(5):
        nome = input(f"Digite o {i+1}º nome: ")  # Entrada de dados
        nomes.append(nome)  # Adiciona o nome à lista

    return nomes  # Retorna a lista preenchida


# Função responsável por imprimir os nomes da lista
def imprimir_nomes(lista_de_nomes):
    print("\nLista de nomes digitados:")

    # Percorre a lista e imprime cada nome
    for i, nome in enumerate(lista_de_nomes, start=1):
        print(f"{i}. {nome}")  # Saída formatada com numeração


# Função principal que organiza o fluxo do programa
def main():
    # Chama a função para ler os nomes
    lista = ler_nomes()

    # Verificação simples (condicional) para garantir que há nomes na lista
    if lista:
        imprimir_nomes(lista)  # Imprime os nomes
    else:
        print("Nenhum nome foi informado.")


# Garante que o código só será executado diretamente
# e não quando importado como módulo
if __name__ == "__main__":
    main()
