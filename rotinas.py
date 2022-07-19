from colorama import init, Fore
from time import sleep
init()


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mDigitação interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tam=26):
    return '-' * tam


def cabeçalho(txt=''):
    print(linha())
    print(txt.center(26))
    print(linha() + Fore.RESET)


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc


def bem_vindo():
    user = dict()
    print('Olá, seja bem vindo! Sou IDA, sua assistente virtual de cadastramento.')
    user['nome'] = str(input('Como posso te chamar? '))
    user['idade'] = leiaInt(f'Prazer em te conhecer, {user["nome"]}! Qual a sua idade? ')
    usuario = open('usuario.txt', 'a')
    usuario.write(f'{user}\n')
