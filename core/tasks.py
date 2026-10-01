def add_task(tasks: list, title: str, description: str = None) :
    tasks.append([title, description, False])


def list_tasks(tasks):
    return tasks


def complete_task(tasks, task_id):
    tasks[task_id][2] = True 


def delete_task(tasks, task_id):
    del tasks[task_id]


def main(tasks):
    while True:
        print("\n")
        print("-- Cписок задач -- ")
        [print(f"Задача {id}: Название: {task[0]}, Описание: {task[1]}, Статус: {"Выполнено" if task[2] else "Не выполнено"}") for id, task in enumerate(tasks)]
        print("\n1. Добавить задачу \n2. Пометить выполненую задачу \n3. Удалить задачу \n4. Выход")

        choice = input("> ").strip()

        if choice == "1":
            title = input("Напишите название задачи: ").strip()
            description = input("Напишите описание задачи: ").strip()
            add_task(tasks, title, description)
        elif choice == "2":
            task_id = int(input("Введите айди задачи: "))
            complete_task(tasks, task_id)
        elif choice == "3":
            task_id = int(input("Введите айди задачи: "))
            delete_task(tasks, task_id)
        elif choice == "4":
            print("Завершено")
            break
        else:
            pass


if __name__ == "__main__":
    tasks = []
    main(tasks)