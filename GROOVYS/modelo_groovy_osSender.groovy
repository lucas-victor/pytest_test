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

   textMsg="""""";
    
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
