


from connection import Connection
from constantes import SA_X_ENRICH_QUERY



def select_sa_x_enrich_rule(name_server, sa):
    """
        Realiza o select no banco configurado e faz a validação dos dados recebidos.
    """
    query_preparada = SA_X_ENRICH_QUERY.format(sa)
    with Connection.get_connection(name_server) as db_con:
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