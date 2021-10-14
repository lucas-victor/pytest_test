import pytest
import os
from pytest import fixture
from pytest import mark

'''
value="""
param1=valor1
param2=valor2
param3=valor3
param4=valor4
param5=valor5
"""
#dict([i.split('=') for i in value.strip().split('\n')])
'''

def carrega_dados():
    #dic = {'param': 'valor'}
    #dict([i.split('=') for i in value.strip().split('\n')])
    lista = []
    #dic2 = {'param_nome_test': 'valor_nome_test'}
    tup = ()
    with open('teste_dados.txt') as arq:
        for line in arq:
            param_valor = line.split('=')
            parm = param_valor[0]
            valor = param_valor[1]
            tup = (parm, valor)
            #dic = (param, valor)
            #dicc = dict(parametro=parm, valor_parametro=valor)
            #print(f'parametro e: {dicc.keys()} e o valor e: {dicc.values()}', end='')
            lista.append(tup)

    print(lista)
    #return lista
    #return dic2
    return lista


def carrega_dados_two():
    #dic = {'param': 'valor'}
    #dict([i.split('=') for i in value.strip().split('\n')])
    lista = []
    lista_param_um_campo = []
    lista_valor_tup_um_campo = []
    dic2 = {'param_nome_test': 'valor_nome_test'}
    tup = ()
    print('iniciando funcao carrega_dados_two.............')
    with open('teste_dados_mult_param.txt') as arq:
        for line in arq:
            if ';' in line:
                lista_param_um_campo = line.split(";")
                print(f'\n1 - lista_param_um_campo {lista_param_um_campo}')

                #percorre lista de parametros de um campo
                for param_e_value in lista_param_um_campo:

                    #pegar cada parametro e valor como uma tupla
                    param_e_valor_tup = tuple(param_e_value.split('='))
                    print(f'2 - param_e_valor_tup {param_e_valor_tup}')

                    #adiciona cada tupla na lista de parametros
                    lista_valor_tup_um_campo.append(param_e_valor_tup)
                    print(f'3 - lista_param_um_campo {lista_valor_tup_um_campo}')

                #add lista de tuplas de parametros de uma linha do arquivo na lista principal
                lista.append(lista_valor_tup_um_campo)
                print(f'4 - lista {lista}')
            else:
                print('5 - entrou no else')
                param_valor = line.split('=')
                parm = param_valor[0]
                valor = param_valor[1]
                tup = (parm, valor)
                print(f'6 - adicionando parametro e valor na tupla tup {tup}')
                #dic = (param, valor)
                #dicc = dict(parametro=parm, valor_parametro=valor)
                #print(f'parametro e: {dicc.keys()} e o valor e: {dicc.values()}', end='')
                print(f'7 - adicionando tupla na lista {tup}')
                lista.append(tup)

    print(f'8 - lista {lista}')
    #return lista
    #return dic2
    return lista


def carrega_dados_tree():
    lista_param = []
    texto_1 = 'te'
    param = 'te'
    tup = param, texto_1
    lista_param.append(param)
    lista_param.append(texto_1)
    print(param, texto_1)
    print(lista_param)
    #return lista_param
    #return param, texto_1
    return tup

#carrega_dados_two()
#carrega_dados()

"""
'''
#@fixture(params='parm')
@fixture(params=carrega_dados())
def my_test_data(request):
    test_data = request.param
    print(f'valor da variavel test_data e: {test_data}')
    return test_data
'''

#@pytest.mark.parametrize("inicial,final", [(0,0), (1,0), (2,1)])
#@pytest.mark.parametrize("SN, 123", carrega_dados())
'''
@pytest.mark.parametrize("parm, valor", my_test_data)
def test_parametrize(param, valor):
    print("entrou parametrize")
    print(param, valor)
'''

@pytest.mark.parametrize("inicial,final", [(0,0), (1,0), (2,1)])
def test_parametrize(inicial, final):
    print("entrou parametrize")
    print(inicial, final)

'''
    for linha in my_test_data:
        parametro = my_test_data['param_nome_test']
        valor = my_test_data['valor_nome_test']
        print(f'meu parametro e: {parametro} e o valor e: {valor} ')
'''

#my_test_data()
test_parametrize()
#dic = {'key_param': 'nome_param', 'key_valor': 'nome_valor'}
#carrega_dados()
"""
