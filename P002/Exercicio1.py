# Lista de tarefas
tarefas = []

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
    elif escolha == "3":
        marcar_como_realizada()
    elif escolha == "4":
        editar_tarefa()
    elif escolha == "5":
        remover_tarefa()
    elif escolha == "6":
        print("Encerrando o programa.")
        break
    else:
        print("Escolha inválida. Tente novamente.")
