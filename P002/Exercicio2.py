tarefas = []

# Função para carregar as tarefas do arquivo
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.strip().split(",")
                tarefa = {"descricao": partes[0], "feito": partes[1] == "True"}
                tarefas.append(tarefa)
    except FileNotFoundError:
        # Se o arquivo não existir, comece com uma lista vazia de tarefas
        tarefas = []

# Função para salvar as tarefas no arquivo
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            feito = "True" if tarefa["feito"] else "False"
            arquivo.write(f"{tarefa['descricao']},{feito}\n")

# No início do programa, carregue as tarefas do arquivo
carregar_tarefas()

# Função para listar as tarefas
def listar_tarefas():
    print("Lista de Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["feito"] else "[ ]"
        print(f"{idx}. {tarefa['descricao']} {status}")

# Função para registrar uma nova tarefa
def registrar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ").capitalize()
    nova_tarefa = {"descricao": descricao, "feito": False}
    tarefas.append(nova_tarefa)
    print("Tarefa registrada!!!")

# Função para marcar uma tarefa como realizada
def marcar_como_realizada():
    listar_tarefas()
    identificador = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
    if identificador <= len(tarefas):
        tarefas[identificador - 1]["feito"] = True
        tarefas.insert(0, tarefas.pop(identificador - 1))
        print("Tarefa marcada como realizada!")
    else:
        print("Identificador inválido ou tarefa já realizada.")

# Função para editar uma tarefa
def editar_tarefa():
    listar_tarefas()
    identificador = int(input("Digite o ID da tarefa a ser editada: "))
    if identificador <= len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[identificador - 1]["descricao"] = nova_descricao
        print("Tarefa editada!")
    else:
        print("Identificador inválido.")

def remover_tarefa():
    listar_tarefas()
    identificador = int(input("Digite o ID da tarefa a ser removida: "))
    if identificador <= len(tarefas):
        tarefas.pop(identificador - 1)
        print("Tarefa removida!")
    else:
        print("Identificador inválido.")

# Loop principal do programa
while True:
    print("\n### MENU ###")
    print("1. Listar tarefas")
    print("2. Registrar nova tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("5. Remover tarefa")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        listar_tarefas()
    elif escolha == "2":
        registrar_tarefa()
        salvar_tarefas()
    elif escolha == "3":
        marcar_como_realizada()
        salvar_tarefas()
    elif escolha == "4":
        editar_tarefa()
    elif escolha == "5":
        remover_tarefa()
        salvar_tarefas()
    elif escolha == "6":
        salvar_tarefas()
        print("Encerrando o programa.")
        break
    else:
        print("Escolha inválida. Tente novamente.")
