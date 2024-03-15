# Sabor Express

O seguinte repositório faz parte do curso **Python: crie sua primeira aplicação** da [Alura](alura.com.br).

Data de conclusão: 15/03/2024

Carga horária: **8h**

* Crie um projeto em Python usando o VSCode
* Descubra o fluxo de uma aplicação com o uso de condicionais e laços de repetição
* Aprenda a utilizar blocos de controle de execução try-except
* Crie funções para mostrar o menu principal e registrar restaurantes em listas e dicionários

link do curso: [Python: crie a sua primeira aplicação](https://cursos.alura.com.br/course/python-crie-sua-primeira-aplicacao "Curso Alura")

![Static Badge](https://img.shields.io/badge/Git_e_GitHub-grey?logo=github) ![Static Badge](https://img.shields.io/badge/Python-blue?logo=python&logoColor=yellow)

---

## Aplicativo

O aplicativo criado foi uma ideia simples de aplicativo de cadastro chamado **"Sabor Express"**, para aprender as funções de Python através do cadastramento, listagem, alternação de estado e remoção de um dicionário. Visto formatação de strings, manipulação de interface via terminal e noções básicas de sintaxe e estruturas.

Este desenvolvimento tem como objetivo servir de base apara aprendizagem visando posteriormente migrar para uma estrutura de Python OO (Orientado à objetos).

![menu](image/README/menu.png)

### Funcionamento

Faz os cadastro, listagem, alternação estados e remoção dos restaurantes através de funções dedicadas, mostrando via terminal com estilização.

Possui um dicionário com as informações dos restaurantes.

```python
# Lista de Restaurantes
restaurantes = [{'nome':"Manu's Risottos",'categoria':'Risotos', 'ativo':True},
                {'nome':"Pizzaranria",'categoria':'Pizzaria', 'ativo':True},
                {'nome':"Merdeiro",'categoria':'Hamburgueria', 'ativo':True}, 
                {'nome':"Slomphies",'categoria':'Smoothieria', 'ativo':False}]
```

Lista as opções em um menu e realiza a função respectiva de cada uma.

```python
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

```

#### Cadastrar restaurante

Cadastra o restaurante dentro do dicionário.

```python
def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante 
  
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes'''
    limpar_console()
    exibir_subtitulo('1. Cadastrar restaurante:')
  
    nome = input('\tDigite o nome do restaurante: ')
    categoria = input(f'\tDigite o nome da categoria do restaurante {cor_texto.BOLD}{nome}{cor_texto.END}: ')
    dados_restaurante = {'nome':nome,'categoria':categoria,'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\n\tO restaurante {cor_texto.BOLD}{cor_texto.GREEN}{nome}{cor_texto.END} foi cadastrado com sucesso!')
    print('\tCaso deseje ativa-lo, retorne ao menu principal e selecione a opção 03 ("Ativar restaurantes").')
    voltar_ao_menu_principal()
```

![Cadastramento](image/README/cadastramento.gif)

#### Listar restaurantes

Lista os restaurantes existentes com sua categoria e seu estado (Em funcionamento ou Desativado).

```python
def listar_restaurantes():
    '''Lista os restaurantes presentes na lista 
  
    Outputs:
    - Exibe a lista de restaurantes na tela'''
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

```

![Listar](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/eduardo_aran/OneDrive%20-%20Sicredi/Documents/Estudos/Python/Sabor-Express/image/README/listar.gif)

#### Alternar estados dos restaurantes

Altera o dicionário invertendo o estado de um restaurante (De desativado para ativo).


![Alternar](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/eduardo_aran/OneDrive%20-%20Sicredi/Documents/Estudos/Python/Sabor-Express/image/README/alternar.gif)

#### Remover restaurante

Remove um restaurante caso ele esteja desativado.

![Remover](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/eduardo_aran/OneDrive%20-%20Sicredi/Documents/Estudos/Python/Sabor-Express/image/README/remover.gif)
