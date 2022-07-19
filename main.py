from colorama import init, Fore
import rotinas as fun
from time import sleep
init()

fun.bem_vindo()

while True:
    resposta = fun.menu(['Ver Cadastros', 'Novo Cadastro', 'Sair'])
    if resposta == 1:
        cadastro = open('cadastros.txt', 'r')
        fun.cabeçalho('Cadastros')
        sleep(1)
        print(cadastro.read())
    elif resposta == 2:
        cadastro = open('cadastros.txt', 'a')
        fun.cabeçalho('Novo Cadastro')
        nome = str(input('Nome: ')).strip()
        telefone = fun.leiaInt('Telefone com DDD (sem símbolos): ')
        info = f'{nome}\t\t\t{telefone}\n'
        cadastro.write(info)
        print(f'Novo registro de {nome} adicionado.')
        sleep(0.5)
    elif resposta == 3:
        fun.cabeçalho('Saindo... Até logo!')
        break
    else:
        print('\033[1;31mERRO: por favor, digite uma opção válida.\033[m')
    sleep(2)