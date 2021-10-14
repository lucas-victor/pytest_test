import javax.jms.*;
import groovy.xml.*;
import net.oi.sis.util.QueueGenObjectSend;

providerURL = "t3://172.26.36.16:7001"
queueNameIn = "sis.wms.OnlineConnectorInQueue"
//queueNameIn = "sis.vas.OnlineConnectorInQueue"
//queueNameIn = "sis.mesox.OnlineConnectorInQueue"

jndiFactory = "weblogic.jndi.WLInitialContextFactory";
authenticationType = null
userID = null
password = null
//jmsFactory = "sis.JMSConnectionFactory"
jmsFactory = "sis.ConnectorJMSConnectionFactory"

QueueGenObjectSend qs = new QueueGenObjectSend();
qs.init(jndiFactory, providerURL, authenticationType, userID, password,
		queueNameIn, jmsFactory)

int qtdMsgEnviada = 0
int tempoMedioEnvio = 0
println "Enviando... "

inicioProcessamento = new Date().time

//1.times() {
int it = 1
while(it <= 2) {
	inicio = new Date().time
	message = """${it};${inicio}"""
        externalId = "US112445_CT07_TC42848_BLOQUEAR_HSI_APC" + "_" + it;
    
    // teste de regra de enriquecimento de rede
    // base de dados: uganda.sis02
    // utilizar HLR65 para OnlineConnector
    // utilizar HLR01 para NAPTIConnector

   textMsg="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<prov:ProvisionerOS xmlns:prov="http://www.oi.net.br/ProvisionerIn" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" externalId="$externalId" priority="1" systemId="wms">
    <ServiceElements>
        <ServiceElement code="BLOQUEAR_HSI_APC"/>
    </ServiceElements>
    <Parameters>
        <Parameter name="ACESSO_ASSET_ID" value="4-3MB46K1"/>
        <Parameter name="ACESSO_ASSET_ID_OLD" value=""/>
        <Parameter name="ACESSO_ASSET_ID_OLD" value=""/>
        <Parameter name="C_VLAN_HSI" value="1193"/>
        <Parameter name="C_VLAN_HSI_OLD" value=""/>
        <Parameter name="LINE_ID_HSI_OLD" value=""/>
        <Parameter name="LINE_ID_HSI" value="MG-BGU02-GALC GPON 1/1/07/04/1/1/1:1193/210"/>
        <Parameter name="GALC" value="MG-BGU02-GALC"/>
        <Parameter name="OLT_PORT" value="4"/>
        <Parameter name="RACK" value="1"/>
        <Parameter name="OLT_SHELF" value="1"/>
        <Parameter name="OLT_SLOT" value="7"/>
        <Parameter name="S_VLAN_HSI" value="4007"/>
        <Parameter name="S_VLAN_HSI_OLD" value=""/>
        <Parameter name="CDOI_SPLITER_PORT" value="6"/>
        <Parameter name="NUMERO_OS" value="4-7882168363"/>
        <Parameter name="HSI_ASSET_ID" value="4-3MB4FO7"/>
        <Parameter name="VELOCIDADE_DOWN" value="200"/>
        <Parameter name="VELOCIDADE_DOWN_OLD" value=""/>
        <Parameter name="VELOCIDADE_UP" value="15"/>
        <Parameter name="VELOCIDADE_UP_OLD" value=""/>
        <Parameter name="FABRICANTE_OLT" value="ALCATEL"/>
    </Parameters>
</prov:ProvisionerOS>""";


// FIM

			
	qs.sendText(textMsg)
	qtdMsgEnviada++
	fim = new Date().time
	tempoEnvio = fim-inicio
	tempoMedioEnvio += tempoEnvio 
	println "$it;$inicio"
	it++
}

	tempoTotalProcessamento = (new Date().time - inicioProcessamento) / 60000
	
	println "	Tempo total de processamento (min):............ $tempoTotalProcessamento"

tempoMedioEnvio = tempoMedioEnvio/qtdMsgEnviada

println """
	Mensagens enviadas:............. $qtdMsgEnviada
	Tempo m�dio para envio (ms):.... $tempoMedioEnvio
"""

qs.close()
