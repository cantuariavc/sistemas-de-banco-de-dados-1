from Arquivo import e_arquivo_vazio, le_arquivo, escreve_arquivo
from Proprietario import cadastrar_proprietario, adiciona_carro_a_proprietario


class Carro:
    def __init__(self, placa, marca, modelo, ano, cpf_proprietario):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cpf_proprietario = cpf_proprietario

    def __str__(self):
        return '{} {} {} {} {}\n'.format(self.__placa, self.__marca, self.__modelo, self.__ano,
                                         self.__cpf_proprietario)

    def get_cpf_proprietario(self):
        return self.__cpf_proprietario


def e_registro_existente(lista, pk):
    registro_existente = False

    if not e_arquivo_vazio():
        for item in lista:
            pk_comparacao = item.split(' ')[0]
            if pk_comparacao == pk:
                registro_existente = True
                break

    return registro_existente


def cadastrar_carro(placa):
    marca = str(input('Marca do carro: ')).split(' ')[0]
    modelo = str(input('Modelo do carro: ')).split(' ')[0]
    ano = str(input('Ano do carro: ')).split(' ')[0]
    cpf_proprietario = str(input('CPF do propietário: ')).split(' ')[0]

    return Carro(placa, marca, modelo, ano, cpf_proprietario)


def registra_carro():
    print('Registro do Carro')

    placa = str(input('Placa do carro: ')).split(' ')[0]
    carros = le_arquivo('Carros Cadastrados')
    carro_existente = e_registro_existente(carros, placa)

    if not carro_existente:
        novo_carro = cadastrar_carro(placa)
        carros.append(novo_carro.__str__())
        cpf_proprietario = novo_carro.get_cpf_proprietario()
        del novo_carro
        carros.sort()

        proprietarios = le_arquivo('Proprietários Cadastrados')
        proprietario_existente = e_registro_existente(proprietarios, cpf_proprietario)

        if not proprietario_existente:
            novo_proprietario = cadastrar_proprietario(cpf_proprietario, placa)
            proprietarios.append(novo_proprietario.__str__())
            del novo_proprietario
            proprietarios.sort()
        else:
            for proprietario in proprietarios:
                cpf_comparacao = proprietario.split(' ')[0]
                if cpf_comparacao == cpf_proprietario:
                    proprietarios = adiciona_carro_a_proprietario(proprietarios, proprietario, placa)
                    break

        escreve_arquivo('Carros Cadastrados', carros)
        escreve_arquivo('Proprietários Cadastrados', proprietarios)

        print('\nCarro cadastrado com sucesso.\n')
    else:
        print('\nPlaca já cadastrada.\n')


def procura_carro():
    carros = le_arquivo('Carros Cadastrados')
    proprietarios = le_arquivo('Proprietários Cadastrados')

    placa = str(input('Placa do carro: ')).split(' ')[0]

    for carro in carros:
        carro = carro.__str__().split('\n')[0].split(' ')
        placa_comparacao = carro[0]

        if placa_comparacao == placa:
            for proprietario in proprietarios:
                proprietario = proprietario.__str__().split('\n')[0].split(' ')

                if carro[4] == proprietario[0]:
                    print('Carro')
                    print('Placa: {}\t\tMarca: {}\t\tModelo: {}\t\tAno: {}\n'.format(carro[0], carro[1], carro[2], carro[3]))
                    print('Proprietário(a)')
                    print('CPF: {}\t\tNome: {}\t\tSobrenome: {}\n'.format(proprietario[0], proprietario[1], proprietario[2]))
                    return

    print('\nPlaca não encontrada.\n')
