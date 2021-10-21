import os
import shutil


def organiza_arqs():
    path = os.getcwd()

    lista_de_arquivos = os.listdir()
    #print(lista_de_arquivos)
    for file in lista_de_arquivos:
        if "organizaArqs.py" != file:
            if os.path.isfile(file) and "." in file:
                nome_arq = file
                tup_nome_e_extensao = nome_arq.split('.')

                nome, extensao = tup_nome_e_extensao
                new_dir = f"./{extensao}"
                if not os.path.exists(extensao):
                    os.mkdir(extensao)

                full_path_src = os.path.join(os.getcwd(), file)
                
                print(f"Copiando...: {file} ---> Dir: {extensao}")
                shutil.copy2(full_path_src, extensao)

    # print(lista_de_arquivos)


organiza_arqs()
