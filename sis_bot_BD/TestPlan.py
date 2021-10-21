from typing import List
from pandas.core.frame import DataFrame
import pandas as pd



from constantes import *
#from sis_bot_BD.DbConnection import get_plano_teste

class TestPlan:

    def __init__(self, path_plano_de_teste) -> DataFrame:
        self.df_test_plan: DataFrame = pd.read_excel(path_plano_de_teste).fillna("-")
        self.df_test_case = None
        self.df_params_for_list = None
        self.list_param_values_preparados = []



    @property
    def get_plano_teste(self):
        """
            Retorna um DataFrame com os dados já tratados.
        """
        return self.df_test_plan

    def localiza_enrich_rule_no_df(self, nome_enrich_rule):
        """ retorna linha do DataFrame referente à regra de enriquecimento """
        return self.df_test_plan.loc[self.df_test_plan[CD_REGRA_ENRIQ] == nome_enrich_rule]


    def localiza_ord_exec_no_df(self, ord_exec_enrich):
        """ retorna linha do DataFrame referente à regra de roteamento """
        return self.df_test_plan.loc[self.df_test_plan[ORDEM_EXECUCAO] == ord_exec_enrich]


    def get_testcases_enrich_rule(self):
        """
            Busca certa (linha e colunas)->(caso de teste) da regra de enriquecimento.
        """
        self.df_params_for_list = self.df_test_plan[[CD_SERV_APROV, CD_REGRA_ENRIQ, ORDEM_EXECUCAO_ENRICH]]

        for line in self.df_params_for_list.values:
            #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
            print(line)
            self.list_param_values_preparados.append(line)   
        
        #print(list_params_configurados)
        return self.list_param_values_preparados



    def get_testcase_router_rule(num_linha_ct, plano_de_teste_df: DataFrame):
        """
            Busca certa (linha e colunas)->(caso de teste) da regra de roteamento.
        """
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



    def get_testcases_sa_x_router(self):
        """
            Carrega o plano de teste inteiro e retorna um DataFrame com as colunas
        """
        #df_router_preparado = self.df_test_plan[[CD_SERV_APROV, CD_REGRA_ROTEAM, CD_SERVIC_REDE, CD_ELEMEN_REDE, ORDEM_EXECUCAO]]
        self.df_params_for_list = self.df_test_plan[[CD_SERV_APROV, CD_REGRA_ROTEAM, CD_SERVIC_REDE, CD_ELEMEN_REDE, ORDEM_EXECUCAO_ROUTER]] 
                                                                                                    #coluna ORDEM_EXECUCAO do roteamento. posicao 7 no plano.
        #breakpoint()
        print(self.df_params_for_list)

        for line in self.df_params_for_list.values:
            #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
            #print(line)
            self.list_param_values_preparados.append(line)
        
        print("lista: ", self.list_param_values_preparados)

        return self.list_param_values_preparados


    # INÍCIO DOS ASSERTS 
    def assert_enrich_rule(self, re_ct, ord_exec_ct, df: DataFrame):
        """ faz o assert da regra de enriquecimento """
        achou_regra_enrich = self.localiza_enrich_rule_no_df(df, re_ct)
        achou_regra_ord_exec = self.localiza_ord_exec_no_df(df, ord_exec_ct)

        #atencao para o erro da coluna de ordem de execucao
        regra_enrich_do_bd = achou_regra_enrich[CD_REGRA_ENRIQ].values
        ord_exec_do_bd = achou_regra_ord_exec[[ORDEM_EXECUCAO_ENRICH]].values

        print(f"\n------> Resultado esperado: {re_ct} {ord_exec_ct}")
        print(f"------> Resultado Atual: {regra_enrich_do_bd[0]} {ord_exec_do_bd}")

        if ord_exec_do_bd.size == 0:
            ord_exec_do_bd = ""
        
        if ord_exec_ct == "-":
            ord_exec_ct = ""

        assert re_ct == regra_enrich_do_bd
        assert ord_exec_ct == ord_exec_do_bd



test = TestPlan(PLANO_DE_TESTE)

test.get_testcases_sa_x_router()

#test.get_testcase_router_rule()
#test.get_testcases_enrich_rule()