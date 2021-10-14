from io import StringIO
import re #RegEx - 
import shutil #possui o copy2 para copiar arquivos
import os, sys, subprocess, time
import pexpect #manipula terminal, possivel automação de tarefas. responde comandos.

USER_HISTORY='US000000'
USER='rootsis'
USER_PASS='chetR4ku'
PATH_OSSENDER_GROOVYS=f'/appl-sis-2/sis/utilitarios/osSenderWeblogic/'
PATH_OSSENDER_EXECUTABLE=f'{PATH_OSSENDER_GROOVYS}bin/'
PATH_LOGS='/appl-sis-2/sis/logs/'
PATH_MONITORPY_LOG=''
PATH_UTILITARIOS='/appl-sis-2/sis/utilitarios/'
PATH_DEST_EVD_FOLDER= f'{PATH_OSSENDER_GROOVYS}EVIDENCIAS_{USER_HISTORY}/'
ARQ_MONITORPY_LOG='monitorPy.log'
HOST='10.61.47.138'
NOME_GROOVY_MODELO='ConnectorXMLTest.groovy'


#testes
nome = 'CN03_CT01_GPON_ESTADO_ONT.txt'
patht = 'ENTRADAS'
path1 = 'ENTRADAS1'
path2 = 'ENTRADAS2'


def get_resp_regra(regra):
    with open('EVIDENCIAS/EVD_US137018_CN03_CT01_28.09.2021.19.57.log') as arq:
        for line in arq:
            #
            if regra in line:
                posicao_regra = line.find('[')
                posicao_fim_regra = line.find(']')
                p = line[posicao_regra:posicao_fim_regra+1]
                print(p)

#get_resp_regra('.rul.')

#verifica se dir existe, senao cria e copia a evidencia para a pasta de log
#ATENCAO alterar para os paths corretos.
def get_evd(path_evd, nome_evd):
    #   if not path.Path.exists(PATH_EVD_FOLDER):
    if not os.path.exists(path2):
        print(f'criando diretorio {path2}')
        os.makedirs(path2)

    if os.path.exists(patht):
        print("Copiando o arquivo para a pasta logs2")
        #resp_com = os.popen(f"cp -v {patht}/{nome_evd} logs2/").read()
        #shutil.copy2(patht+'/'+nome_evd, 'logs2',)
        absoluty_path_evd = os.path.join(patht, nome_evd)
        shutil.copy2(absoluty_path_evd, 'logs2', )

        print(f'{absoluty_path_evd}', 'logs2')

'''    if not os.path.exists(PATH_EVD_FOLDER):
        os.makedirs(PATH_EVD_FOLDER)
    if os.path.exists(PATH_LOGS + nome_evd):
        os.popen(f"cp {PATH_LOGS}{nome_evd} {PATH_EVD_FOLDER}")
'''

#get_evd(patht, nome)

##pega nome da evidencia gerada e retorna
def pega_nome_evd(log_py):
    #encontrar_string(log_py, ".*.log")
    with open(log_py,'r') as f:
        texto=f.read()

    lista_palavras = texto.split(' ')
    for palavra in lista_palavras:
        if '.log' in palavra:
            nome_evd = palavra

    return nome_evd


def executa_ossender():
    #subprocess.run(['/appl-sis-2/sis/utilitarios/osSenderWeblogic/bin/./osSender.sh ../ConnectorXMLTest.groovy'] )
    resp_comando = os.popen("/appl-sis-2/sis/utilitarios/osSenderWeblogic/bin/./osSender.sh ../ConnectorXMLTest.groovy").read()
    print("osSender.sh executado com sucesso. Resposta da execução: ")
    print(resp_comando)

def pexpect_test(comando):
    child = pexpect.spawn(comando)
#    print(child.read())
   # child.expect(pexpect.EOF)
    child.expect(".*password:")
    child.sendline(comando + ' -lathr')
    print(child.read())

#executa monitor na sisdx02, aguarda tempo e gera evidencia. gerando arquivo de log dos passos.
def exec_monitor(): #conn_file, prov_file, net_file, adapter_file
    print("Conectando no host para executar monitor")
    child = pexpect.spawn(f'ssh {USER}@{HOST}')
    log = open(ARQ_MONITORPY_LOG, 'wb')
    child.logfile = log
    child.expect(".*assword:")
    child.sendline(USER_PASS)
    child.expect(".*~>")
    print("Login efetuado com sucesso!")
    child.sendline(f"cd {PATH_LOGS}")
    child.expect(".*logs>")
    #child.sendline(f'/appl-sis-2/sis/logs2/./monitor.sh {conn_file} {prov_file} {net_file} {adapter_file}')
    print("Executando o monitor.sh")
    child.sendline(f'./monitor.sh connector-jms-td_vrainst01.log adapter-HDM04_vrainst01.log')
    child.expect(".*(S/n)")
    print("Monitor.sh executado com sucesso. Enviar OS")

    #executa ossender para enviar OS
    print("Executando OS sender...")
    executa_ossender()

    time.sleep(10)
    child.sendline('s')
    child.expect(".*Evidencia gerada")
    print("Evidencias gerada com sucesso")
    log.close()


#retorna lista dos arquivos de entrada (OSs).
def lista_oss(pathdir):
    dir_list = os.listdir(pathdir)
    os_list = []
    diretorio = os.getcwd() + "/ENTRADAS/"
    for file in dir_list:
        print(file)
        full_path = diretorio + file
        with open(full_path, 'r') as file_os:
            texto_os = file_os.read()
            #os_list = [texto_os]
            os_list.append(f'  textMsg="""{texto_os}""";')
    print(len(os_list))
    print(os_list)
    os_list.sort()
    return os_list

#le texto da OS e retorna o conteudo para ser alterado no arquivo de envio.
def ler_os(path_file):
    with open(path_file, 'r') as f:
        texto = f.read()
    return f'  textMsg="""{texto}""";'

#encontra linha do groovy para adicionar a OS.
def encontrar_string(path_file,string):
    with open(path_file,'r') as f:
        texto=f.readlines()
    for i in texto:
        if string in i:
            print(f"A linha a ser alterada no arquivo é: {texto.index(i)}")
            return texto.index(i)
    print('String não encontrada')


#Altera a linha especifica do groovy de envio das OSs.
def alterar_linha(path_file, index_linha, nova_linha, file_out_id):
    with open(path_file,'r') as f:
        texto=f.readlines()
        nome_split = path_file.split('.')
        novo_nome = NOME_GROOVY_MODELO.split('.')
        ##file_out_id + '_' + path_file
    with open(novo_nome[0] + '_' + file_out_id + '.' + novo_nome[1], 'w') as f:
        for linha in texto:
            if texto.index(linha) == index_linha:
                f.write(nova_linha+'\n')
            else:
                f.write(linha)

# 1 - pega lista OSs
lista_os = lista_oss('ENTRADAS/')

path = 'GROOVYS/modelo_groovy_osSender.groovy'
string = 'textMsg='

# 2 - percorre lista de OSs criando os groovys
count = 0
for file in lista_os:
    count += 1

#    path_file = f'ENTRADAS/{file}'
    #conteudo_os = ler_os(path_file)

    # texto_nova_linha = 'textMsg=""teste alteracao lucas"";'
    linha_a_substituir = encontrar_string(path, string)

    # print(linha_a_substituir)
    alterar_linha(path, linha_a_substituir, file, str(count))

    #executa monitor e chama também o executa_ossender() faz o envio aguarda 10 seg e gera a evd.
    #exec_monitor()

#    Foi comentado aqui para ficar dentro do metodo exec_monitor()
#    #executa ossender para enviar OS
#    executa_ossender()



log_py = 'monitorPy.log'
#pega_nome_evd(log_py)

#print(pega_nome_evd(log_py))


#lista_oss('ENTRADAS')
#exec_monitor()

#dir = os.listdir()
#print(dir)

#exec_monitor()


#text = os.popen("ls -lathr").read()
#print(text)

#for linha in text.split('\n'):
#    if 'weblogicSend.py' in linha:
#        print(linha)