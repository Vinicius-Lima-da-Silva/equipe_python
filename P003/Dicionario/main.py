
# Criando o dicionário para armazenar os dados dos empregados
empregados = []

# Lendo as informações dos funcionários de um arquivo
with open("funcionarios.txt", "r") as arquivo:
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

def salvar_arquivo():
    with open("funcionarios.txt", "w") as arquivo:
        for empregado in empregados:
            arquivo.write(f"{empregado['nome']},{empregado['sobrenome']},{empregado['ano_nascimento']},{empregado['RG']},{empregado['ano_admissao']},{empregado['salario']}\n")

def listar_empregados():
    for i, empregado in enumerate(empregados, start=1):
        print(f"{i}. {empregado['nome']} {empregado['sobrenome']}")

def Reajusta_dez_porcento(empregados):
     for empregado in empregados:
         empregado['salario'] *= 1.1
