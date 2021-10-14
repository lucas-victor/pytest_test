"""
#from tests.test_parametrize import carrega_dados_two, carrega_dados_tree
#carrega_dados_two()
#carrega_dados_tree()

#print(text.index("localizacao de strings", 10, 80))
#print(text.index("strings"))
#print(text.find("teste de substituicao"))

text = "teste string grande para teste de substituicao e localizacao de strings em python e mais testes"

#print(len(text))
lista = ['teste', 'teste2']

print(lista)


connection = cx_Oracle.connect("username/password@host/port")
print (connection.version)
connection.close()
"""

"""
Testada conexão com banco do sis com sucesso.
realizada a consulta.

import cx_Oracle

#jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
con = cx_Oracle.connect('sis/sis@sisdev4-h1/sisdev4')

cursor = con.cursor()
querystring = "SELECT * FROM sisinv.TBELEMENREDE ele WHERE ele.CD_ELEMEN_REDE LIKE 'NCEGPON_NETQ%'"

cursor.execute(querystring)
result = cursor.fetchone()
print(result)
#print(con.version)
con.close()
"""

import cx_Oracle

#jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
con = cx_Oracle.connect('sis/sis@sisdev4-h1/sisdev4')

cursor = con.cursor()
querystring = "SELECT * FROM sisinv.TBELEMENREDE ele WHERE ele.CD_ELEMEN_REDE LIKE '%ZTE%'"

cursor.execute(querystring)
result = cursor.fetchone()
#print(result)
if result == None:
    print("Nenhum resultado para a query realizada.")
    exit()
else:
    while result:
        print(result)
        result = cursor.fetchone()
        #print(f"resultado depois do fetch do while:\n {result}")

cursor.close()
#print(con.version)
con.close()




