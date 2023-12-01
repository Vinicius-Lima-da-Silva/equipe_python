# Função para inserir um novo produto
def inserir_produto(lista_produtos):
    codigo = input("Digite o código do produto (13 caracteres): ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    produto = {'codigo': codigo, 'nome': nome, 'preco': preco}
    lista_produtos.append(produto)
    print("Produto inserido com sucesso!")

# Função para excluir um produto cadastrado
def excluir_produto(lista_produtos):
    codigo = input("Digite o código do produto que deseja excluir: ")
    for produto in lista_produtos:
        if produto['codigo'] == codigo:
            lista_produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")

# Função para listar todos os produtos com seus respectivos códigos e preços
def listar_produtos(lista_produtos):
    for i, produto in enumerate(lista_produtos, start=1):
        print(f"{i}. Código: {produto['codigo']} - Nome: {produto['nome']} - Preço: R${produto['preco']:.2f}")

# Função para consultar o preço de um produto através de seu código
def consultar_preco(lista_produtos):
    codigo = input("Digite o código do produto que deseja consultar o preço: ")
    for produto in lista_produtos:
        if produto['codigo'] == codigo:
            print(f"O preço do produto '{produto['nome']}' é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")

# Função principal
def main():
    lista_produtos = []
    
    while True:
        print("\n===== MENU =====")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            inserir_produto(lista_produtos)
        elif opcao == '2':
            excluir_produto(lista_produtos)
        elif opcao == '3':
            listar_produtos(lista_produtos)
        elif opcao == '4':
            consultar_preco(lista_produtos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
