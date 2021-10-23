import cx_Oracle

from sis_bot_BD.constantes import *


class Connection:

    def __init__(self, server_name) -> cx_Oracle:
        self.server_name: str = server_name
        self.con: cx_Oracle = None

    @property
    def get_server_name(self):
        return self.server_name

    @property
    def get_connection(self) -> cx_Oracle:
        try:

            if self.server_name.lower() == "sisdx02":
                self.con = cx_Oracle.connect(SISDX02)
                return self.con
            elif self.server_name.lower() == "sisdx03":
                self.con = cx_Oracle.connect(SISDX03)
                return self.con
            elif self.server_name.lower() == "sisdx04":
                self.con = cx_Oracle.connect(SISDX04)
                return self.con
            elif self.server_name.lower() == "sisdx05":
                self.con = cx_Oracle.connect(SISDX05)
                return self.con
            elif self.server_name.lower() == "sisdx06":
                self.con = cx_Oracle.connect(SISDX06)
                return self.con
            elif self.server_name.lower() == "sisdx07":
                self.con = cx_Oracle.connect(SISDX07)
                return self.con
            elif self.server_name.lower() == "sisdx08":
                self.con = cx_Oracle.connect(SISDX08)
                return self.con
            elif self.server_name.lower() == "sisdx09":
                self.con = cx_Oracle.connect(SISDX09)
                return self.con
            elif self.server_name.lower() == "sisdx11":
                self.con = cx_Oracle.connect(SISDX11)
                return self.con
            elif self.server_name.lower() == "sisdx12":
                self.con = cx_Oracle.connect(SISDX12)
                return self.con
            else:
                print(
                    f"\nNome do servidor inválido: '{self.server_name}'. Digite um nome válido. Ex: sisdx06\n")

        except Exception as e:
            print(f'StackTrace: {e}')
            print(f"\nErro ao tentar estabelecer conexão com o banco de dados {self.server_name}. Favor verificar!")




conn = Connection("sisdx03")
print(conn.get_connection)


#conn = cx_Oracle.connect(SISDX06)
#print(f'printando conexao: {conn}')


