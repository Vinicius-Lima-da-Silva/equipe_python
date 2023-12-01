import os

def adicionar_produto(lista_produtos):
    os.system("cls||clear")
    codigo = input("Digite o código do produto: ")
    nome_produto = input("Digite o nome do produto: ").capitalize()
    while True:
        try:
            preco_produto = float(input("Digite o preço do produto: "))
        except ValueError:
            print("Valor digitado inválido!")
        except Exception as e:
            print("Erro: ", e)
        else:
            break
    
    produto = {
        "codigo": codigo,
        "nome": nome_produto,
        "preco": round(preco_produto, 2)
    }

    lista_produtos.append(produto)
    print("Produto inserido com sucesso!\n")
    os.system("pause")
    

def remover_produto(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            lista_produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
            os.system("pause")
            return

    print("Produto não encontrado!\n")
    os.system("pause")


def listar_produtos(lista_produtos):
    os.system("cls||clear")
    if not lista_produtos:
        print("Nenhum produto cadastrado.\n")
        os.system("pause")
        return

    produtos_ordenados = sorted(lista_produtos, key=lambda x: x["codigo"])
    
    paginas = [produtos_ordenados[i:i+10] for i in range(0, len(produtos_ordenados), 10)]
    
    print("Lista de produtos:")
    for i, pagina in enumerate(paginas, start=1):
        print(f"\n === Página {i} === ")
        for produto in pagina:
            print(f"# {produto['codigo']} - {produto['nome']} \tR${produto['preco']:.2f}")

    print()
    os.system("pause")


def consultar_preco(lista_produtos, codigo):
    for produto in lista_produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}\n")
            os.system("pause")
            return

    print("Produto não encontrado!\n")
    os.system("pause")
