from numpy import empty
from numpy.core.fromnumeric import shape
from pytest import mark
import cx_Oracle
import pandas as pd
import os
#import traceback
import logging
from IPython.display import display
from pandas.core.frame import DataFrame
import pytest


PLANO_DE_TESTE = "../PLANO_TESTE/plano_de_teste_automatizado.ods"
#PLANO_DE_TESTE = "PLANO_TESTE/plano_de_teste_automatizado.ods"

#sa = 'INSTALAR_INFRA_NASS'
regra_enrich_global = 'LineIdIptv'
server = "sisdx06"

SA_X_ENRICH_QUERY = """select 
    sa.cd_serv_aprov, re.cd_regra_enriq, rs.ordem_execucao
    from sisapr.tbservicapro sa
    join sisapr.rserviapreen rs on rs.id_serv_aprov = sa.id_serv_aprov 
    join sisapr.tbregraenriq re on re.id_regra_enriq = rs.id_regra_enriq
    where sa.cd_serv_aprov like '{sa}' and re.cd_regra_enriq like '{re}'"""

SA_X_ROUTER_QUERY="""SELECT 
	sa.CD_SERV_APROV,
	rotea.CD_REGRA_ROTEAM,
	sr.CD_SERVIC_REDE,
	ele.CD_ELEMEN_REDE,
	rot.ORDEM_EXECUCAO 
FROM sisapr.TBSERVICAPRO sa
LEFT JOIN sisapr.TBROTA rot ON rot.ID_SERV_APROV = sa.ID_SERV_APROV 
LEFT JOIN sisapr.TBREGRAROTEA rotea ON rotea.ID_REGRA_ROTEAM = rot.ID_REGRA_ROTEAM 
LEFT JOIN sisred.TBSERVICREDE sr ON sr.ID_SERVIC_REDE = rot.ID_SERVIC_REDE
LEFT JOIN sisinv.TBELEMENREDE ele ON ele.ID_ELEMEN_REDE = rot.ID_ELEMEN_REDE 
WHERE sa.CD_SERV_APROV LIKE '{sa}' AND rotea.CD_REGRA_ROTEAM LIKE '{rotea}'"""


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
    """
        Busca o plano de teste inteiro na pasta configurada e retorna um DataFrame com os dados já tratados.
    """
    # with open("PLANO_TESTE/plano_de_teste_automatizado.ods", "r") as plano:
    #print(os.getcwd())
    df = pd.read_excel(PLANO_DE_TESTE)
    # print(df)
    replaced_df = df.fillna("-") #.replace(0.0, 0)
    #df[list("ABCD")] = df[list("ABCD")].fillna(0.0).astype(int)
    return replaced_df
   
    #replaced_df = replaced_df.replace(0.0, 0)
    # print(replaced_df)
    #achou_regra_recuperada = df.loc[df["CD_REGRA_ENRIQ"] == "LineIdIptv"]
    #regra_do_bd = achou_regra_recuperada["CD_REGRA_ENRIQ"].get(0)
    #serv_aprov = replaced_df["CD_SERV_APROV"].get(0)
    #regra_enrich = replaced_df["CD_REGRA_ENRIQ"].get(0)

    #print(serv_aprov, regra_enrich)
    


"""Teste get plano
"""
# get_plano_teste()



def get_testcase_enrich_rule(num_linha_ct, plano_de_teste_df: DataFrame):
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

def get_testcase_router_rule(num_linha_ct, plano_de_teste_df: DataFrame):
    # for i in range(0, len(plano_de_teste_df)):
    linha_ct = plano_de_teste_df.loc[num_linha_ct]
    print(f"printando linha: {num_linha_ct} = {linha_ct.values}")
    #CD_SERV_APROV CD_REGRA_ROTEAM	CD_SERVIC_REDE	CD_ELEMEN_REDE	ORDEM_EXECUCAO
#    print(f"Print tuple: {sa_router_tup}")
    #serv_aprov = linha_ct["CD_SERV_APROV"].get(0)
    #regra_enrich = linha_ct["CD_REGRA_ENRIQ"].get(0)
    #print(f"Linha: {i} == SA: {serv_aprov} --> RE: {regra_enrich}")
    # jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
    # self.
    # return con
 #   return sa_router_tup

#get_testcase_router_rule(1, get_plano_teste())
#get_caso_de_teste(get_plano_teste())

# @mark.parametrize("param, valor", carrega_dados())
# def test_two(param, valor):
#     print(param, valor)
#     assert param, valor

# @mark.parametrize("ct_serv_aprov, ct_regra_enrich", carrega_dados())
# def test_two(param, valor):
#     print(param, valor)
#     assert param, valor


def est_sa_x_regra_enrich():
    plano_de_teste_df = get_plano_teste()
    query_sa_x_enrich_df = ""

    for linha in range(0, len(plano_de_teste_df)):
        #print(f"Linha: {linha} ---> {plano_de_teste_df.values[linha]}")
        sa_ct, re_ct, ord_exec = get_testcase_enrich_rule(linha, plano_de_teste_df)
        #print(sa_ct, re_ct, ord_exec)
        df_result_query = executa_query_db(sa_ct)
        print(f"Printando display {linha}")
        display(df_result_query)
        assert_enrich_rule(re_ct, df_result_query)


def localiza_enrich_rule_no_df(df: DataFrame, nome_re):
    return df.loc[df["CD_REGRA_ENRIQ"] == nome_re]

def localiza_ord_exec_no_df(df: DataFrame, ord_exec):
    return df.loc[df["ORDEM_EXECUCAO"] == ord_exec]

def assert_enrich_rule(re_ct, ord_exec_ct, df: DataFrame):
    #if re_ct != "-":
    achou_regra_enrich = localiza_enrich_rule_no_df(df, re_ct)
    achou_regra_ord_exec = localiza_ord_exec_no_df(df, ord_exec_ct)
    #print(f"\n------> Regra localizada?  \n{achou_regra_enrich}")
    #print(f"------> A ordem de execucao foi localizada?  \n{achou_regra_ord_exec}")

    regra_enrich_do_bd = achou_regra_enrich["CD_REGRA_ENRIQ"].values
    ord_exec_do_bd = achou_regra_ord_exec["ORDEM_EXECUCAO"].values
    #print(f"\n------> Buscando regra: {re_ct}")
    print(f"\n------> Resultado esperado: {re_ct} {ord_exec_ct}")
    print(f"------> Resultado Atual: {regra_enrich_do_bd[0]} {ord_exec_do_bd}")
    #print("------> Realizando o assert da regra")
    #display(achou_regra_ord_exec)
    #solucao paleativa para o warning de lista vazia no assert
    if ord_exec_do_bd.size == 0:
        ord_exec_do_bd = ""
    
    if ord_exec_ct == "-":
        ord_exec_ct = ""

    assert re_ct == regra_enrich_do_bd
    assert ord_exec_ct == ord_exec_do_bd


def select_sa_x_enrich_rule(sa):
    """
        Realiza o select no banco configurado e faz a validação dos dados recebidos.
    """
    query_preparada = SA_X_ENRICH_QUERY.format(sa)
    with get_connection(server) as db_con:
        try:
            df = pd.read_sql_query(query_preparada, db_con)
            print("Regras encontradas para o serviço: ")
            display(df)

            achou_regra_enrich = localiza_enrich_rule_no_df(df, regra_enrich_global)
            
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


def executa_query_db(sql):
    """
        Realiza o select no banco configurado e retorna o resultado.
    """
    #query_preparada = sa_x_enrich_rule_query.format(sa = serv_aprov, re = regra_enrich)
    try:
        with get_connection(server) as db_con:
            print("------> Executando query no banco...")
            df = pd.read_sql_query(sql, db_con)
            return df
    except Exception as e:
        print(
            f"------> Não foi possível estabelecer conexão com o banco {server} \n {e}")


# test_sa_x_regra_enrich()
# print(sa_x_enrich_rule_query.format(sa))
# select_sa_x_enrich_rule_2()


# select_sa_x_enrich_rule()
# select_sa_x_enrich_rule()


def est_db_connect():
    df = pd.read_sql_query(SA_X_ENRICH_QUERY, get_connection(server))
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
    achou_regra_enrich = localiza_enrich_rule_no_df(df, regra_enrich_global)
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

def get_testcases_sa_x_router():
    """
        Carrega o plano de teste inteiro e retorna um DataFrame com as colunas
    """
    df_plano_de_teste = get_plano_teste()
    #print("Alterando o tipo da coluna ORDEM_EXECUCAO")
    #df_plano_de_teste["ORDEM_EXECUCAO"].fillna(0.0).astype(int)
    print(df_plano_de_teste)

    df_router_preparado = df_plano_de_teste[["CD_SERV_APROV", "CD_REGRA_ROTEAM", "CD_SERVIC_REDE", "CD_ELEMEN_REDE", "ORDEM_EXECUCAO"]] #, "CD_REGRA_ROTEAM", "CD_SERVIC_REDE", "CD_ELEMEN_REDE", "ORDEM_EXECUCAO"
    
    #breakpoint()
    print(df_router_preparado)

    list_params_configurados = []
    for line in df_router_preparado.values:
        #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
        #print(line)


        list_params_configurados.append(line)
    
    print("lista: ", list_params_configurados)

    return list_params_configurados
"""
    serv_aprov = df_plano_de_teste["CD_SERV_APROV"]
    regra_rotea = df_plano_de_teste["CD_REGRA_ROTEAM"]
    serv_rede = df_plano_de_teste["CD_SERVIC_REDE"]
    element_rede = df_plano_de_teste["CD_ELEMEN_REDE"]
    ord_exec_router = df_plano_de_teste["ORDEM_EXECUCAO"]
    sa_router_tup = (serv_aprov.values , regra_rotea.values, serv_rede.values, element_rede.values, ord_exec_router.values)


 """   
    #print(list_params_configurados)
    #serv_aprov = df_plano_de_teste["CD_SERV_APROV"]
    #regra_enrich = df_plano_de_teste["CD_REGRA_ENRIQ"]
    #ord_exec = df_plano_de_teste["ORDEM_EXECUCAO"]
    #df_sa_x_regra_enrich = [[serv_aprov, regra_enrich, ord_exec]]
    #print(serv_aprov)
    #print(regra_enrich)
    #print(ord_exec)
    #return df_sa_x
    # _regra_enrich
    
    #return list_params_configurados


get_testcases_sa_x_router()




def get_testcases_sa_x_enrich():
    """
        Carrega o plano de teste inteiro e retorna um DataFrame com as colunas serv_aprov, regra_enrich, ord_exec 
    """
    df_plano_de_teste = get_plano_teste()
    #print("Alterando o tipo da coluna ORDEM_EXECUCAO")
    #df_plano_de_teste["ORDEM_EXECUCAO"].fillna(0.0).astype(int)
    #display(df_plano_de_teste)
    list_params_configurados = []
    for line in df_plano_de_teste.values:
        #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
        print(line)
        list_params_configurados.append(line)   
    
    #print(list_params_configurados)
    return list_params_configurados
    #serv_aprov = df_plano_de_teste["CD_SERV_APROV"]
    #regra_enrich = df_plano_de_teste["CD_REGRA_ENRIQ"]
    #ord_exec = df_plano_de_teste["ORDEM_EXECUCAO"]
    #df_sa_x_regra_enrich = [[serv_aprov, regra_enrich, ord_exec]]
    #print(serv_aprov)
    #print(regra_enrich)
    #print(ord_exec)
    #return df_sa_x_regra_enrich
    
    
#get_testcases_sa_x_enrich()

def parametriza_sql_sa_x_regra_enrich(serv_aprov, regra_enrich):
    return SA_X_ENRICH_QUERY.format(sa = serv_aprov, re = regra_enrich)

def parametriza_sql_sa_x_router_rule_query(serv_aprov, regra_rotea):
    return SA_X_ROUTER_QUERY.format(sa = serv_aprov, rotea = regra_rotea)
    

"""
@mark.parametrize ("ct_serv_aprov, ct_regra_enrich, ct_ord_exec", get_testcases_sa_x_enrich())
def test_sa_x_enrich_rule(ct_serv_aprov, ct_regra_enrich, ct_ord_exec):
    print(f"------> Teste SA x RE x OE")
    print(f"------> parametros: SA: {ct_serv_aprov}, RE:{ct_regra_enrich}, OE: {ct_ord_exec}")
    
    if ct_regra_enrich == "-":
        print("------> Caso de teste não possui regra de enriquecimento a ser testada.")
        pytest.skip()
    else:
        sql = parametriza_sql_sa_x_regra_enrich(ct_serv_aprov, ct_regra_enrich)
        df_result_query = executa_query_db(sql)
        print(f"------> Resultado da query - RE x SA x OE:\n\n {df_result_query}")
        assert_enrich_rule(ct_regra_enrich, ct_ord_exec, df_result_query)
"""

@mark.parametrize ("ct_serv_aprov, ct_regra_router, ct_serv_rede, ct_elemen_rede, ct_ord_exec", get_testcases_sa_x_router())
def test_sa_x_router_rule(ct_serv_aprov, ct_regra_router, ct_serv_rede, ct_elemen_rede, ct_ord_exec):
    #"CD_SERV_APROV", "CD_REGRA_ROTEAM", "CD_SERVIC_REDE", "CD_ELEMEN_REDE", "ORDEM_EXECUCAO"]
    print(f"------> Teste SA x RR x SR x ELR x OE")
    print(f"------> parametros: SA:{ct_serv_aprov}, RR:{ct_regra_router}, SR:{ct_serv_rede}, ELR:{ct_elemen_rede}, OE: {ct_ord_exec}")
    
    if ct_regra_router == "-":
        print("------> Caso de teste não possui regra de enriquecimento a ser testada.")
        pytest.skip()
    else:
        sql = parametriza_sql_sa_x_router_rule_query(ct_serv_aprov, ct_regra_router)
        df_result_query = executa_query_db(sql)
        print(f"------> Resultado da query - SA x RR x SR x ELR x OE\n") #{df_result_query}
        display(df_result_query)
        #assert_enrich_rule(ct_regra_enrich, ct_ord_exec, df_result_query)




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
