# Criando o dicionário para armazenar os dados dos empregados
empregados = []

# Lendo as informações dos funcionários de um arquivo
def ler_arquivo():
    with open("funcionarios.txt", "r") as arquivo:  # Modo alterado para leitura "r"
        linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.strip().split(",")
        empregado = {
            "nome": dados[0],
            "sobrenome": dados[1],
            "ano_nascimento": int(dados[2]),
            "RG": dados[3],
            "ano_admissao": int(dados[4]),
            "salario": float(dados[5])
        }
        empregados.append(empregado)

def cadastrar_empregado():
    nome = input("Digite o nome do empregado: ")
    sobrenome = input("Digite o sobrenome do empregado: ")
    ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
    RG = input("Digite o RG do empregado: ")
    ano_admissao = int(input("Digite o ano de admissão do empregado: "))
    salario = float(input("Digite o salário do empregado: "))
    empregado = {
        "nome": nome,
        "sobrenome": sobrenome,
        "ano_nascimento": ano_nascimento,
        "RG": RG,
        "ano_admissao": ano_admissao,
        "salario": salario
    }
    empregados.append(empregado)

def salvar_arquivo():
    with open("funcionarios.txt", "w") as arquivo:
        for empregado in empregados:
            arquivo.write(f"{empregado['nome']},{empregado['sobrenome']},{empregado['ano_nascimento']},{empregado['RG']},{empregado['ano_admissao']},{empregado['salario']}\n")

def listar_empregados():
    for i, empregado in enumerate(empregados, start=1):
        print(f"{i}. {empregado['nome']} {empregado['sobrenome']}")

def reajusta_dez_porcento(empregados):  # Corrigido para 'reajusta_dez_porcento'
     for empregado in empregados:
         empregado['salario'] *= 1.1

def menu():
    print("1. Listar empregados")
    print("2. Reajustar salários")
    print("3. Salvar e sair")
    opcao = int(input("Digite a opção desejada: "))
    while opcao != 3:
        if opcao == 1:
            listar_empregados()
        elif opcao == 2:
            reajusta_dez_porcento(empregados)
        else:
            print("Opção inválida!")
        print("1. Listar empregados")
        print("2. Reajustar salários")
        print("3. Salvar e sair")
        opcao = int(input("Digite a opção desejada: "))
