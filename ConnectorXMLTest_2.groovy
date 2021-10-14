import javax.jms.*;
import groovy.xml.*;
import net.oi.sis.util.QueueGenObjectSend;

providerURL = "t3://10.61.47.142:7003"
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
while(it < 2) {
	inicio = new Date().time
	message = """${it};${inicio}"""
        externalId = "US112445_CT07_TC42848_BLOQUEAR_HSI_APC" + "_" + it;
    
    // teste de regra de enriquecimento de rede
    // base de dados: uganda.sis02
    // utilizar HLR65 para OnlineConnector
    // utilizar HLR01 para NAPTIConnector

//####################################################################
//Atenção: Início da alteração do script sender_bot.py
//####################################################################

  textMsg="""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<ns2:ProvisionerOS xmlns:ns2="http://www.oi.net.br/ProvisionerIn" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" externalId="US137018_CN03_CT02" priority="7" timeToLive="240000" url="http://10.61.44.251:9091/sis/response">
    <ServiceElements>
        <ServiceElement code="GPON_ESTADO_ONT">
            <Parameters>
                <Parameter name="LINE_ID" value="RJ-ALV03-GZTE GPON 1/1/03/06/41/1/1"/>
                <Parameter name="RACK" value="1"/>
                <Parameter name="VERSION" value="5.7"/>
                <Parameter name="SLOT" value="3"/>
                <Parameter name="VENDOR" value="ZTE"/>
                <Parameter name="SHELF" value="1"/>
                <Parameter name="MODEL" value="ISAM-7360-FX"/>
                <Parameter name="ONTID" value="41"/>
                <Parameter name="PON" value="6"/>
                <Parameter name="OLT_NAME" value="RJ-ALV03-GZTE"/>
            </Parameters>
        </ServiceElement>
    </ServiceElements>
</ns2:ProvisionerOS>

""";
    
//####################################################################
//Atenção: Fim da alteração do script sender_bot.py
//####################################################################


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
