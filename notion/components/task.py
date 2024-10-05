import reflex as rx
from notion.models.tasks import Tasks
from notion.states import State
from notion.constant import COLOR_SCHEME


def task(task: Tasks):
    return rx.card(
        rx.checkbox(
            default_checked=task.status,
            spacing="2",
            on_change=lambda a: State.change_status(task),
            class_name="text-4xl cursor-pointer",
            variant="soft",
            color_scheme=COLOR_SCHEME,
            size="5"
        ),
        rx.heading(task.title, class_name="select-none"),

        class_name="""
            px-5 flex items-center gap-5 min-w-40 min-h-10 hover:bg-black
            hover:bg-opacity-20 transition-all duration-300
            cursor-pointer
        """,
        on_click=lambda: State.change_status(task),
    )
