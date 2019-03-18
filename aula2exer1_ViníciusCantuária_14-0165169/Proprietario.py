from Arquivo import le_arquivo


class Proprietario:
    def __init__(self, cpf, primeiro_nome, ultimo_nome, placa_carro):
        self.__cpf = cpf
        self.__primeiro_nome = primeiro_nome
        self.__ultimo_nome = ultimo_nome
        self.__placas_carros = [placa_carro]

    def __str__(self):
        return '{} {} {} {}\n'.format(self.__cpf, self.__primeiro_nome, self.__ultimo_nome, self.__placas_carros)

    def adiciona_carro(self, placa_carro):
        self.__placas_carros.extend(placa_carro)


def cadastrar_proprietario(cpf, placa):
    primeir_nome = str(input('Primeiro nome do proprietário: ')).split(' ')[0]
    ultimo_nome = str(input('Último nome do proprietário: ')).split(' ')[0]

    return Proprietario(cpf, primeir_nome, ultimo_nome, placa)


def pega_carros_do_proprietario(proprietario):
    return ' '.join(proprietario.split('[')[1].split(']')[0].split(', ')).replace('\'', '').split(' ')


def adiciona_carro_a_proprietario(proprietarios, proprietario, placa):
    placas = pega_carros_do_proprietario(proprietario)
    placas.append(placa)
    placas.sort()
    proprietario_lista_elementos = proprietario.split(' ')
    proprietario_atualizado = '{} {} {} {}\n'.format(proprietario_lista_elementos[0],
                                                     proprietario_lista_elementos[1],
                                                     proprietario_lista_elementos[2],
                                                     placas)
    proprietarios[proprietarios.index(proprietario)] = proprietario_atualizado

    return proprietarios


def procura_proprietario():
    proprietarios = le_arquivo('Proprietários Cadastrados')
    carros = le_arquivo('Carros Cadastrados')

    cpf = str(input('CPF do Proprietário: ')).split(' ')[0]

    for proprietario in proprietarios:
        placas = pega_carros_do_proprietario(proprietario)
        proprietario = proprietario.__str__().split('\n')[0].split(' ')

        if cpf == proprietario[0]:
            visualiza_proprietario_carros(proprietario, carros, placas)
            return

    print('\nCPF não encontrado.\n')


def visualiza_proprietario_carros(proprietario, carros, placas):
    print('Proprietário(a)')
    print('CPF: {}\t\tNome: {}\t\tSobrenome: {}\n'.format(proprietario[0], proprietario[1], proprietario[2]))
    print('Carro(s)')

    for carro in carros:
        carro = carro.__str__().split('\n')[0].split(' ')
        placa_comparacao = carro[0]

        for placa in placas:
            if placa_comparacao == placa:
                print(
                    'Placa: {}\t\tMarca: {}\t\tModelo: {}\t\tAno: {}\n'.format(carro[0], carro[1], carro[2], carro[3]))

    print('\n')
