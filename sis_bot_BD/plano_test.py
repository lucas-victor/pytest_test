from IPython.display import display
#from typing import List
from pandas.core.frame import DataFrame
import pandas as pd


from sis_bot_BD.constantes import *
#from sis_bot_BD.DbConnection import get_plano_teste

class PlanoTeste:

    def __init__(self, path_plano_de_teste) -> DataFrame:
        self.df_test_plan: DataFrame = pd.read_excel(path_plano_de_teste).fillna("-")
        self.df_test_case: DataFrame = None
        self.df_test_case_result = ""
        self.df_params_for_list = None
        self.list_param_values_preparados = []


    @property
    def get_plano_teste(self):
        """
            Retorna um DataFrame com os dados já tratados.
        """
        return self.df_test_plan


    def _find_rule_no_df_testcase(self, nome_coluna, nome_rule):
        """ retorna linha do DataFrame referente à regra de enriquecimento """
        return self.df_test_case.loc[self.df_test_case[nome_coluna] == nome_rule]


    def _find_rule_no_df_testresult(self, nome_coluna, nome_rule, df: DataFrame):
        """ retorna linha do DataFrame referente à regra """
        self.df_test_case_result = df.loc[df[nome_coluna] == nome_rule]
        return self.df_test_case_result

    # def find_enrich_rule_no_df(self, nome_enrich_rule):
    #     """ retorna linha do DataFrame referente à regra de enriquecimento """
    #     return self.df_test_plan.loc[self.df_test_plan[CD_REGRA_ENRIQ] == nome_enrich_rule]

    # def find_ord_exec_no_df(self, ord_exec_enrich):
    #     """ retorna linha do DataFrame referente à regra de roteamento """
    #     return self.df_test_plan.loc[self.df_test_plan[ORDEM_EXECUCAO_ENRICH] == ord_exec_enrich]

    def get_valor_do_campo(self, num_linha: int, num_coluna: int, df: DataFrame):
        return df.iat[num_linha, num_coluna]


    def get_testcases_enrich_rule(self):
        """
            Busca certa (linha e colunas)->(caso de teste) da regra de enriquecimento.
        """
        self.df_params_for_list = []
        self.list_param_values_preparados = []
        self.df_params_for_list = self.df_test_plan[[CD_SERV_APROV, CD_REGRA_ENRIQ, ORDEM_EXECUCAO_ENRICH]]

        for line in self.df_params_for_list.values:
            #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
            print(line)
            self.list_param_values_preparados.append(line)   
        
        #print(list_params_configurados)
        return self.list_param_values_preparados


    """def get_testcases_sa_x_enrich(self):
        ""
            Carrega o plano de teste inteiro e retorna um DataFrame com as colunas serv_aprov, regra_enrich, ord_exec 
        ""
        self.df_params_for_list = self.df_test_plan[[]]
        df_plano_de_teste = get_plano_teste()

        list_params_configurados = []
        for line in df_plano_de_teste.values:
            #cts_tup = (line[["CD_SERV_APROV","CD_REGRA_ENRIQ","ORDEM_EXECUCAO"]])
            print(line)
            list_params_configurados.append(line)   
        
        #print(list_params_configurados)
        return list_params_configurados"""




    # def get_testcase_router_rule(num_linha_ct, plano_de_teste_df: DataFrame):
    #     """
    #         Busca certa (linha e colunas)->(caso de teste) da regra de roteamento.
    #     """
    #     # for i in range(0, len(plano_de_teste_df)):
    #     linha_ct = plano_de_teste_df.loc[num_linha_ct]
    #     print(f"printando linha: {num_linha_ct} = {linha_ct.values}")
    #     #CD_SERV_APROV CD_REGRA_ROTEAM	CD_SERVIC_REDE	CD_ELEMEN_REDE	ORDEM_EXECUCAO
    # #    print(f"Print tuple: {sa_router_tup}")
    #     #serv_aprov = linha_ct["CD_SERV_APROV"].get(0)
    #     #regra_enrich = linha_ct["CD_REGRA_ENRIQ"].get(0)
    #     #print(f"Linha: {i} == SA: {serv_aprov} --> RE: {regra_enrich}")
    #     # jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
    #     # self.
    #     # return con
    # #   return sa_router_tup



    def get_testcases_sa_x_router(self):
        """
            Carrega as colunas o plano de teste inteiro e retorna um DataFrame com as colunas
        """
        #df_router_preparado = self.df_test_plan[[CD_SERV_APROV, CD_REGRA_ROTEAM, CD_SERVIC_REDE, CD_ELEMEN_REDE, ORDEM_EXECUCAO]]
        self.df_params_for_list = []
        self.list_param_values_preparados = []
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
    def assert_enrich_rule(self, sa_ct, re_ct, ord_exec_ct, df: DataFrame):
        """ faz o assert da regra de enriquecimento """
        #pega 
        self._find_rule_no_df_testresult(CD_REGRA_ENRIQ, re_ct, df)
        
        serv_aprov_bd = ""
        regra_enrich_do_bd = ""
        ord_exec_do_bd = ""
        
        if self.df_test_case_result.size != 0:
            serv_aprov_bd = self.get_valor_do_campo(0, 0, self.df_test_case_result)
            regra_enrich_do_bd = self.get_valor_do_campo(0, 1, self.df_test_case_result)
            ord_exec_do_bd = self.get_valor_do_campo(0, 2, self.df_test_case_result)
        
        print(f"\n--> Resultado esperado: SA:{sa_ct} RE:{re_ct} OE:{ord_exec_ct}")
        print(f"--> Resultado Atual:    SA:{serv_aprov_bd} RE:{regra_enrich_do_bd} OE:{ord_exec_do_bd} \n\n")

        assert re_ct == regra_enrich_do_bd
        assert ord_exec_ct == ord_exec_do_bd



    def assert_router_rule(self, sa_ct, rr_ct, sr_ct, ele_ct, ord_exec_ct, df: DataFrame):
            """ faz o assert da regra de enriquecimento """
            #pega 
            self._find_rule_no_df_testresult(CD_REGRA_ROTEAM, rr_ct, df)
            
            serv_aprov_bd = ""
            regra_router_bd = ""
            serv_rede_bd = ""
            ele_rede_bd = ""
            ord_exec_do_bd = ""
            #CD_SERV_APROV, CD_REGRA_ROTEAM, CD_SERVIC_REDE, CD_ELEMEN_REDE, ORDEM_EXECUCAO_ROUTER
            if self.df_test_case_result.size != 0:
                serv_aprov_bd = self.get_valor_do_campo(0, 0, self.df_test_case_result)
                regra_router_bd = self.get_valor_do_campo(0, 1, self.df_test_case_result)
                serv_rede_bd = self.get_valor_do_campo(0, 2, self.df_test_case_result)
                ele_rede_bd = self.get_valor_do_campo(0, 3, self.df_test_case_result)
                ord_exec_do_bd = self.get_valor_do_campo(0, 4, self.df_test_case_result)
            
            print(f"\n--> Resultado esperado: SA:{sa_ct} RR:{rr_ct} SR:{sr_ct} ELE:{ele_ct} OE:{ord_exec_ct}")
            print(f"--> Resultado Atual:    SA:{serv_aprov_bd} RR:{regra_router_bd} SR:{serv_rede_bd} ELE:{ele_rede_bd} OE:{ord_exec_do_bd} \n\n")

            assert rr_ct == regra_router_bd
            assert ord_exec_ct == ord_exec_do_bd



#
# test = TestPlan(PLANO_DE_TESTE)

#test.get_testcases_sa_x_router()           

#test.get_testcase_router_rule()
#test.get_testcases_enrich_rule()