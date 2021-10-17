#import DbConnection
import cx_Oracle
import sys
import pandas as pd
from IPython.display import display


sa = 'INSTALAR_INFRA_NASS'
regra_enrich_global = 'LineIdIptv'

query_sa_x_enrich_rule = f"""select 
    sa.cd_serv_aprov, re.cd_regra_enriq, rs.ordem_execucao
    from sisapr.tbservicapro sa
    join sisapr.rserviapreen rs on rs.id_serv_aprov = sa.id_serv_aprov 
    join sisapr.tbregraenriq re on re.id_regra_enriq = rs.id_regra_enriq
    where sa.cd_serv_aprov like '{sa}'"""


#print(sys.path)


"""
def test_db_conn():
    df = pd.read_sql_query(query_sa_x_enrich_rule, db_connection.get_connection())
    display(df)

    #print(df)
    for campo in df.values:
        print(f"imprimindo campo: {campo}")

    imprimindo campo: ['INSTALAR_INFRA_NASS' 'LineIdIptv' None]
    imprimindo campo: ['INSTALAR_INFRA_NASS' 'AcessoAssetIdValidation' None]
    imprimindo campo: ['INSTALAR_INFRA_NASS' 'LineIdHsiValidation' None]
    imprimindo campo: ['INSTALAR_INFRA_NASS' 'VelocidadeBasica' None]


    achou_regra_enrich = df.loc[df["CD_REGRA_ENRIQ"] == regra_enrich_global]
    print(f"a regra foi localizada?  \n{achou_regra_enrich}")

    if regra_enrich_global in achou_regra_enrich.values:
        print(f"Regra encontrada: {regra_enrich_global}")
        #print(regra_enrich)
        display(achou_regra_enrich)
    else:
        print("é none")
        print(regra_enrich_global)
        print(f"printando NÂO achou \n{achou_regra_enrich}")

#test_db_conn()

"""