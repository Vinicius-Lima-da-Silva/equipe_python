def inserir_produto(lista_produtos):
    codigo = input("Digite o código do produto (13 caracteres): ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    produto = {'codigo': codigo, 'nome': nome, 'preco': preco}
    lista_produtos.append(produto)
    print("Produto inserido com sucesso!")

