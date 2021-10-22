from IPython.display import display
from sis_bot_BD.connection import Connection

from sis_bot_BD.test_plan import *
from sis_bot_BD.sql_query import *
from sis_bot_BD.connection import *
from sis_bot_BD.constantes import *



class SqlQuery:
    
    def __init__(self, connection) -> None:
        self.connection: Connection = connection
        self.df_result_sql: DataFrame = None
        self.__string_sql = ""


    def parametriza_sql_sa_x_regra_enrich(self, serv_aprov, regra_enrich):
        self.__string_sql = SA_X_ENRICH_QUERY.format(sa = serv_aprov, re = regra_enrich)

    def parametriza_sql_sa_x_router_rule_query(self, serv_aprov, regra_rotea):
        self.__string_sql = SA_X_ROUTER_QUERY.format(sa = serv_aprov, rotea = regra_rotea)
    
    def get_sql_parametrizado_sa_x_enrich_rule(self):
        return self.__string_sql
    
    def get_sql_parametrizado_sa_x_router_rule(self):
        return self.__string_sql


    def select_sa_x_enrich_rule(self, name_server, sa):
        """
            Realiza o select no banco configurado e faz a validação dos dados recebidos.
        """
        query_preparada = SA_X_ENRICH_QUERY.format(sa)
        with self.connection.get_connection(name_server) as db_con:
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


    def executa_query_db(self):
        """
            Realiza o select no banco configurado e retorna o resultado.
        """
        #query_preparada = sa_x_enrich_rule_query.format(sa = serv_aprov, re = regra_enrich)
        try:
            with self.connection.get_connection() as db_con:
                print("------> Executando query no banco...")
                df = pd.read_sql_query(self.__string_sql, db_con)
                return df
        except Exception as e:
            print(
                f"------> Não foi possível estabelecer conexão com o banco {self.connection.server_name} \n {e}")