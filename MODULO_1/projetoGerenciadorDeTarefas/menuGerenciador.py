def addTasks(tasks, taskName):
    task = {"taskName": taskName, "completed":False}
    tasks.append(task)
    print(f"A tarefa '{taskName}' foi adicionada com sucesso!")
    return

def viewTasks(tasks):
    print("\nLista de tarefas:")
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else " "
        taskName = task["taskName"]
        print(f"{index} | [ {status} ] - {taskName}")
    return

def updateTask(tasks, indexTask, updateNameTask):
    indexTaskAdjusted = int(indexTask) - 1
    if indexTaskAdjusted >= 0 and indexTaskAdjusted < len(tasks):
        tasks[indexTaskAdjusted]["taskName"] = updateNameTask
        print(f"Tarefa {indexTask} foi atualizada para {updateNameTask}")
    else:
        print("Opção inválida!")
    return

def completeTask(tasks, indexTask):
    indexTaskAdjusted = int(indexTask) - 1
    tasks[indexTaskAdjusted]["completed"] = True
    print(f"Tarefa {indexTask} concluída !")
    return

def deleteTask(tasks):
    for task in tasks:
        if task["completed"]: # "completed" = True
            tasks.remove(task)
    print("\nTarefas já completadas foram deletadas!")
    return

tasks = []

#MAIN MENU
while True: 
    print("\n#############################################")
    print("   MENU DO GERENCIADOR DE LISTA DE TAREFAS:  ")
    print("#############################################\n")
    print("1 - ADICIONAR TAREFA")
    print("2 - VER TAREFAS")
    print("3 - ATUALIZAR TAREFA")
    print("4 - COMPLETAR TAREFA")
    print("5 - DELETAR TAREFAS COMPLETADAS")
    print("6 - ENCERRAR GERENCIADOR DE TAREFAS")
    
    option = input("\nInsira a opção desejada: ")
    
    if option == "1":
        taskName = input("Digite o nome da tarefa: ")
        addTasks(tasks, taskName)
        
    elif option == "2":
        viewTasks(tasks)
        
    elif option == "3":
        viewTasks(tasks)
        indexTask = input("Qual tarefa deseja alterar? ")
        updateNameTask = input("Insira a alteração: ")
        updateTask(tasks, indexTask, updateNameTask)
        
    elif option == "4":
        viewTasks(tasks)
        indexTask = input("Qual tarefa deseja completar? ")
        completeTask(tasks, indexTask)
        
    elif option == "5":
        viewTasks(tasks)
        deleteTask(tasks)
        viewTasks(tasks)
    elif option == "6":
        break
    
print("\nPrograma encerrado !")