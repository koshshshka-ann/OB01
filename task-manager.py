# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():

    def __init__(self, name, description, deadline=None, status=False):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.status = status