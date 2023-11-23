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