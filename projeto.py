import time
import os
os.system('cls')

#ARQUIVIO

#verifica se o arquivo existe
def testeExiste(nome):
    try:
        #abre o arquivo em modo de leitura ('rt')
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        #retorna falso se o arquivo não existe
        return False 
    else:
        #retorna verdadeiro se o arquivo existe
        return True

#cria um arquivo novo se não existir
def criarArquivo(nome):
    try:
        #abre o arquivo em modo de escrita ('wt+')
        a = open(nome, 'wt+', encoding='utf-8')
        a.close()
    except:
        #menssagem de erro se tiver problema na abertura do arquivo
        print('Teve erro na criação do arquivo')
    else:
        #menssagem quando abre a arquivo com sucesso
        print(f'Arquivo {nome} criado com sucesso')

#ler arquivo e exibir os livros cadastrados
def lerArquivo(nome):
    try:
        #abre o arquivo em modo de leitura ('rt')
        a = open(nome, 'rt', encoding='utf-8')
    except:
        #menssagem se tiver algum erro ao abrir o arquivo
        print('Erro ao ler o arquivo')
    else:
        #cabeçalho para a lista de livros
        cabecalho('Livros Cadastrados')
        print('Ordem informações: Livro - Autor - Categoria - Nível\n')
        #separa os dados da linha do arquivo
        for linha in a:
            dado = linha.split(' - ')
            #remove a quebra de linha
            dado[1] = dado[1].replace('\n','')
            #printa os Livros e suas características
            print(f'{dado[0]}\t\t{dado[1]}\t\t{dado[2]}\t\t{dado[3]}')
    finally:
        #fecha o arquivo
        a.close()

#passar a informação do livro para o arquivo
def cadastrar(nome, autor, categoria, nivel):
    try:
         #abre o arquivo em modo de anexo ('at')
        a = open(teste, 'at', encoding='utf-8')
    except:
        #menssagem de erro se tiver problema ao abrir o arquivo
        print('ERRO na abertura do arquivo')
    else:
        try:
            #escreve os dados do novo livro no arquivo
            a.write(f'{nome} - {autor} - {categoria} - {nivel}\n')
        except:
            #menssagem de erro se tiver problema ao enviar o livro
            print('ERRO ao passar os dados do livro')
        else:
            #menssagem avisando que o livro foi cadastrado
            print(f'O livro {nome} foi cadastrado\n')
            a.close()

#nome do arquivo utilizado
teste = 'teste.txt'

#verifica se o arquivo existe caso contrario cria um novo
if not testeExiste(teste):
    criarArquivo(teste)


#INTERFACE

while True:
    #função para ler um número inteiro digitado pelo usuário
    def leiaInt(msg):
        while True:
            try:
                n = int(input(msg))
            #TypeErro = deve ser int e não str
            except (ValueError, TypeError):
                print('ERRO: por favor, digite um número válido \n')
                continue
            else:
                return n

    #função cria uma linha para separar 
    def linha(tam=80):
        return '-' * tam

    #função para exibir um cabeçalho
    def cabecalho(txt):
        print(linha())
        print(txt.center(80))
        print(linha())

    #função para exibir o menu e receber a decisão do usuário
    def menu(lista):
        cabecalho('Menu Principal')
        c = 1
        for item in lista:
            print(f'{c} - {item}')
            c += 1
        print(linha())
        opc = leiaInt('Sua Opção: ')
        return opc

    #exibe o menu de possibilidades e executa a opção escolhida
    resposta = menu(['Ver Biblioteca', 'Adicionar Livro','Editar Livro','Excluir Livro', 'Sair'])

    if resposta == 1:
        #opção de listar o conteúdo de um arquivo
        lerArquivo(teste)

    elif resposta == 2:
        #cadastrar o livro
        cabecalho('Livro Novo')
        nome = str(input('Digite o nome do livro: ')).title()
        autor = str(input(f'Digite o nome do autor livro {nome}: ')).title()
        print('\nRomance\nFicção científica\nFantasia\nTerror\nMistério\nSuspense\nDrama\nComédia\nPoesia\nBiografia\nHistória\nAção\nDocumentário')
        categoria = str(input(f'Digite qual a categoria do {nome}: ')).title()
        print('\nNível de leitura:\nFácil\nMédio\nDifícil')
        nivel = str(input('Qual o nível de leitura do livro: ')).title()

        cadastrar(nome, autor, categoria, nivel)


    elif resposta == 3:
        #editando as caracteristicas do livro
        def editarLivro(nome, livro):
            try:
                #abre o arquivo em modo de leitura para obter os dados
                with open(nome, 'r', encoding='utf-8') as arquivo:
                    #lê todas as linhas do arquivo
                    linhas = arquivo.readlines()
                #variável para verificar se o livro foi encontrado
                encontrado = False
                #abre o arquivo em modo de escrita para realizar a edição
                with open(nome, 'w', encoding='utf-8') as arquivo:
                    #percorre todas as linhas do arquivo
                    for linha in linhas:
                        #divide a linha em dados separados pelo separador ' - '
                        dados = linha.split(' - ')
                        #verifica se o título do livro atual é igual ao título fornecido para edição
                        if dados[0] == livro:
                            #marca como encontrado
                            encontrado = True
                            #solicita novas informações para edição
                            novo_autor = input(f'Digite o novo autor para o livro {livro}: ').title()
                            nova_categoria = input(f'Digite a nova categoria para o livro {livro}: ').title()
                            novo_nivel = input(f'Digite o novo nível para o livro {livro}: ').title()
                            #atualiza a linha com as novas informações
                            linha = f'{livro} - {novo_autor} - {nova_categoria} - {novo_nivel}\n'
                            print(f'O livro "{livro}" foi editado com sucesso.')
                        #escreve a linha no arquivo
                        arquivo.write(linha)  
                    
                    # Se o livro não foi encontrado, exibe uma mensagem
                    if not encontrado:
                        print(f'O livro "{livro}" não foi encontrado na biblioteca.')
            except FileNotFoundError:
                print('Arquivo não encontrado.')
            except Exception as e:
                print(f'Ocorreu um erro: {str(e)}')

        #livro a ser editado
        print(linha())
        livro_editado = input('Digite o título do livro que deseja editar: ').title()
        #chama a função para editar o livro na biblioteca
        editarLivro(teste, livro_editado)
            

    elif resposta == 4:
        def excluir(nome, livro):
            try:
                #abre o arquivo em modo de leitura para obter os dados
                with open(nome, "r", encoding='utf-8') as f:
                    # Lê todas as linhas do arquivo
                    linhas = f.readlines()

                with open(nome, 'w', encoding='utf-8') as f:
                    #percorre todas as linhas do arquivo
                    for lin in linhas:
                        # Divide a linha em dados separados pelo separador ' - '
                        livre = lin.split(' - ')
                        # Verifica se o título do livro atual é igual ao título fornecido para remoção
                        if livre[0]!=livro:
                            # Escreve a linha no arquivo
                            f.write(lin)
                    print(f'O {livro} foi removido\n')
                    f.close
            except FileNotFoundError:
                print('Arquivo não encontrado.')

        print(linha())
        livro = str(input("Qual o nome do livro: ").title())
        excluir(teste, livro)
    

    elif resposta == 5:
        #sair do Loop
        cabecalho('Saindo')
        break

    else:
        #digitou um número maior que as opições
        print('Digite um número com que tenha uma função\n')
        time.sleep(2)