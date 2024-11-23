import os
from pathlib import Path

# Funções


def procurar_carro():
    lista_carros = []  # lista de dicionários (cada carro = dict)
    resultado = []  # resultado da pesquisa, a ser exibido

    # separando os valores do arquivo .txt
    p = Path(__file__).with_name('estoque_carros.txt')
    with p.open('r', encoding='utf-8') as file:
        file_lines = file.readlines()

        for line in file_lines:
            nome_carro = line.split(',')[0]
            preco = line.split(',')[1]
            ano = line.split(',')[2]
            estado = line.split(',')[3][:-1]

            # colocando-os num dicionário, dentro de uma lista
            lista_carros.append(
                {'nome_carro': nome_carro, 'preco': preco, 'ano': ano, 'estado': estado})

        # usuário digita valor a ser pesquisado (estado ou preço máximo)
        pesquisa = input(
            f'\nDigite o preço máximo do carro que você deseja, ou o estado de conservação dele ("novo", "seminovo", "conservado" ou "mal estado"): ')

        try:
            pesquisa = float(pesquisa)  # se funcionar, pesquisa é float

            # verificando o preço e adicionando o carro nos resultados, caso ok
            for carro in lista_carros:
                if float(carro['preco']) <= pesquisa:
                    resultado.append(carro)

            # caso resultado esteja vazio
            if resultado == []:
                return None

            # caso não esteja vazio
            else:
                return resultado

        except ValueError:  # se caiu no except, pesquisa é string
            for carro in lista_carros:
                if carro['estado'] == pesquisa:
                    resultado.append(carro)

            # caso resultado esteja vazio
            if resultado == []:
                return None

            # caso não esteja vazio
            else:
                return resultado


# pra receber resultado de procurar_carro() e printar de forma legível, caso não seja vazio
def printar_resultado(resultado):
    if resultado == None:
        print("\nCarro NÃO encontrado!")

    else:
        print("\nCarros encontrados:\n")
        for carro in resultado:
            print(f"Modelo: {carro['nome_carro']}, Preço: {carro['preco']}, Ano: {
                  carro['ano']}, Estado: {carro['estado']};")


def cadastrar_carro():
    carros_a_cadastrar = []  # lista de carros a serem cadastrados no .txt ao final da função

    while True:
        nome_carro = input(
            "\nDigite o nome do carro que deseja cadastrar (se desejar parar, digite 0): ")
        if nome_carro == '0':  # pra quebrar o loop caso o usuário termine de cadastrar
            break

        try:  # pegando exceção caso digite uma string
            preco = float(input("Digite o preço do carro: "))
        except ValueError:
            print("ERRO! O preço deve ser um valor numérico. Tente novamente.")
            quit()

        try:  # pegando exceção caso digite uma string
            ano = int(input("Digite o ano de fabricação do carro: "))
        except ValueError:
            print("ERRO! O ano deve ser um valor numérico. Tente novamente.")
            quit()

        estado = input(
            'Digite o estado de conservação do carro ("novo", "seminovo", "conservado" ou "mau estado"): ')

        # coloco em lista de tuplas pra poder depois separar por linha
        carros_a_cadastrar.append((nome_carro, preco, ano, estado))
        print("\nCarro cadastrado!")

    p = Path(__file__).with_name('estoque_carros.txt')
    with p.open('a', encoding='utf-8') as file:
        for carro in carros_a_cadastrar:
            # retirando parênteses, aspas e espaços em branco antes de salvar
            file.write(str(carro)[1:-1].replace(" ", "").replace("'", ""))
            file.write('\n')

    # mensagem de sucesso
    print("\nCarro(s) registrado(s) com sucesso!")


# Mensagens

msg_bem_vindo = '''
##############################################

Bem-vindo à concessionária Paraíba Cars LTDA!'''

msg_menu = '''
##############################################

Digite a opção que você deseja ('p', 'c' ou 's'):

[p] = Procurar carro
[c] = Cadastrar carro
[s] = Sair do sistema

> '''

msg_procurar = '''
##############################################

Vamos pesquisar um carro para você!\n
'''

msg_cadastrar = '''
##############################################

Vamos cadastrar um carro!\n
'''

# Menus


def main():
    os.system('cls')
    print(msg_bem_vindo)

    while True:
        opcao = input(msg_menu)

        if opcao == 'p':
            resultado = procurar_carro()
            printar_resultado(resultado)

        elif opcao == 'c':
            cadastrar_carro()

        elif opcao == 's':
            print("\nObrigado por usar o nosso sistema!")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n\n")


main()
