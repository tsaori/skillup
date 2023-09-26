import pyodbc
import utils
from variables import *
# Variables not commited to github > company only

def create_connection():
    connection = pyodbc.connect(cnxn_str)
    cursor =  connection.cursor()
    return cursor, connection


def check_cep(cep):
    cursor, connection = create_connection()
    
    query = f'''
        SELECT [cep] FROM {table_cep} WHERE [cep] = '{cep["CEP"]}'    
    '''

    cursor.execute(query)
    check_cep = cursor.fetchall()
    connection.commit()

    if check_cep == []:
        write_cep(cep)
    else:
        pass
    

def write_cep(cep):
    cursor, connection = create_connection()
    query = f''' 
        INSERT INTO {table_cep}(cep, logradouro, bairro, cidade, estado)
        VALUES('{cep['CEP']}','{cep['Logradouro']}','{cep['Bairro']}','{cep['Cidade']}','{cep['Estado']}')
    '''
    cursor.execute(query)
    connection.commit()

    

def write_client(client):
    cursor, connection = create_connection()
    query = f''' 
        INSERT INTO {table}(nome, cpf, rg, data_nascimento, cep, numero_residencia)
        VALUES('{client['Nome']}','{client['CPF']}','{client['RG']}','{client['Nascimento']}','{client['Endereco']['CEP']}','{client['Numero']}')
'''

    cursor.execute(query)
    connection.commit()

def read_client(cpf):
    cursor, connection = create_connection()
    query = f'''
        SELECT 
            [nome]
            ,[cpf]
            ,[rg]
            ,[data_nascimento]
            ,[cep]
            ,[numero_residencia]

        FROM {table}
        WHERE [cpf] = '{cpf}'
'''
    cursor.execute(query)
    cliente = cursor.fetchall()
    connection.commit()

    cliente_parse = f'''
        Nome: {cliente[0][0]}
        CPF: {cliente[0][1]}
    	RG: {cliente[0][2]}
        Data de nascimento: {cliente[0][3]}
        CEP: {cliente[0][4]}
        Numero casa: {cliente[0][5]}
'''
    print('\nCLIENTE: ')
    print(cliente_parse)
    return cliente[0]

def update_client(cpf):
    cursor, connection = create_connection()
    validate = True

    while validate:
        cliente ={
                    "Nome": str(input('Digite nome: ')),
                    "RG": (str(input('Digite RG: '))),
                    "Nascimento": utils.validacao_nascimento(),
                    "Endereco": utils.buscar_cep(str(input('Digite CEP: '))),
                    "Numero": str(input('Digite numero da casa: '))
                }
        previous_client = read_client(cpf)
        changes = f'''
            Nome: {previous_client[0]} -----> {cliente['Nome']}
            RG: {previous_client[2]} -----> {cliente['RG']}
            Data de nascimento: {previous_client[3]} -----> {cliente['Nascimento']}
            CEP: {previous_client[4]} -----> {cliente['Endereco']['CEP']}
            Numero casa: {previous_client[5]} -----> {cliente['Numero']}
    '''
        print(changes)
        confirm = str(input('\n Para confirmar mudanças digite s, para editar novamente digite n: '))

        if confirm == 's' or confirm == 'S':
            query = f'''
                UPDATE {table}
                SET [nome]='{cliente['Nome']}', [rg]='{cliente['RG']}' ,[data_nascimento]='{cliente['Nascimento']}',[cep]='{cliente['Endereco']['CEP']}',[numero_residencia]='{cliente['Numero']}'
                WHERE [cpf]='{cpf}'
            '''
            cursor.execute(query)
            connection.commit()
            validate = False

def delete_client(cpf):
    cursor, connection = create_connection()
    query = f'''
        DELETE FROM {table} WHERE [cpf] = '{cpf}'
'''
    cursor.execute(query)
    connection.commit()

def all_clients():
    cursor, connection = create_connection()
    query = f'''
        SELECT * FROM {table}
    '''
    cursor.execute(query)
    clients = cursor.fetchall()
    connection.commit()
    for client in clients:
        cliente_parse = f'''
            ID : {client[0]}
            Nome: {client[1]}
            CPF: {client[2]}
            RG: {client[3]}
            Data de nascimento: {client[4]}
            CEP: {client[5]}
            Numero casa: {client[6]}
            '''
        print(cliente_parse)


