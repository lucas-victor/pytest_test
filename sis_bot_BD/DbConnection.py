import cx_Oracle
import pandas as pd
import sys, os
#import traceback
import logging
from IPython.display import display
from pandas.core.frame import DataFrame


PLANO_DE_TESTE = "../PLANO_TESTE/plano_de_teste_automatizado.ods"

sa = 'INSTALAR_INFRA_NASS'
regra_enrich_global = 'LineIdIptv'
server = "sisdx06"

sa_x_enrich_rule_query = f"""select 
    sa.cd_serv_aprov, re.cd_regra_enriq, rs.ordem_execucao
    from sisapr.tbservicapro sa
    join sisapr.rserviapreen rs on rs.id_serv_aprov = sa.id_serv_aprov 
    join sisapr.tbregraenriq re on re.id_regra_enriq = rs.id_regra_enriq
    where sa.cd_serv_aprov like '{sa}'"""


def get_connection(server_name):
    if server_name.lower() == "sisdx02":
        return cx_Oracle.connect('sis/sis@sisdev2-h1/sisdev2')
    elif server_name.lower() == "sisdx03":
        return cx_Oracle.connect('sis/sis@sisdev3-h1/sisdev3')
    elif server_name.lower() == "sisdx04":
        return cx_Oracle.connect('sis/sis@sisdev4-h1/sisdev4')
    elif server_name.lower() == "sisdx05":
        return cx_Oracle.connect('sis/sis@sisdev5-h1/sisdev5')
    elif server_name.lower() == "sisdx06":
        return cx_Oracle.connect('sis/sis@sisdev6-h1/sisdev6')
    elif server_name.lower() == "sisdx07":
        return cx_Oracle.connect('sis/sis@sisdev7-h1/sisdev7')
    elif server_name.lower() == "sisdx08":
        return cx_Oracle.connect('sis/sis@sisdev8-h1/sisdev8')
    elif server_name.lower() == "sisdx09":
        return cx_Oracle.connect('sis/sis@sisdev6-h1/sisdev6')
    else:
        print(
            f"Nome do servidor inválido: {server_name}. Verifique a string de conexão!")


""" teste db get_connection ok
con = get_connection("sisdx06")
print(con)
"""


def get_plano_teste():
    # with open("PLANO_TESTE/plano_de_teste_automatizado.ods", "r") as plano:
    print(os.getcwd())
    df = pd.read_excel(PLANO_DE_TESTE)
    # print(df)
    replaced_df = df.fillna("-").replace(0.0, 0)
    #replaced_df = replaced_df.replace(0.0, 0)
    # print(replaced_df)
    #achou_regra_recuperada = df.loc[df["CD_REGRA_ENRIQ"] == "LineIdIptv"]
    #regra_do_bd = achou_regra_recuperada["CD_REGRA_ENRIQ"].get(0)
    #serv_aprov = replaced_df["CD_SERV_APROV"].get(0)
    #regra_enrich = replaced_df["CD_REGRA_ENRIQ"].get(0)

    #print(serv_aprov, regra_enrich)
    return replaced_df


"""Teste get plano
"""
# get_plano_teste()


def get_caso_de_teste(num_linha_ct, plano_de_teste_df: DataFrame):
    # plano_de_teste_df
    # for i in range(0, len(plano_de_teste_df)):
    linha_ct = plano_de_teste_df.loc[num_linha_ct]
    print(f"printando linha: {num_linha_ct} = {linha_ct.values}")
    sa_reg_tup = (linha_ct.values[0], linha_ct.values[1], linha_ct.values[2])
    print(f"Print tuple: {sa_reg_tup}")
    #serv_aprov = linha_ct["CD_SERV_APROV"].get(0)
    #regra_enrich = linha_ct["CD_REGRA_ENRIQ"].get(0)
    #print(f"Linha: {i} == SA: {serv_aprov} --> RE: {regra_enrich}")
    # jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
    # self.
    # return con
    return sa_reg_tup

# get_caso_de_teste(get_plano_teste())


def test_sa_x_regra_enrich():
    plano_de_teste_df = get_plano_teste()
    query_sa_x_enrich_df = ""

    for linha in range(0, len(plano_de_teste_df)):
        #print(f"Linha: {linha} ---> {plano_de_teste_df.values[linha]}")
        sa_ct, re_ct, ord_exec = get_caso_de_teste(linha, plano_de_teste_df)
        #print(sa_ct, re_ct, ord_exec)

        df_result_query = select_sa_x_enrich_rule_2(sa_ct)
        print(f"Printando display {linha}")
        display(df_result_query)
        assert_regra(re_ct, df_result_query)


def assert_regra(re_ct, df: DataFrame):

    if re_ct != "-":
        achou_regra_enrich = df.loc[df["CD_REGRA_ENRIQ"] == re_ct]
        print(f"a regra foi localizada?  \n{achou_regra_enrich}")
        
        regra_do_bd = achou_regra_enrich["CD_REGRA_ENRIQ"].values
        print(f"\nBuscando regra: {re_ct}")
        print("realizando o assert da regra")
        print(f"Resultado esperado: {re_ct}\nResultado Atual: {regra_do_bd}")
        assert re_ct == regra_do_bd


def select_sa_x_enrich_rule(sa):
    """
        Realiza o select no banco configurado e faz a validação dos dados recebidos.
    """
    query_preparada = sa_x_enrich_rule_query.format(sa)
    with get_connection(server) as db_con:
        try:
            df = pd.read_sql_query(query_preparada, db_con)
            print("Regras encontradas para o serviço: ")
            display(df)

            achou_regra_enrich = df.loc[df["CD_REGRA_ENRIQ"]
                                        == regra_enrich_global]
            #print(f"a regra foi localizada?  \n{achou_regra_enrich}")

            regra_do_bd = achou_regra_enrich["CD_REGRA_ENRIQ"].get(0)
            print(f"\nBuscando regra: {regra_enrich_global}")
            # print(regra_do_bd)
            assert regra_enrich_global == regra_do_bd

            print(f"\nRegra encontrada com sucesso!")
            display(achou_regra_enrich)

        except AssertionError:
            logging.error(
                f"Resultado esperado: {regra_enrich_global} - Resultado atual: {regra_do_bd}", exc_info=True)


def select_sa_x_enrich_rule_2(sa):
    """
        Realiza o select no banco configurado e faz a validação dos dados recebidos.
    """
    query_preparada = sa_x_enrich_rule_query.format(sa)
    try:
        with get_connection(server) as db_con:
            print("realizando select no banco. SA x RE")
            df = pd.read_sql_query(query_preparada, db_con)
            return df
    except Exception as e:
        print(
            f"Não foi possível estabelecer conexão com o banco {server} \n {e}")


test_sa_x_regra_enrich()
# print(sa_x_enrich_rule_query.format(sa))
# select_sa_x_enrich_rule_2()


# select_sa_x_enrich_rule()
# select_sa_x_enrich_rule()


def test_db_connect():
    df = pd.read_sql_query(sa_x_enrich_rule_query, get_connection(server))
    print("Todos os dados retornados pelo select: ")
    display(df)
    """
        #print(df)
        for campo in df.values:
            print(f"imprimindo campo: {campo}")

        imprimindo campo: ['INSTALAR_INFRA_NASS' 'LineIdIptv' None]
        imprimindo campo: ['INSTALAR_INFRA_NASS' 'AcessoAssetIdValidation' None]
        imprimindo campo: ['INSTALAR_INFRA_NASS' 'LineIdHsiValidation' None]
        imprimindo campo: ['INSTALAR_INFRA_NASS' 'VelocidadeBasica' None]
        """

    achou_regra_enrich = df.loc[df["CD_REGRA_ENRIQ"] == regra_enrich_global]
    #print(f"a regra foi localizada?  \n{achou_regra_enrich}")

    if regra_enrich_global in achou_regra_enrich.values:
        #print(f"Regra encontrada: {achou_regra_enrich}")
        # print(regra_enrich)
        display(achou_regra_enrich)
        regra_recuperada = achou_regra_enrich["CD_REGRA_ENRIQ"].get(0)
        #print(f"Resultado esperado: {regra_enrich_global} resultado obtido do banco: {regra_recuperada}")
        assert regra_enrich_global == regra_recuperada
    # else:
        #print("é none")
        # print(regra_enrich_global)
        #print(f"printando NÂO achou \n{achou_regra_enrich}")

     # return df


# test_db_connect()
# print()
# print()
# print(sys.path)
#db = DBConnection()

# db.test_db_connect()
# test_db_connect()
# print(result_one_line)
# print(df)

# for campo in df.values:
#    print(campo)


"""
def select_sa_x_enrich_rule():
    with get_connection(server) as db_con:
        try:
           cursor = db_con.cursor()
           cursor.execute(query_sa_x_enrich_rule)
           result_one_line = cursor.fetchone()
           count = 0
        except:
           print("Ocorreu uma exceção!")
        con = db_connection.get_connection()
        print(con)
        cursor = con.cursor()

        cursor.execute(query_sa_x_enrich_rule)
        result = cursor.fetchall()

        print(result)



        for valor in achou_regra_enrich:
            print(valor, "\n")

        
        if regra_enrich_global in achou_regra_enrich.values:
            #print(f"Regra encontrada: {achou_regra_enrich}")
            #print(regra_enrich)
            display(achou_regra_enrich)
            regra_recuperada = achou_regra_enrich["CD_REGRA_ENRIQ"].get(0)
            #print(f"Resultado esperado: {regra_enrich_global} resultado obtido do banco: {regra_recuperada}")
            assert regra_enrich_global == regra_recuperada


        except Exception as e:
            print(f"Ocorreu uma exceção! \n {e}")



        try
        except AssertionError:
            _, _, tb = sys.exc_info()
            traceback.print_tb(tb) # Fixed format
            tb_info = traceback.extract_tb(tb)
            filename, line, func, text = tb_info[-1]

            print('An error occurred on line {} in statement {}'.format(line, text))
            exit(1)



if __name__ == "__main__":
    import sys
    DBConnection(sys.argv[1])
"""
