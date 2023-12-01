def inserir_produto(lista_produtos):
    codigo = input("Digite o código do produto (13 caracteres): ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    produto = {'codigo': codigo, 'nome': nome, 'preco': preco}
    lista_produtos.append(produto)
    print("Produto inserido com sucesso!")

def excluir_produto(lista_produtos):
    codigo = input("Digite o código do produto que deseja excluir: ")
    produtos_encontrados = [produto for produto in lista_produtos if produto['codigo'] == codigo]
    
    if produtos_encontrados:
        lista_produtos.remove(produtos_encontrados[0])
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")

