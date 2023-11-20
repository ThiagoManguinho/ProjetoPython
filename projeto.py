import os 
os.system('cls')

livros = []  # Lista vazia para armazenar informações sobre os livros

def visualizar_livros():
    if not livros:
        print('Nenhum livro cadastrado ainda.\n')
        return

    for livro in livros:
        print(f'ID: {livro["id"]}, Nome: {livro["nome"]}, Autor: {livro["autor"]}, Categoria: {livro["categoria"]}, Custo: R${livro["custo"]:.2f}')
    print()

def atualizar_livro():
    visualizar_livros()  # Chama a função para exibir os livros antes de atualizar

    try:
        livro_id = int(input('Digite o ID do livro que deseja atualizar:'))  # Solicita o ID do livro que o usuário deseja atualizar
        livro_encontrado = next((livro for livro in livros if livro["id"] == livro_id), None)  # Encontra o livro com o ID fornecido

        if not livro_encontrado:
            print(f'Livro com ID {livro_id} não encontrado.\n')  # Se o livro não for encontrado, exibe uma mensagem
            return

        # Exibe informações sobre o livro encontrado
        print(f'Livro encontrado: ID: {livro_encontrado["id"]}, Nome: {livro_encontrado["nome"]}, Autor: {livro_encontrado["autor"]}, Categoria: {livro_encontrado["categoria"]}, Custo: R${livro_encontrado["custo"]:.2f}')

        # Solicita ao usuário novas informações sobre o livro
        livro_encontrado["nome"] = input('Novo nome do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["autor"] = input('Novo autor do livro (ou pressione Enter para manter o mesmo): ')
        livro_encontrado["categoria"] = input('Nova categoria do livro (ou pressione Enter para manter a mesma): ')
        novo_custo = input('Novo custo do livro (ou pressione Enter para manter o mesmo): ')

        # Atualiza o custo apenas se o usuário fornecer um novo custo
        if novo_custo:
            livro_encontrado["custo"] = float(novo_custo)

        print('Livro atualizado com sucesso!\n')  # Exibe uma mensagem de sucesso após a atualização

    except ValueError:
        print('Por favor, insira um ID válido (número inteiro).\n')  # Lida com exceção se o usuário inserir um valor não inteiro para o ID
    except Exception as e:
        print(f'Ocorreu um erro: {e}\n')  # Lida com outras exceções e exibe uma mensagem de erro

# Exemplo de uso
atualizar_livro()  # Chama a função para atualizar um livro
