from datetime import datetime


class TaskNotFoundError(Exception):
    pass


class Task:
    def __init__(self, task_id: int, title: str, description: str):
        self.id = task_id
        self.title = title
        self.description = description
        self.is_completed = False
        self.created_at = datetime.now()

    def complete_task(self) -> None:
        self.is_completed = True

    def __str__(self) -> str:
        return f"ID: {self.id}, Название: {self.title}, Описание: {self.description}, Статус: {"Выполнено" if self.is_completed else "Не выполнено"}, Создано: {self.created_at}"


class TaskService:
    def __init__(self):
        self.storage: {int, Task} = {}
        self._next_id = 0

    def add_task(self, title: str, description: str) -> None:
        task = Task(self._next_id, title, description)
        self.storage[self._next_id] = task
        self._next_id += 1

    def get_task(self, task_id: int) -> Task | None:
        return self.storage.get(task_id)

    def get_list(self) -> list:
        return list(self.storage.values())

    def complete_task(self, task_id: int) -> None:
        task = self.storage.get(task_id)
        if not task:
            raise TaskNotFoundError
        task.complete_task()

    def delete_task(self, task_id: int) -> None:
        if not self.storage.get(task_id):
            raise TaskNotFoundError
        self.storage.pop(task_id, None) 
        

def main(tasks: TaskService):
    while True:
        print("\n")
        print("-- Cписок задач -- ")
        [print(task) for task in tasks.get_list()]
        print("\n1. Добавить задачу \n2. Пометить выполненую задачу \n3. Удалить задачу \n4. Выход")

        choice = input("> ").strip()

        if choice == "1":
            title = input("Напишите название задачи: ").strip()
            description = input("Напишите описание задачи: ").strip()
            tasks.add_task(title, description)
        elif choice == "2":
            task_id = int(input("Введите айди задачи: "))
            tasks.complete_task(task_id)
        elif choice == "3":
            task_id = int(input("Введите айди задачи: "))
            tasks.delete_task(task_id)
        elif choice == "4":
            break
        else:
            pass


if __name__ == "__main__":
    tasks = TaskService()
    main(tasks)