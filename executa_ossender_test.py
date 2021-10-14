# -*- coding: utf-8 -*-
#comentario necessário para executar no servidor sisdx04 por conter caracteres ASCII

#funcao testada na sisdx04. Funcionou corretamente.
import os

def executa_ossender():
    #subprocess.run(['/appl-sis-2/sis/utilitarios/osSenderWeblogic/bin/./osSender.sh ../ConnectorXMLTest.groovy'] )
    resp_comando = os.popen("/appl-sis-2/sis/utilitarios/osSenderWeblogic/bin/./osSender.sh ../ConnectorXMLTest.groovy").read()
    print("osSender.sh executado com sucesso. Resposta da execução: ")
    print(resp_comando)


executa_ossender()
