from Carro import registra_carro, procura_carro
from Proprietario import procura_proprietario
from Registos import visualiza_registros


def menu(opcao):
    try:
        print('\tMenu')
        print('0 - Sair\n')
        print('1 - Cadastrar carro\n')
        print('2 - Pesquisar por proprietário\n')
        print('3 - Pesquisar por veículo\n')
        print('4 - Vizualizar todos os registros\n')
        opcao = int(input('Opcao: '))
    except ValueError:
        pass

    print('\n')

    return opcao


def escolha(opcao):
    if opcao == 1:
        registra_carro()
    elif opcao == 2:
        procura_proprietario()
    elif opcao == 3:
        procura_carro()
    elif opcao == 4:
        visualiza_registros()
