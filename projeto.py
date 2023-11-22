def excluir():
    f = open(".txt", "+r")
    lista = f.readline()
#Escolhendo o numero de livros a serem deletados
    print(f.read())
    print("-"*110)
    print("Ao escrever sair o programa encerrara".capitalize())
    while True:
        
        #Escolhendo o livro 
        livro = input("Qual o nome do livro :").upper()



        #Deletando o dicionario
        try :
            if lista.get(livro):
                lista.pop(livro)
                print("Livros excluidos com sucesso")
            if lista == () :
                print("Sua lista esta vazia")
                break
            elif livro == "sair" :
                break
        except FileNotFoundError:
            print("Esse livro nao esta na lista")
            break
        #Retornando a lista nova 
        f.close
    return lista