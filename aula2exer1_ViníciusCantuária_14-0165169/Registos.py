from Arquivo import le_arquivo
from Proprietario import pega_carros_do_proprietario, visualiza_proprietario_carros


def visualiza_registros():
    proprietarios = le_arquivo('Proprietários Cadastrados')
    carros = le_arquivo('Carros Cadastrados')

    for proprietario in proprietarios:
        placas = pega_carros_do_proprietario(proprietario)
        proprietario = proprietario.__str__().split('\n')[0].split(' ')
        visualiza_proprietario_carros(proprietario, carros, placas)
