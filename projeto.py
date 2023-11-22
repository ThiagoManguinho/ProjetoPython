import os 
os.system('cls')

livros = []  # Lista vazia para armazenar informações sobre os livros

def visualizar_livros():
    if not livros:
        print('Nenhum livro cadastrado ainda.\n')
        return

    for livro in livros:
        print(f'Nome: {livro["nome"]}, Autor: {livro["autor"]}, Categoria: {livro["categoria"]}, Custo: R${livro["custo"]:.2f}')
    print()

def atualizar_livro():
    visualizar_livros()  # Chama a função para exibir os livros antes de atualizar

    try:
        nome_livro = input('Digite o nome do livro que deseja atualizar: ')  # Solicita o nome do livro que o usuário deseja atualizar
        livro_encontrado = next((livro for livro in livros if livro["nome"] == nome_livro), None)  # Encontra o livro com o nome fornecido

        if not livro_encontrado:
            print(f'Livro com o nome "{nome_livro}" não encontrado.\n')  # Se o livro não for encontrado, exibe uma mensagem
            return

        # Exibe informações sobre o livro encontrado
        print(f'Livro encontrado: Nome: {livro_encontrado["nome"]}, Autor: {livro_encontrado["autor"]}, Categoria: {livro_encontrado["categoria"]}, Custo: R${livro_encontrado["custo"]:.2f}')

        # Solicita ao usuário novas informações sobre o livro
        livro_encontrado["nome"] = input('Novo nome do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["autor"] = input('Novo autor do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["categoria"] = input('Nova categoria do livro (ou pressione Enter para manter a mesma): ')
        novo_custo = input('Novo custo do livro (ou pressione Enter para manter o mesmo): ')

        # Atualiza o custo apenas se o usuário fornecer um novo custo
        if novo_custo:
            livro_encontrado["custo"] = float(novo_custo)

        print('Livro atualizado com sucesso!\n')  # Exibe uma mensagem de sucesso após a atualização

    except Exception as e:
        print(f'Ocorreu um erro: {e}\n')  # Lida com exceções e exibe uma mensagem de erro

# Exemplo de uso
atualizar_livro()  # Chama a função para atualizar um livro