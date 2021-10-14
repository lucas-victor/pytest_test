'''
def div(x, y):
    return x / y

def test_div():
    assert 1 == div(3, 3)

def test_div2():
    assert 2 == div(9, 3)
'''

"""
Todos os ips.

#querystring = "SELECT * FROM sisinv.TBELEMENREDE ele WHERE ele.CD_ELEMEN_REDE LIKE '%ZTE%'"
"""
import pytest
import cx_Oracle
import pandas as pd


def get_connection():
    #jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
    con = cx_Oracle.connect('sis/sis@sisdev6-h1/sisdev6')
    return con
    
    


def test_servaprov_por_regra_enriqucimento():
    """
        Testa se o serviço de aprovisionamento está relacionado a regra.

    """
    sa = 'INSTALAR_INFRA_NASS'
    regra_enrich = 'LineIdIptv'

    querystring = f"""select sa.cd_serv_aprov, re.cd_regra_enriq, rs.ordem_execucao
    from sisapr.tbservicapro sa
    join sisapr.rserviapreen rs on rs.id_serv_aprov = sa.id_serv_aprov 
    join sisapr.tbregraenriq re on re.id_regra_enriq = rs.id_regra_enriq
    where sa.cd_serv_aprov like '{sa}'"""

    
    con = get_connection()
    cursor = con.cursor()
    cursor.execute(querystring)
    
    #result_one_line = cursor.fetchone()

    #df = pd.read_sql_query(querystring, con)
    #print(result_one_line)
    #print(df)

    #for campo in df.values:
    #    print(campo)


    if result_one_line == None:
        print("Nenhum resultado para a query realizada.")
        exit()
    else:
        while result_one_line:
            count += 1
            print(result_one_line)
        
            for campo in result_one_line:
                if str(campo).find(regra_enrich) != -1:
                    regra_localizada = campo

                    print(f"""A regra de enriquecimento: {regra_localizada}\nEstá associada ao servico: {sa}""") 
                    assert regra_localizada == regra_enrich
                    #{result_one_line.index(campo)} na linha {count}
                   #if "ZTE_NetQ" in str(campo):
            result_one_line = cursor.fetchone()
        #print(f"resultado depois do fetch do while:\n {result}")
    cursor.close()
    con.close()
    #print("Erro ao realizar o select no banco")
    

test_servaprov_por_regra_enriqucimento()

"""
if result_one_line == None:
    print("Nenhum resultado para a query realizada.")
    exit()
else:
    while result_one_line:
        count += 1
        print(result_one_line)
        for campo in result_one_line:
           if str(campo).find("ZTE_NetQ") != -1:
              print(f"encontrei o texto ZTE_NetQ na posicao {result_one_line.index(campo)} na linha {count}")
#           if "ZTE_NetQ" in str(campo):
#

        result_one_line = cursor.fetchone()
        #print(f"resultado depois do fetch do while:\n {result}")

cursor.close()
#print(con.version)
con.close()

"""