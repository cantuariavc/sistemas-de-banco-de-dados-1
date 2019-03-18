import os


def pega_caminho_arquivo(nome_arquivo):
    return '{}/{}.txt'.format(os.path.dirname(os.path.abspath(__file__)), nome_arquivo)


def e_arquivo_vazio():
    return os.stat(pega_caminho_arquivo('Carros Cadastrados')).st_size == 0


def abre_arquivo(nome_arquivo, modo):
    arquivo = None
    caminho_arquivo = pega_caminho_arquivo(nome_arquivo)

    if not os.path.isfile(caminho_arquivo):
        arquivo = open(caminho_arquivo, 'w+')
        arquivo.close()

    if modo == 'w':
        arquivo = open(caminho_arquivo, 'w')
    elif modo == 'r':
        arquivo = open(caminho_arquivo, 'r')

    return arquivo


def le_arquivo(nome_arquivo):
    arquivo = abre_arquivo(nome_arquivo, 'r')
    conteudo = arquivo.readlines()
    arquivo.close()

    return conteudo


def escreve_arquivo(nome_arquivo, conteudo):
    arquivo = abre_arquivo(nome_arquivo, 'w')
    arquivo.writelines(conteudo)
    arquivo.close()
