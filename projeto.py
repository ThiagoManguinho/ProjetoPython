todoslivros = {'Livros': []}
livros_autores = {}
livros_categorias = {}

#ESTILIZANDO
print('-=' * 50)

print('CADASTRO DOS LIVROS')
qnt = int(input('Digite quantos livros deseja adicionar: '))
print()

for t in range(qnt):
    livro = input('Digite o nome do livro: ').title()
    #USOU-SE O {LIVRO} PARA CITAR O NOME DO LIVRO NO PRINT
    autor = input(f'Digite o nome do autor do livro {livro}: ').title()
    categoria = input(f'Digite qual a categoria do livro {livro}: ').title()
    valor = float(input(f'Digite o valor que {livro} foi adquirido: R$'))
    print()

    #ADICIONANDO À LISTA
    todoslivros['Livros'].append(livro)
    livros_autores[livro] = autor

    #VERIFICANDO SE A CATEGORIA EXISTE
    if categoria in livros_categorias:
        livros_categorias[categoria].append(livro)
    else:
        livros_categorias[categoria] = [livro]

print('-=' * 50)

print()
print(todoslivros)
print(livros_autores)
print(livros_categorias)
print()