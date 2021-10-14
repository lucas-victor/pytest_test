

#print("helo world")


#name = "lucas victor"

#print(name)


class User:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

class Pessoa(User):
    def __init__(self, cpf):
        self.__nome_pessoa = User.get_nome()
        self.__cpf =  cpf

    def get_dados(self):
        return self.__nome_pessoa + " | " + self.__cpf

user_lucas = User("lucas victor")

print(user_lucas.get_nome())

pessoa_lucas = Pessoa("07800902312")

print(pessoa_lucas.get_dados())

