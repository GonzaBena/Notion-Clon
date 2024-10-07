from typing import Optional

import reflex as rx

from notion.components.dialog import dialog as Dialog
from notion.components.dynamic_icon import dynamic_icon as Dynamic_icon
from notion.constant import COLOR_SCHEME, Icons
from notion.models.tasks import Tasks
from notion.states.notes import Notes


class TaskState(rx.State):
    open: bool = False
    task: Optional[Tasks] = None
    modified_task: Optional[Tasks] = None
    icon: Icons = Icons.EARTH

    @rx.var
    def was_modified(self) -> bool:
        return self.modified_task is not None and self.modified == self.task

    def toggle(self):
        self.open = not self.open

    def assign_task(self, task: Tasks):
        self.toggle()
        self.task = task

    def clear_task(self):
        self.task = None
        self.open = False




def edit_task(**kwargs):
    task = kwargs.get("task")

    return Dialog(
        rx.heading("This is a dialog", size="3"),
        button_content = rx.icon(tag="pencil", color_scheme=COLOR_SCHEME),
        title=task.title,
        description = rx.cond(TaskState.task, TaskState.task.description, "No description available"),
        icon=task.icon,
        
        on_click = lambda : TaskState.assign_task(task),
        to_clear = TaskState.clear_task,
    )


def task(task: Tasks):
    return rx.card(
        rx.grid(
            rx.checkbox(
                default_checked=task.status,
                spacing="2",
                on_change=lambda value: Notes.change_status(task),
                class_name="text-4xl cursor-pointer",
                variant="soft",
                color_scheme=COLOR_SCHEME,
                size="3"
            ),
            rx.hstack(
                Dynamic_icon(task.icon),
                rx.heading(task.title, class_name="select-none capitalize", weight="bold"),

                class_name="flex items-center gap-2"
            ),
            rx.heading(task.description, class_name="select-none col-start-2", weight="regular", size="3"),

            columns="50px 1fr",
            rows=rx.cond(task.description, "2", "1"),
            class_name="w-full items-start justify-items-start"
        ),
        edit_task(task=task),

        class_name="""
            px-5 flex flex-row items-start gap-5 min-w-40 w-full min-h-10 hover:bg-black
            hover:bg-opacity-20 transition-all duration-300
            cursor-pointer
        """,
    )
