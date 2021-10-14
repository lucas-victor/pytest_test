from pytest import mark

from tests.test_parametrize import carrega_dados

"""
@mark.parametrize("number", [1,2])
def test_first(number):
    print(number)
    assert number


@mark.parametrize("param, valor", [(1,2), (3,4)])
def test_first(param, valor):
    print(param, valor)
    assert param, valor
"""

@mark.parametrize("param, valor", carrega_dados())
def test_two(param, valor):
    print(param, valor)
    assert param, valor

