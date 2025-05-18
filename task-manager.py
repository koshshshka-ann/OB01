# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
class Task():

    current_tasks = [] # список текущих задач (задачи, где status=False)

    def __init__(self, description, deadline=None, status=False): # инициализация объекта
        self.description = description
        self.deadline = deadline
        self.status = status
        if not status:
            Task.current_tasks.append(self) # все задачи со статусом False добавляются в список текущих

    @staticmethod
    def add_task(description, deadline=None, status=False):
        new_task = Task(description, deadline, status)
        return new_task

    def mark_done(self): # меняем статус на "выполнено" и удаляем из текущих
        if not self.status:
            self.status=True
            Task.current_tasks.remove(self)

    def mark_undone(self):
        if self.status:
            self.status=False
            Task.current_tasks.append(self)

    @staticmethod
    def get_current_list():
        return list(Task.current_tasks)

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

task1 = Task.add_task("Помыть кошек", "20/05/2025")
task2 = Task.add_task("Сделать кошкам маникюр", None)
task3 = Task.add_task("Выполнить домашку Zerocoder", "18/05/2025")

Task.print_current_list()

task3.mark_done()
print(f"\nПосле mark_done(): {task3.description}: {task3.status}")

task3.mark_undone()
print(f"\nПосле mark_undone(): {task3.description}: {task3.status}")

task1.mark_done()
task2.mark_done()
task3.mark_done()

Task.print_current_list()
