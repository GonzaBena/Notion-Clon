import reflex as rx
from typing import Any, List

from notion.models.tasks import Tasks
from . import State


class Notes(State):
    notes: List[Tasks] = [
        Tasks(title="primer test 1", description="", status=True),
        Tasks(title="primer test 2", description="", status=True),
        Tasks(title="primer test 3", description="", status=True),
        Tasks(title="primer test 4", description="", status=True),
    ]
    notes_filtered: List[Tasks] = notes
    condition: str = ""

    def to_tasks(self, notes: List[Any]) -> List[Tasks]:
        tasks: List[Tasks] = []
        for i in notes:
            task = {}
            keys = i.get_fields()
            for key in keys:
                task[key] = i.get_value(key)
            tasks.append(Tasks(**task))
        return tasks

    @rx.var
    def ready_tasks(self) -> List[Tasks]:
        return [i for i in self.notes_filtered if i.status]
    
    def set_condition(self, condition: str) -> None:
        self.condition = condition.lower().strip()
        self.filter_notes()

    def filter_notes(self) -> None:
        tasks = list(filter(lambda a: self.condition.lower() in a.title.lower(), self.notes))
        self.notes_filtered = self.to_tasks(tasks)

    def add_note(self, note: Tasks):
        self.notes.append(note)
        if self.condition in note.title.lower():
            self.notes_filtered = self.notes

    @rx.var
    def todo_tasks(self) -> List[Tasks]:
        return [i for i in self.notes_filtered if not i.status]

    def get_note(self, title: str):
        return [item for item in self.notes_filtered 
                if item.title.lower() == title.lower()][0]

    def change_status(self, task: Tasks):
        task_saved = self.get_note(task["title"])
        status = bool(task_saved.status)
        new_task = Tasks(
            title=task_saved.title,
            description=task_saved.description,
            status=not status
        )

        index = self.notes_filtered.index(task_saved)
        self.notes_filtered[index] = new_task
