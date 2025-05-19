# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():

    # Инициация. Создаем список
    def __init__(self):
        self.task_list = []

    # Метод. Добавить задачу
    def add_task(self, description, deadline):
        self.task_list.append({
            "description": description,
            "deadline": deadline,
            "status": "НЕ выполнено"
        })

    # Метод. Поменять статус на "выполнено"
    def task_done(self, description):
        for task in self.task_list:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f"\nЗадача '{task['description']}' выполнена!")
                self.task_list.remove(task) # Удаление задачи из списка текущих, если статус поменялся
                return
            else:
                print(f"\nЗадача '{task}' НЕ найдена!")

    # Метод. Вывод списка текущих задач
    def current_tasks(self):

        if not self.task_list:
            print("Все задачи выполнены!")

        else:
            print(f"\nТекущие задачи:")
            i = 1
            for task in self.task_list:
               print(f"{i}. {task['description']}. Выполнить до {task['deadline']}")
               i += 1

# === Проверка ===
t = Task()

t.add_task("Помыть кошек", "20.05.2025")
t.add_task("Сделать кошкам маникюр", "21.05.2025")

t.current_tasks()

t.task_done("Помыть кошек")

t.current_tasks()