from validate_docbr import CPF
import re
from datetime import datetime
import requests
from cliente import create_connection
from variables import *

def check_cpf(cpf):
    cursor, connection = create_connection()
    
    query = f'''
        SELECT [cpf] FROM {table} WHERE [cpf] = '{cpf}'    
    '''

    cursor.execute(query)
    check_cpf = cursor.fetchall()
    connection.commit()

    if check_cpf == []:
        return True
    else:
        return False
    
def validacao_cpf(numero_cpf):
    cpf = CPF()
    validate = True
    while validate:
        numero_cpf = re.sub('[-.]', '',numero_cpf)
        cpf_validado = cpf.validate(numero_cpf)
        
        if cpf_validado:
            cpf_formatado = f"{numero_cpf[:3]}.{numero_cpf[3:6]}.{numero_cpf[6:9]}-{numero_cpf[9:]}"
            cpf_checked = check_cpf(cpf_formatado)
            if cpf_checked == True: 
                validate = False
                return cpf_formatado
            else:
                numero_cpf = input("CPF já cadastrado. Digite novamente: ")
        else:
            numero_cpf = input("CPF inválido. Digite novamente: ")




def validao_rg(rg_input):
    # RG: 11.111.111.-x
    # RG nao valido: 11.111.11x-x
    padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'
    validate = True
    while validate:
        rg_input = re.sub('[-.]','', rg_input)
        rg_input = f'{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}'

        if re.match(padrao_rg, rg_input):
            validate = False
            return rg_input
        else:
            rg_input = input("RG inválido. Digite novamente: ")

def validacao_nascimento():
    # enquanto -> condicao -> verdadeira
    while True:

        data_nascimento_input = input("Digite a data de nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento_input, '%d/%m/%Y').date()
            data_atual = datetime.now().date()
        
            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
                #26/08/1972
            
            else:
                print("Data inválida. A sua data de nascimento deve ser menor que a data atual ")
        
        except ValueError as e:
            print("Formato de data inválido. Você recebeu o erro: ", e, " Tente novamente.")

def buscar_cep(cep_input):
    url = f'https://viacep.com.br/ws/{cep_input}/json/'
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()

        endereco = {
            "CEP": data['cep'],
            "Logradouro": data['logradouro'],
            "Bairro": data['bairro'],
            "Cidade": data['localidade'],
            "Estado": data['uf']
        }

    return endereco
