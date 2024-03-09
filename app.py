import os

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
    # MACOS
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls') # WINDOWS
    print('''
________________________________
          
Uso do aplicativo finalizado!
Obrigado pela preferência!
________________________________

          ''')

def escolher_opcao(): 

    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
        case 1: 
            print('\n__________________________________________')
            print('Cadastrar Restaurante')
        case 2: 
            print('\n__________________________________________')
            print('Listar Restaurantes')
        case 3: 
            print('\n__________________________________________')
            print('Ativar Restaurantes')
        case 4: 
            finalizar_app()
        case _: print('Opção inválida! Tente novamente!')

def main():
    nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()