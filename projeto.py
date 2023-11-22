#ler arquivo e exibir os livros cadastrados
def lerArquivo(nome):
    try:
        #abre o arquivo em modo de leitura ('rt')
        a = open(nome, 'rt', encoding='utf-8')
    except:
        #menssagem se tiver algum erro ao abrir o arquivo
        print('Erro ao ler o arquivo')