def soma(x, y):
    return x + y

def test_soma():
    for i in 2, 3, 4, 5:
        print(f"######## teste do item: {i}")
        assert 5 == soma(i,3)

'''
def test_soma2():
    if 5 == soma(2,3):
        print("######## teste passou com sucesso.")
        assert True
    else:
        print("######## teste falhou miseravelmente")
        assert False
'''



