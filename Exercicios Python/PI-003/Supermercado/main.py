from Supermercado import adicionar_produto, remover_produto, listar_produtos, consultar_preco
import os

def menu():
    print("Supermercado - Menu de Opções:")
    print("1. Inserir um novo produto")
    print("2. Excluir um produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar o preço de um produto")
    print("0. Sair")

def main():
    lista_produtos = []

    while True:
        os.system("cls||clear")
        menu()
        opcao = input("Digite a opção desejada: ")

        match(opcao):
            case "1":
                adicionar_produto(lista_produtos)
            case "2":
                os.system("cls||clear")
                codigo = input("Digite o código do produto a ser excluído: ")
                remover_produto(lista_produtos, codigo)
            case "3":
                listar_produtos(lista_produtos)
            case "4":
                os.system("cls||clear")
                codigo = input("Digite o código do produto para consultar o preço: ")
                consultar_preco(lista_produtos, codigo)
            case "0":
                os.system("cls||clear")
                print("Saindo do programa. Até mais!")
                break
            case _:
                os.system("cls||clear")
                print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
