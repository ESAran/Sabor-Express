import os, time

# Lista de Restaurantes
restaurantes = [{'nome':"Manu's Risottos",'categoria':'Risotos', 'ativo':True},
                {'nome':"Pizzaranria",'categoria':'Pizzaria', 'ativo':True},
                {'nome':"Merdeiro",'categoria':'Hamburgueria', 'ativo':True}, 
                {'nome':"Slomphies",'categoria':'Smoothieria', 'ativo':False}]

#region GUI

def nome_programa():
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

def exibir_subtitulo(subtitulo):
    print('''              
▒█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ▒█▀▀▀ █░█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
░▀▀▀▄▄ █▄▄█ █▀▀▄ █░░█ █▄▄▀ 　 ▒█▀▀▀ ▄▀▄ █░░█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
▒█▄▄▄█ ▀░░▀ ▀▀▀░ ▀▀▀▀ ▀░▀▀ 　 ▒█▄▄▄ ▀░▀ █▀▀▀ ▀░▀▀ ▀▀▀ ▀▀▀ ▀▀▀
=============================================================
          ''')
    print(f'{subtitulo}\n')

def exibir_opcoes():
    print('''1. Cadastrar restaurante
2. Listar restaurantes
3. Alternar estado dos restaurantes
4. Remover restaurantes
5. Sair\n''')

def finalizar_app():
    limpar_console()
    exibir_subtitulo(f'''{cor_texto.BOLD}Uso do aplicativo finalizado!
Obrigado pela preferência!{cor_texto.END}
''')


def limpar_console():
    time.sleep(0.01)
    os.system('cls')
    time.sleep(0.01)

class cor_texto:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   GREY = '\033[90m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#endregion

#region Funcionamento
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para retornar ao menu principal. ')
    main()

def cadastrar_novo_restaurante():
    limpar_console()
    exibir_subtitulo('1. Cadastrar restaurante:')
    
    nome = input('\tDigite o nome do restaurante: ')
    categoria = input(f'\tDigite o nome da categoria do restaurante {cor_texto.BOLD}{nome}{cor_texto.END}: ')
    dados_restaurante = {'nome':nome,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\n\tO restaurante {cor_texto.BOLD}{cor_texto.GREEN}{nome}{cor_texto.END} foi cadastrado com sucesso!')
    print('\tCaso deseje ativa-lo, retorne ao menu principal e selecione a opção 03 ("Ativar restaurantes").')
    voltar_ao_menu_principal()

def listar_restaurantes():
    limpar_console()
    exibir_subtitulo('2. Listar restaurantes:')
    i=0
    for restaurante in restaurantes:
        i+=1
        print(f'\t[{i}] restaurante: \033[1m{restaurante['nome']}\033[0m')
        print(f'\t\tCategoria: {restaurante['categoria']}')
        if restaurante['ativo'] == True:
            print(f'\t\t{cor_texto.BLUE}Em funcionamento!{cor_texto.END}')
        else:
            print(f'\t\t{cor_texto.GREY}Desativado{cor_texto.END}')
        print('')
        
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    limpar_console()
    exibir_subtitulo('3. Alternar estado dos restaurantes:')
    nome = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {cor_texto.BOLD}{nome}{cor_texto.END} foi {cor_texto.BOLD}{cor_texto.BLUE}ativado{cor_texto.END} com sucesso!' if restaurante['ativo'] else f'O restaurante {cor_texto.BOLD}{nome}{cor_texto.END} foi {cor_texto.BOLD}{cor_texto.GREY}desativado{cor_texto.END} com sucesso!'

    if not restaurante_encontrado:
        print('\n\tRestaurante não encontrado!')
        print('\nDigite 3 para tentar novamente. ')
        escolha = str(input('Digite qualquer tecla para voltar ao menu principal. '))
        if escolha == '3':
            alternar_estado_restaurante()
        else:  main()

    print(mensagem)
    voltar_ao_menu_principal()

def remover_restaurantes():
    limpar_console()
    exibir_subtitulo('4. Remover restaurantes:')
    nome = input('Digite o nome do restaurante que deseja remover: ')
    restaurante_encontrado = False
    restaurante_ativo = False
    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            if restaurante['ativo'] == True:
                restaurante_ativo = True
            else:
                restaurantes.remove(restaurante)
                print(f'O restaurante {cor_texto.BOLD}{nome}{cor_texto.END} foi {cor_texto.BOLD}{cor_texto.RED}removido{cor_texto.END} com sucesso!')

    if not restaurante_encontrado:
        print('\n\tRestaurante não encontrado!')
        print('\nDigite 4 para tentar novamente. ')
        escolha = str(input('Digite qualquer tecla para voltar ao menu principal. '))
        if escolha == '4':
            remover_restaurantes()
        else: main()
    elif restaurante_ativo == True:
            print('\n\tRestaurante ainda está ativo!')
            print('\nDigite 3 para ir à alteração de estado. ')
            escolha = str(input('Digite qualquer tecla para voltar ao menu principal. '))
            if escolha == '3':
                alternar_estado_restaurante()
            else: main()
    else: voltar_ao_menu_principal()

def opcao_invalida():
    limpar_console()
    exibir_subtitulo('Opção inválida! Tente novamente!')
    voltar_ao_menu_principal()

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2: 
                listar_restaurantes()
            case 3: 
                alternar_estado_restaurante()
            case 4:
                remover_restaurantes()
            case 5: 
                finalizar_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

#endregion
        
def main():
    limpar_console()
    nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()