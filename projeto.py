import os
os.system('cls')

todoslivros = {'Livros': []}
livros_autores = {}
livros_categorias = {}
valor_gasto = 0

#ESTILIZANDO
print('-=' * 50)

print('CADASTRO DOS LIVROS')
qnt = int(input('Digite quantos livros deseja adicionar: '))
print()

for t in range(qnt):
    livro = input('Digite o nome do livro: ').upper()
    #USOU-SE O {LIVRO} PARA CITAR O NOME DO LIVRO NO PRINT
    autor = input(f'Digite o nome do autor do livro {livro}: ').upper()
    categoria = input(f'Digite qual a categoria do livro {livro}: ').upper()
    valor = float(input(f'Digite o valor que {livro} foi adquirido: R$'))
    print()

    #ADICIONANDO À LISTA
    todoslivros['Livros'].append(livro)
    livros_autores[autor] = livro

    #VERIFICANDO SE A CATEGORIA EXISTE
    if categoria in livros_categorias:
        livros_categorias[categoria].append(livro)
    else:
        livros_categorias[categoria] = [livro]

    #CALCULANDO O VALOR GASTO
    valor_gasto+=valor

print('-=' * 50)

print()
print('Os livros presentes na Biblioteca são: ',todoslivros)
print('Os livros separados por autor são: ',livros_autores)
print('Os livros separados pro categoria: ',livros_categorias)
print()
print(f'O valor total gasto foi de: R$ {valor_gasto}')