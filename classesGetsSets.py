

class Conta:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, nome, agencia):
        self.__nome = nome
        self.__agencia = agencia

    #get
    @property
    def nome(self):
        return self.__nome
        print("executando get nome")

    #set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        print("executando set nome")

    # get
    @property
    def agencia(self):
        return self.__agencia
        print("executando get agencia")

    # set
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia
        print("executando set agencia")

    def __str__(self):
        return f'string retornada: {self.__nome} - {self.__agencia}'

conta = Conta("lucas", 123)

conta2 = Conta("teste", 456)

print(conta)
print(conta2)

conta2.nome = "trocaNome"
conta2.agencia = 789

print(conta.nome, conta2.agencia)
print(conta2)