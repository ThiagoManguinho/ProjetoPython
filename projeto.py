def execluir():
    n = int(input("Quantos livros voce quer deletar :"))
    for i in range(n):
        livro = input("Qual o nome do livro :").lower()
        if lista.get(livro):
            lista.pop(livro)
        else :
            print("Esse livro não esta na lista")
    return lista 
