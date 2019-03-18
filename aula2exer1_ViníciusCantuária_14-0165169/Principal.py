# -*- coding: utf-8 -*-
from Servicos import menu, escolha


def main():
    opcao = 5
    while opcao != 0:
        opcao = menu(opcao)
        while opcao < 0 or opcao > 4:
            print('\nOpção inválida.\n')
            opcao = menu(opcao)

        escolha(opcao)


if __name__ == '__main__':
    main()
