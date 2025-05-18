# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task():

    current_tasks = [] # список текущих задач (задачи, где status=False)

    # Инициация объекта
    def __init__(self, description, deadline=None, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status
        if not status:
            Task.current_tasks.append(self) # все задачи со статусом False добавляются в список текущих

    # Добавление задачи
    @staticmethod
    def add_task(description, deadline=None, status=False):
        new_task = Task(description, deadline, status)
        return new_task

    # Отметка о выполнении
    def mark_done(self): # меняем статус на "выполнено" и удаляем из текущих
        if not self.status:
            self.status=True
            Task.current_tasks.remove(self)

    # Отметка о НЕ выполнении
    def mark_undone(self):
        if self.status:
            self.status=False
            Task.current_tasks.append(self)

    # Возврат текущего списка задач (для дальнейшего использования в коде)
    @staticmethod
    def get_current_list():
        return list(Task.current_tasks)

    # Красивый вывод списка текущих задач (для пользователя)
    @staticmethod
    def print_current_list():
        print(f"\nСписок текущих задач:")

        if not Task.current_tasks:
            print("Все задачи выполнены!")
            return

        else:
            i = 1
            for current_task in Task.current_tasks:
                deadline_info = f" до {current_task.deadline}" if current_task.deadline else ""
                print(f"{i}. {current_task.description}{deadline_info}")
                i += 1

# === Тестирование ===

# Метод: Добавление задачи
task1 = Task.add_task("Помыть кошек", "20/05/2025") # Задача 1
task2 = Task.add_task("Сделать кошкам маникюр") # Задача 2 (без дедлайна)
task3 = Task.add_task("Выполнить домашку Zerocoder", "18/05/2025") # Задача 3

# Метод: Красивый вывод списка текущих задач
Task.print_current_list()

# Метод: Отметка о выполнении
task3.mark_done()
print(f"\nПосле mark_done(): {task3.description}: {task3.status}") # Контрольный вывод

# Метод: Отметка о НЕ выполнении
task3.mark_undone()
print(f"\nПосле mark_undone(): {task3.description}: {task3.status}") # Контрольный вывод

# Метод: Отметка о выполнении (все задачи)
task1.mark_done()
task2.mark_done()
task3.mark_done()

# Метод: Красивый вывод списка текущих задач (все задачи выполнены)
Task.print_current_list()
