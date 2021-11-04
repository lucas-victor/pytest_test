from pytest import mark, fixture
from IPython.display import display
import pytest
from sis_bot_BD.plano_test import *
from sis_bot_BD.sql_query import *
from sis_bot_BD.connection import *
from sis_bot_BD.constantes import *
#from sis_bot_BD.DbConnection import * #executa_query_db, parametriza_sql_sa_x_router_rule_query, parametriza_sql_sa_x_regra_enrich, assert_enrich_rule, get_testcases_sa_x_router                                        

#import pytest
"""
@fixture
def fixture_testplan():
    return PlanoTeste(PLANO_DE_TESTE).get_plano_teste
"""
tp = PlanoTeste(PLANO_DE_TESTE)
con = Connection("sisdx06")
sql = SqlQuery(con)


@mark.parametrize("ct_serv_aprov, ct_regra_enrich, ct_ord_exec", tp.get_testcases_enrich_rule())
def test_sa_x_enrich_rule(ct_serv_aprov, ct_regra_enrich, ct_ord_exec):
    """
    Testa as regras de enriquecimento do serviço de aprovisionamento.
    """
    print(f"--> Teste SA x RE x OE")
    print(f"--> parametros: SA: {ct_serv_aprov}, RE:{ct_regra_enrich}, OE: {ct_ord_exec}")
    
    if ct_regra_enrich == "-":
        print("--> Caso de teste não possui regra de enriquecimento a ser testada.")
        pytest.skip()
    else:
        sql.parametriza_sql_sa_x_regra_enrich(ct_serv_aprov, ct_regra_enrich)
        sql.executa_query_db()
        print(f"--> Resultado da query - SA x RE x OE:\n\n {sql.get_result_sql}")
        tp.assert_enrich_rule(ct_serv_aprov, ct_regra_enrich, ct_ord_exec, sql.get_result_sql)



@mark.parametrize ("ct_serv_aprov, ct_regra_router, ct_serv_rede, ct_elemen_rede, ct_ord_exec", tp.get_testcases_sa_x_router())
def test_sa_x_router_rule(ct_serv_aprov, ct_regra_router, ct_serv_rede, ct_elemen_rede, ct_ord_exec):
    """
    Testa as regras de roteamento do serviço de aprovisionamento.
    """
    #"CD_SERV_APROV", "CD_REGRA_ROTEAM", "CD_SERVIC_REDE", "CD_ELEMEN_REDE", "ORDEM_EXECUCAO"]
    print(f"--> Teste SA x RR x SR x ELR x OE")
    print(f"--> parametros: SA:{ct_serv_aprov}, RR:{ct_regra_router}, SR:{ct_serv_rede}, ELR:{ct_elemen_rede}, OE: {ct_ord_exec}")

    if ct_regra_router == "-":
        print("--> Caso de teste não possui regra de enriquecimento a ser testada.")
        pytest.skip()
    else:
        sql.parametriza_sql_sa_x_router_rule_query(ct_serv_aprov, ct_regra_router)
        sql.executa_query_db()
        print(f"--> Resultado da query - SA x RR x SR x ELR x OE\n") #{df_result_query}
        display(sql.get_result_sql)
        #assert_enrich_rule(ct_regra_enrich, ct_ord_exec, df_result_query)