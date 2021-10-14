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

textMsg="""teste alteracao lucas""";
    
//trecho alterado pelo script de envio automatizado .py
//   textMsg="""""";

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
