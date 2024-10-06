import reflex as rx
from notion.states import State
from notion.states.notes import Notes
from notion.constant import COLOR_SCHEME
from .card import card as Card


class NoteState(State):
    text: str = ""
    color_scheme: str = COLOR_SCHEME

    def clear_text(self):
        self.text = ""


def note_insert():
    return Card(
        rx.hstack(
            rx.input(
                placeholder="Search here...", max_length=20,
                value=NoteState.text,
                on_change=lambda value: Notes.set_condition(value),
                variant="soft",
                color_scheme=NoteState.color_scheme,
                size="3",
                width="100%",
            ),
            rx.heading(NoteState.text),
            rx.button(
                "Erase", 
                on_click=NoteState.clear_text,
                color_scheme=NoteState.color_scheme,
            ),

            class_name="justify-center items-center w-[80%]"
        ),

        min_height="100px",
        class_name="""
            w-full gap-5 items-center justify-center
        """
    )
