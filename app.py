import os

restaurantes = []

def nome_programa():
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''')

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

def cadastrar_novo_restaurante():
    limpar_console()
    print('__________________________________________')
    print('Cadastrar Restaurante\n')
    
    nome = input('Digite o nome do restaurante: ')
    restaurantes.append(nome)
    print(f'O restaurante {nome} foi cadastrado com sucesso!')
    print()
    input('Digite uma tecla para retornar ao menu principal. ')
    main()

def limpar_console():
    if os.name == 'posix':
        os.system('clear') # MACOS
    elif os.name == 'nt':
        os.system('cls') # WINDOWS

def opcao_invalida():
    limpar_console()
    print('Opção inválida! Tente novamente!')
    input('Digite uma tecla para retornar ao menu principal. ')
    main()

def escolher_opcao(): 
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2: 
                print('\n__________________________________________')
                print('Listar Restaurantes')
            case 3: 
                print('\n__________________________________________')
                print('Ativar Restaurantes')
            case 4: 
                finalizar_app()
            case _:
                opcao_invalida()
    except: 
        opcao_invalida()

def main():
    limpar_console()
    #nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()