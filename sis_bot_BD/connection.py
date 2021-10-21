import cx_Oracle


SISDX02='sis/sis@10.61.47.138/sisdev2'
SISDX03='sis/sis@10.61.47.141/sisdev3'
SISDX04='sis/sis@10.61.47.142/sisdev4'
SISDX05='sis/sis@10.61.47.140/sisdev5'
SISDX06='sis/sis@10.61.47.144/sisdev6'
SISDX07='sis/sis@10.61.47.145/sisdev7'
SISDX08='sis/sis@10.61.47.146/sisdev8'
SISDX09='sis/sis@10.61.47.147/sisdev9'

class Connection:

    def __init__(self):
        pass

    def get_connection(self, server_name):
        if server_name.lower() == "sisdx02":
            return cx_Oracle.connect(SISDX02)
        elif server_name.lower() == "sisdx03":
            return cx_Oracle.connect(SISDX03)
        elif server_name.lower() == "sisdx04":
            return cx_Oracle.connect(SISDX04)
        elif server_name.lower() == "sisdx05":
            return cx_Oracle.connect(SISDX05)
        elif server_name.lower() == "sisdx06":
            return cx_Oracle.connect(SISDX06)
        elif server_name.lower() == "sisdx07":
            return cx_Oracle.connect(SISDX07)
        elif server_name.lower() == "sisdx08":
            return cx_Oracle.connect(SISDX08)
        elif server_name.lower() == "sisdx09":
            return cx_Oracle.connect(SISDX09)
        else:
            print(
                f"Nome do servidor inválido: {server_name}. Verifique a string de conexão!")
