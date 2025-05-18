# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():

    current_tasks = [] # список текущих задач (задачи, где status=False)

    def __init__(self, description, deadline=None, status=False): # инициализация объекта
        self.description = description
        self.deadline = deadline
        self.status = status
        if not status:
            Task.current_tasks.append(self) # все задачи со статусом False добавляются в список текущих

    def add_task(self, description, deadline=None, status=False):
        new_task = Task(description, deadline, status)
        return new_task

    def mark_done(self): # меняем статус на "выполнено" и удаляем из текущих
        self.status=True
        Task.current_tasks.remove(self)

    def marc_undone(self):
        self.status=False
        Task.current_tasks.append(self)