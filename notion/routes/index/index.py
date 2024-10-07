import reflex as rx
from notion.components.navbar import navbar as Navbar
from notion.components.note_insertion import note_insert as Note_insert
from notion.states import State
from notion.components.task import task as Task
from notion.components.card import card as Card
from notion.states.notes import Notes


@rx.page('/', title="Inicio")
def index() -> rx.Component:
    return rx.center(
        Navbar(),
        rx.flex(
            Note_insert(),
            rx.grid(
                Card(
                    rx.heading("Por Hacer"),
                    rx.foreach(
                        Notes.ready_tasks,
                        Task,
                    ),
                    class_name="items-start flex-wrap",
                ),
                Card(
                    rx.heading("Hechas"),
                    rx.foreach(
                        Notes.todo_tasks,
                        Task,
                    ),
                    class_name="items-start flex-wrap",
                ),

                columns="2",
                spacing="5",
                width="100%",
            ),

            class_name="flex flex-grow flex-col h-full w-full gap-5",
        ),
        class_name="""
            flex-col p-[16px] pb-0 gap-5 mx-auto max-w-[880px] min-h-screen
        """,
    )
