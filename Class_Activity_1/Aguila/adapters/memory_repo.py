from domain.ports import TaskOutputPort
from domain.entities import Task

class InMemoryTaskRepository(TaskOutputPort):
    def __init__(self):
        self.tasks = []

    def save(self, task: Task) -> None:
        self.tasks = [t for t in self.tasks if t.id != task.id]
        self.tasks.append(task)

    def list_all(self) -> list[Task]:
        return self.tasks
    # Añadimos al repositorio la funcion get_by_id para obtener una tarea por su id
    def get_by_id(self, task_id: str) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
