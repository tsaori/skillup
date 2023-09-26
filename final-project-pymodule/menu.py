from utils import *
from cliente import *

def menu_principal():
    menu_text = f'''    
Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:
1 - Cliente
2 - Ordem
3 - Realizar análise da carteira
4 - Imprimir relatório da carteira
5 - Sair
    '''
    print(menu_text)
    option = int(input('Digite opção desejada: '))
    validate = True
    while validate:
        if option == 1:
            menu_cliente()
        elif option == 2:
           validate = False
           menu_principal()
        elif option == 3:
            validate = False
            menu_principal()
        elif option == 4:
            validate = False
            menu_principal()
        elif option == 5:
            print('Encerrando programa')
            exit()
        else:
            print('Opçao invalida')
            menu_principal()

def menu_cliente():
    # lista_cliente = []   
  
    validate = True
    while validate:
        menu_client_text = f'''
------ Menu Cliente ------
1 - Cadastrar Cliente
2 - Alterar Cliente
3 - Buscar Cliente
4 - Deletar Cliente
5 - Listar Clientes
6 - Voltar ao menu anterior
'''
        print(menu_client_text)
        option_cliente = int(input('Digite opção desejada: '))
        if option_cliente == 1:
            cliente ={
                "Nome": str(input('Digite nome: ')),
                "CPF": validacao_cpf(str(input('Digite CPF: ')), option_cliente),
                "RG": validacao_rg(str(input('Digite RG: '))),
                "Nascimento": validacao_nascimento(),
                "Endereco": buscar_cep(str(input('Digite CEP: '))),
                "Numero": str(input('Digite numero da casa: '))
            }
            # lista_cliente.append(cliente)
            write_client(cliente)
            check_cep(cliente['Endereco'])
            # print(lista_cliente)
            validate = False
        elif option_cliente == 2:
            cpf = validacao_cpf(str(input('Digite CPF do cliente a ser atualizado: ')), option_cliente)
            update_client(cpf)
            print('Cliente atualizado')
            validate = False
        elif option_cliente == 3:
            cpf = validacao_cpf(str(input('Digite CPF do cliente: ')), option_cliente)
            read_client(cpf)
            validate = False
        elif option_cliente == 4:
            cpf = validacao_cpf(str(input('Digite CPF do cliente a ser >> deletado <<: ')), option_cliente)
            delete_client(cpf)
            print('Cliente deletado')
            validate = False
        elif option_cliente == 5:
            print('\nList of clients:')
            all_clients()
            validate = False
        elif option_cliente == 6:
            print('Encerrando menu cliente')
            menu_principal()
            validate = False

            