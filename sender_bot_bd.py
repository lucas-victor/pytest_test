"""
Todos os ips.

alias tosisdx02='ssh rootsis@10.61.47.138'
alias tosisdx02_tr698043='ssh tr698043@10.61.47.138'
alias tosisdx03='ssh rootsis@10.61.47.141'
alias tosisdx04='ssh rootsis@10.61.47.142'
alias tosisdx04_tr698043='ssh tr698043@10.61.47.142'
alias tosisdx05='ssh rootsis@10.61.47.140'
alias tosisdx06='ssh rootsis@10.61.47.144'
alias tosisdx06_tr698043='ssh tr698043@10.61.47.144'
alias tosisdx07='ssh rootsis@10.61.47.145'
alias tosisdx07_tr698043='ssh tr698043@10.61.47.145'
alias tosisdx08='ssh rootsis@10.61.47.146'
alias tosisdx08_tr698043='ssh tr698043@10.61.47.146'
alias tosisdx09='ssh rootsis@10.61.47.147'
alias tosislab='ssh rootsis@10.121.216.69'
alias tosislab_beaadmin='ssh beaadmin@10.121.216.69'
alias tosisprd38='ssh rootsis@10.32.216.11'
alias tosisprd39='ssh rootsis@10.32.216.24'
alias tosisprd40='ssh rootsis@10.32.216.25'
alias tosisprd41='ssh rootsis@10.32.216.26'
alias tosisprd42='ssh rootsis@10.32.216.32'
alias tosisprd43='ssh rootsis@10.32.216.33'
alias tosispx15='ssh rootsis@10.32.206.152'
alias tosispx16='ssh rootsis@10.32.206.153'
alias tosispx17='ssh rootsis@10.32.206.155'
alias tosispx18='ssh rootsis@10.32.206.163'
alias tosispx19='ssh rootsis@10.32.206.164'
alias tosispx20='ssh rootsis@10.32.206.165'
alias tosisqx04a_ti_movel='ssh rootsis@10.58.167.127'
alias tosisqx04b_ti_movel='ssh rootsis@10.58.167.128'
alias tosisqx04c_ti_fixa='ssh rootsis@10.58.167.129'
alias tosisqx04d_ti_fixa='ssh rootsis@10.58.167.130'
alias tosisqx09a_trg_movel='ssh rootsis@10.58.227.27'
alias tosisqx09b_trg_movel='ssh rootsis@10.58.227.28'
alias tosisqx09c_trg_fixa='ssh rootsis@10.58.227.29'
alias tosisqx09d_trg_fixa='ssh rootsis@10.58.227.30'
"""
import pytest
import cx_Oracle

#jdbc:oracle:thin:@//sisdev4-h1:1549/sisdev4
con = cx_Oracle.connect('sis/sis@sisdev6-h1/sisdev6')

cursor = con.cursor()
querystring = "SELECT * FROM sisinv.TBELEMENREDE ele WHERE ele.CD_ELEMEN_REDE LIKE '%ZTE%'"

cursor.execute(querystring)
result_one_line = cursor.fetchone()
count = 0
#print(result)
if result_one_line == None:
    print("Nenhum resultado para a query realizada.")
    exit()
else:
    while result_one_line:
        count += 1
        print(result_one_line)
        for campo in result_one_line:
           if str(campo).find("ZTE_NetQ") != -1:
              print(f"encontrei o texto ZTE_NetQ na posicao {result_one_line.index(campo)} na linha {count}")
#           if "ZTE_NetQ" in str(campo):
#

        result_one_line = cursor.fetchone()
        #print(f"resultado depois do fetch do while:\n {result}")

cursor.close()
#print(con.version)
con.close()