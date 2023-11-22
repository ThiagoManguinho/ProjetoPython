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