def execluir():
#Escolhendo o numero de livros a serem deletados
    n = int(input("Quantos livros voce quer deletar :"))
    for i in range(n):

        #Escolhendo o livro 
        livro = input("Qual o nome do livro :").lower()

        #Deletando o dicionario
        if lista.get(livro):
            lista.pop(livro)
            if lista == {} :
                print("Sua lista esta vazia")
        else :
            print("Esse livro não esta na lista")
        #Retornando a lista nova 
    return lista 
