import os
os.system('cls')

livros = []

def cadastrar_livro():
    try:
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        categoria = input("Digite a categoria do livro: ")
        valor = float(input("Digite o valor gasto para adquiri-lo: "))

        livro = {
            'nome': nome,
            'autor': autor,
            'categoria': categoria,
            'valor': valor
        }

        livros.append(livro)
        print("Livro cadastrado com sucesso!")
    except ValueError:
        print("Erro: Valor inválido. Certifique-se de inserir um número para o valor do livro.")

def visualizar_livros():
    if not livros:
        print("A biblioteca está vazia.")
        return

    for i, livro in enumerate(livros, 1):
        print(f"ID: {i}, Nome: {livro['nome']}, Autor: {livro['autor']}, Categoria: {livro['categoria']}, Valor: R${livro['valor']:.2f}")

def atualizar_livro():
    if not livros:
        print("A biblioteca está vazia. Não há livros para atualizar.")
        return

    visualizar_livros()

    try:
        livro_id = int(input("Digite o ID do livro que deseja atualizar: ")) - 1  # Ajuste para a indexação de 0

        if 0 <= livro_id < len(livros):
            novo_nome = input("Digite o novo nome do livro (ou pressione Enter para manter o mesmo): ")
            novo_autor = input("Digite o novo autor do livro (ou pressione Enter para manter o mesmo): ")
            nova_categoria = input("Digite a nova categoria do livro (ou pressione Enter para manter a mesma): ")
            novo_valor = float(input("Digite o novo valor do livro (ou pressione Enter para manter o mesmo): "))

            livros[livro_id]['nome'] = novo_nome if novo_nome else livros[livro_id]['nome']
            livros[livro_id]['autor'] = novo_autor if novo_autor else livros[livro_id]['autor']
            livros[livro_id]['categoria'] = nova_categoria if nova_categoria else livros[livro_id]['categoria']
            livros[livro_id]['valor'] = novo_valor if novo_valor else livros[livro_id]['valor']

            print("Livro atualizado com sucesso!")
        else:
            print("Livro não encontrado.")
    except ValueError:
        print("Erro: Valor inválido. Certifique-se de inserir um número para o ID do livro ou valor do livro.")

def excluir_livro():
    if not livros:
        print("A biblioteca está vazia. Não há livros para excluir.")
        return

    visualizar_livros()

    try:
        livro_id = int(input("Digite o ID do livro que deseja excluir: ")) - 1  # Ajuste para a indexação de 0

        if 0 <= livro_id < len(livros):
            del livros[livro_id]
            print("Livro excluído com sucesso!")
        else:
            print("Livro não encontrado.")
    except ValueError:
        print("Erro: Valor inválido. Certifique-se de inserir um número para o ID do livro.")

def livros_por_categoria():
    if not livros:
        print("A biblioteca está vazia. Não há livros para exibir por categoria.")
        return

    categorias = set(livro['categoria'] for livro in livros)

    for categoria in categorias:
        print(f"\nCategoria: {categoria}")
        for i, livro in enumerate(livros, 1):
            if livro['categoria'] == categoria:
                print(f"ID: {i}, Nome: {livro['nome']}, Autor: {livro['autor']}, Valor: R${livro['valor']:.2f}")

def extrato_por_categoria():
    if not livros:
        print("A biblioteca está vazia. Não há livros para gerar um extrato por categoria.")
        return

    extrato = {}

    for livro in livros:
        categoria = livro['categoria']
        if categoria in extrato:
            extrato[categoria] += livro['valor']
        else:
            extrato[categoria] = livro['valor']

    for categoria, total in extrato.items():
        print(f"Categoria: {categoria}, Total Gasto: R${total:.2f}")

def total_gastos():
    if not livros:
        print("A biblioteca está vazia. Não há gastos para calcular.")
        return

    total = sum(livro['valor'] for livro in livros)
    print(f"Total de dinheiro gasto em livros: R${total:.2f}")

# Menu interativo
while True:
    print("\n===== Menu =====")
    print("1. Cadastrar Livro")
    print("2. Visualizar Livros")
    print("3. Atualizar Livro")
    print("4. Excluir Livro")
    print("5. Livros por Categoria")
    print("6. Extrato por Categoria")
    print("7. Total de Gastos")
    print("8. Sair")

    opcao = input("Digite o número da opção desejada: ")

    try:
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            visualizar_livros()
        elif opcao == '3':
            atualizar_livro()
        elif opcao == '4':
            excluir_livro()
        elif opcao == '5':
            livros_por_categoria()
        elif opcao == '6':
            extrato_por_categoria()
        elif opcao == '7':
            total_gastos()
        elif opcao == '8':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
