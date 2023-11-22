import os 
os.system('cls')

def salvar_para_arquivo():
    with open('livros.txt', 'w') as arquivo:
        for livro in livros:
            linha = f"{livro['nome']},{livro['autor']},{livro['categoria']},{livro['custo']}\n"
            arquivo.write(linha)

def carregar_do_arquivo():
    livros_carregados = []
    if os.path.exists('livros.txt'):
        with open('livros.txt', 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                livro = {
                    'nome': dados[0],
                    'autor': dados[1],
                    'categoria': dados[2],
                    'custo': float(dados[3])
                }
                livros_carregados.append(livro)
    return livros_carregados

os.system('cls')

livros = carregar_do_arquivo()

def visualizar_livros():
    if not livros:
        print('Nenhum livro cadastrado ainda.\n')
        return

    for livro in livros:
        print(f'Nome: {livro["nome"]}, Autor: {livro["autor"]}, Categoria: {livro["categoria"]}, Custo: R${livro["custo"]:.2f}')
    print()

def atualizar_livro():
    visualizar_livros()

    try:
        nome_livro = input('Digite o nome do livro que deseja atualizar: ')
        livro_encontrado = next((livro for livro in livros if livro["nome"] == nome_livro), None)

        if not livro_encontrado:
            print(f'Livro com o nome "{nome_livro}" não encontrado.\n')
            return

        print(f'Livro encontrado: Nome: {livro_encontrado["nome"]}, Autor: {livro_encontrado["autor"]}, Categoria: {livro_encontrado["categoria"]}, Custo: R${livro_encontrado["custo"]:.2f}')

        livro_encontrado["nome"] = input('Novo nome do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["autor"] = input('Novo autor do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["categoria"] = input('Nova categoria do livro (ou pressione Enter para manter a mesma): ')
        novo_custo = input('Novo custo do livro (ou pressione Enter para manter o mesmo): ')

        if novo_custo:
            livro_encontrado["custo"] = float(novo_custo)

        salvar_para_arquivo()  # Salva as alterações no arquivo após a atualização

        print('Livro atualizado com sucesso!\n')

    except Exception as e:
        print(f'Ocorreu um erro: {e}\n')

# Exemplo de uso
atualizar_livro()
Esta versão usa apenas as funções na