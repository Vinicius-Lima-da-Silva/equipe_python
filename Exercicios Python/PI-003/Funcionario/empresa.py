import os


def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salário'] *= 1.1  


def ler_arquivo(nome_arquivo):
    lista_empregados = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')  
            empregado = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salário': float(dados[5])
            }
            lista_empregados.append(empregado)
    return lista_empregados


def exibir_empregados(lista_empregados):
    for empregado in lista_empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, "
              f"Ano de Nascimento: {empregado['ano_nascimento']}, "
              f"RG: {empregado['RG']}, "
              f"Ano de Admissão: {empregado['ano_admissao']}, "
              f"Salário: R${empregado['salário']:.2f}")


diretorio = r'C:\Users\Vini_\OneDrive\Área de Trabalho\equipe_python\Exercicios Python\PI-003\Funcionario'


arquivo_dados = 'dados_empregados.txt'


caminho_arquivo = os.path.join(diretorio, arquivo_dados)


if os.path.exists(caminho_arquivo):
    
    lista_empregados = ler_arquivo(caminho_arquivo)

    
    print("Empregados antes do reajuste:")
    exibir_empregados(lista_empregados)

    
    reajusta_dez_porcento(lista_empregados)

    
    print("\nEmpregados após o reajuste:")
    exibir_empregados(lista_empregados)
else:
    print(f"O arquivo {arquivo_dados} não foi encontrado no diretório especificado.")
