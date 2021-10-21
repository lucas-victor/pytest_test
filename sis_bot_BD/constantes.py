#strings de conexao dos ambientes(ip)
SISDX02='sis/sis@10.61.47.138/sisdev2'
SISDX03='sis/sis@10.61.47.141/sisdev3'
SISDX04='sis/sis@10.61.47.142/sisdev4'
SISDX05='sis/sis@10.61.47.140/sisdev5'
SISDX06='sis/sis@10.61.47.144/sisdev6'
SISDX07='sis/sis@10.61.47.145/sisdev7'
SISDX08='sis/sis@10.61.47.146/sisdev8'
SISDX09='sis/sis@10.61.47.147/sisdev9'

PLANO_DE_TESTE = "../PLANO_TESTE/plano_de_teste_automatizado.ods"
#PLANO_DE_TESTE = "PLANO_TESTE/plano_de_teste_automatizado.ods"

#Colunas do aprovisionamento
CD_SERV_APROV = "CD_SERV_APROV"
    #enriquecimento
CD_REGRA_ENRIQ = "CD_REGRA_ENRIQ"
ORDEM_EXECUCAO = "ORDEM_EXECUCAO"
ORDEM_EXECUCAO_ENRICH = "ORDEM_EXECUCAO_ENRICH"
#ORDEM_EXECUCAO_ENRICH = 2
    #roteamento
CD_REGRA_ROTEAM = "CD_REGRA_ROTEAM"
CD_SERVIC_REDE = "CD_SERVIC_REDE"
CD_ELEMEN_REDE = "CD_ELEMEN_REDE"
ORDEM_EXECUCAO = "ORDEM_EXECUCAO"
ORDEM_EXECUCAO_ROUTER = "ORDEM_EXECUCAO_ROUTER"
#ORDEM_EXECUCAO_ROUTER = 7 #posicao. campo mesmo nome.


#Colunas da network


#Selects SA
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