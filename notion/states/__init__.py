import reflex as rx
from typing import List
from notion.models.tasks import Tasks


class State(rx.State):
    title: str = "Hola"
    notes: List[Tasks] = [
        Tasks(title="primer test", description="", status=True)
    ]

    @rx.var
    def ready_tasks(self) -> List[Tasks]:
        return [i for i in self.notes if i.status]

    @rx.var
    def todo_tasks(self) -> List[Tasks]:
        return [i for i in self.notes if not i.status]

    def get_note(self, title: str):
        return [item for item in self.notes
                if item.title.lower() == title.lower()][0]

    def change_status(self, task: Tasks):
        task_saved = self.get_note(task["title"])
        status = bool(task_saved.status)
        new_task = Tasks(
            title=task_saved.title,
            description=task_saved.description,
            status=not status
        )

        index = self.notes.index(task_saved)
        self.notes[index] = new_task
