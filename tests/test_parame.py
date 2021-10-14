from pytest import mark

from tests.test_parametrize import carrega_dados, carrega_dados_two, carrega_dados_tree

"""
@mark.parametrize("number", [1,2])
def test_first(number):
    print(number)
    assert number


@mark.parametrize("param, valor", [(1,2), (3,4)])
def test_first(param, valor):
    print(param, valor)
    assert param, valor
    
#####################
#correto que funciona
    @mark.parametrize("param, valor", carrega_dados())
def test_first(param, valor):
    print(param, valor)
    assert param, valor
"""



#carrega_dados_two()
"""
@mark.parametrize("param, valor, lista_1, lista_2", carrega_dados_two())
def test_two(param, valor, lista_1, lista_2):
    print(param, valor, lista_1, lista_2)
    #assert param, valor
 """

"""
#####################
#correto que funciona
@mark.parametrize("param, valor", carrega_dados_two())
def test_two(param, valor):
    print(param, valor)
    #assert param, valor

"""

"""
@mark.parametrize("param, valor", carrega_dados_two())
def test_two(param, valor):
    print(type(param))
    print(type(valor))
    print(param, valor)
    #assert param, valor
"""
"""
@mark.parametrize("param, valor", carrega_dados_tree())
def test_tree(param, valor):
    print(param, valor)
    #assert param, valor
"""
#FUNCIONOUUUUUUUUUUUUUUUUUUUUUUUU
#recuperar string e cortar para cada parametro iterando e realizando assert de cada.
@mark.parametrize("param, valor", carrega_dados_two())
def test_two(param, valor):
    print(param, valor)
    #assert param, valor