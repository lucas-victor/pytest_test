import cx_Oracle
import pandas as pd
from IPython.display import display

sa = 'INSTALAR_INFRA_NASS'
regra_enrich = 'LineIdIptv'

query_sa_x_enrich_rule = f"""select 
    sa.cd_serv_aprov, re.cd_regra_enriq, rs.ordem_execucao
    from sisapr.tbservicapro sa
    join sisapr.rserviapreen rs on rs.id_serv_aprov = sa.id_serv_aprov 
    join sisapr.tbregraenriq re on re.id_regra_enriq = rs.id_regra_enriq
    where sa.cd_serv_aprov like '{sa}'"""


class DBConnection:

    def __init__(self):
        self.__con = cx_Oracle.connect('sis/sis@sisdev6-h1/sisdev6')
        self.ambiente = "sisdx06"

    
    def get_connection(self):
        return self.__con
        """
        #self.ambiente = "sisdx06"
        if self.ambiente == "sisdx06":
            print("retornando conection")
            
        else:
            print("nao retornou conection")
            return None
        """
        #jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
        #self.
        #return con

    def select_sa_x_enrich_rule(get_connection):
        """
            teste
        """
        with get_connection() as db_con:
            try:
                cursor = db_con.cursor()
                cursor.execute(query_sa_x_enrich_rule)
                result_one_line = cursor.fetchone()
                count = 0
            except:
                print("Ocorreu uma exceção!")


db_connection = DBConnection()
df = pd.read_sql_query(query_sa_x_enrich_rule, db_connection.get_connection())

#print(df)
for campo in df.values:
    print(f"imprimindo campo: {campo}")

achou_regra_enrich = df.loc[df["CD_REGRA_ENRIQ"] == regra_enrich]
print(f"a regra foi localizada?  \n{achou_regra_enrich}")

if regra_enrich in achou_regra_enrich.values:
    print("não é none")
    print(regra_enrich)
    print(f"printando valores do achou \n{achou_regra_enrich}")
else:
    print("é none")
    print(regra_enrich)
    print(f"printando NÂO achou \n{achou_regra_enrich}")

display(achou_regra_enrich)
#print(result_one_line)
#print(df)

#for campo in df.values:
#    print(campo)
        
"""
    con = db_connection.get_connection()
    print(con)
    cursor = con.cursor()

    cursor.execute(query_sa_x_enrich_rule)
    result = cursor.fetchall()

    print(result)
"""