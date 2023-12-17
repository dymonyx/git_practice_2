tasks = []

def get_all_tasks():
    return tasks

def get_task(title):
    for task in tasks:
        if task["title"] == title:
            return task
    return None

def update_task_status(title, new_status):
    task = get_task(title)
    if task:
        task["status"] = new_status


action = input("Что вы хотите сделать? Создать, Посмотреть все таски, Изменить статус: ")
if action == "Посмотреть все таски":
  print(get_all_tasks)
else:
  update_task_status(input("Ввведите название: "), input("Введите новый статус: ")
