import os

# Lista de Restaurantes
restaurantes = ["Manu's Risottos", "Pizzaranria"]

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
3. Ativar restaurantes
4. Sair\n''')

def finalizar_app():
    print('''
________________________________
          
Uso do aplicativo finalizado!
Obrigado pela preferência!
________________________________

          ''')

def limpar_console():
    if os.name == 'posix':
        os.system('clear') # MACOS
    elif os.name == 'nt':
        os.system('cls') # WINDOWS

#endregion

#region Funcionamento
def voltar_ao_menu_principal():
    input('Digite uma tecla para retornar ao menu principal. ')
    main()

def cadastrar_novo_restaurante():
    limpar_console()
    exibir_subtitulo('1. Cadastrar restaurante')
    
    nome = input('\tDigite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'\tO restaurante \033[1m\033[92m{nome}\033[0m foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    limpar_console()
    exibir_subtitulo('2. Listar Restaurantes:')
    i=0
    for restaurante in restaurantes:
        i+=1
        print(f'\t[{i}] restaurante: \033[1m{restaurante}\033[0m')
    voltar_ao_menu_principal()

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
                print('Ativar Restaurantes')
            case 4: 
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