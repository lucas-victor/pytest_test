from IPython.display import display
from sis_bot_BD.connection import Connection

from sis_bot_BD.plano_test import *
from sis_bot_BD.sql_query import *
from sis_bot_BD.connection import *
from sis_bot_BD.constantes import *



class SqlQuery:
    
    def __init__(self, connection) -> None:
        self.connection: Connection = connection
        self.df_result_sql: DataFrame = None
        self.__string_sql = ""
        self.valor_recuperado_do_df = ""

    @property
    def get_result_sql(self):
        return self.df_result_sql

    @property
    def get_sql_parametrizado_sa_x_enrich_rule(self):
        return self.__string_sql

    @property
    def get_sql_parametrizado_sa_x_router_rule(self):
        return self.__string_sql

    def parametriza_sql_sa_x_regra_enrich(self, serv_aprov, regra_enrich):
        self.__string_sql = SA_X_ENRICH_QUERY.format(sa = serv_aprov, re = regra_enrich)

    def parametriza_sql_sa_x_router_rule_query(self, serv_aprov, regra_rotea):
        self.__string_sql = SA_X_ROUTER_QUERY.format(sa = serv_aprov, rotea = regra_rotea)

    def _read_sql_query_pd(self, query_preparada, db_con):
        self.df_result_sql = pd.read_sql_query(query_preparada, db_con)
        #self.df_result_sql = self.df_result_sql.where(self.df_result_sql==None, "-")
        self.df_result_sql = self.df_result_sql.fillna("-")
        #return self.df_result_sql

    # def _find_rule_no_df(self, nome_coluna, nome_rule):
    #     """ retorna linha do DataFrame referente à regra de enriquecimento """
    #     return self.df_result_sql.loc[self.df_result_sql[nome_coluna] == nome_rule]

    # def find_enrich_rule_no_df(self, nome_enrich_rule):
    #     """ retorna linha do DataFrame referente à regra de enriquecimento """
    #     return self.df_result_sql.loc[self.df_result_sql[CD_REGRA_ENRIQ] == nome_enrich_rule]


    # def find_router_rule_no_df(self, nome_router_rule):
    #     """ retorna linha do DataFrame referente à regra de roteamento """
    #     return self.df_result_sql.loc[self.df_result_sql[CD_REGRA_ROTEAM] == nome_router_rule]


    def executa_query_db(self):
        """
            Realiza o select no banco configurado e retorna o resultado.
        """
        #query_preparada = sa_x_enrich_rule_query.format(sa = serv_aprov, re = regra_enrich)
        try:
            with self.connection.get_connection as db_con:
                print("------> Executando query no banco...")
                self._read_sql_query_pd(self.__string_sql, db_con)
                #return self.df_result_sql
        except Exception as e:
            print(
                f"------> Não foi possível estabelecer conexão com o banco {self.connection.server_name} \n {e}")


"""

    def select_sa_x_enrich_rule(self, name_server, sa):
        ""
            Realiza o select no banco configurado e faz a validação dos dados recebidos.
        ""
        #query_preparada = SA_X_ENRICH_QUERY.format(sa)
        self.parametriza_sql_sa_x_regra_enrich()
        sql_preparado = self.get_sql_parametrizado_sa_x_enrich_rule()

        self.executa_query_db(sql_preparado)



        with self.connection.get_connection as db_con:
            try:
                self._read_sql_query_pd(sql_preparado, db_con)
                print("Regras encontradas para o serviço: ")
                display(df)

                achou_regra_enrich = self.find_enrich_rule_no_df(regra_enrich_global)
              
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

"""
    