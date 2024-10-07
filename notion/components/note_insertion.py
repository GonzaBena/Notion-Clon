import reflex as rx
from notion.states import State
from notion.states.notes import Notes
from notion.constant import ColorScheme
from .insert_note import insert_note as Insert_note
from .card import card as Card


class NoteState(State):
    text: str = ""

    def clear_text(self):
        self.text = ""


def note_insert():
    return Card(
        rx.hstack(
            rx.input(
                placeholder="Search here...", max_length=20,
                value=Notes.condition,
                on_change=lambda value: Notes.set_condition(value),
                variant="soft",
                color_scheme=ColorScheme.INPUTS.value, 
                size="3",
                width="100%",
            ),
            rx.button(
                "Erase", 
                on_click=lambda: Notes.set_condition(""),
                color_scheme=ColorScheme.DELETE.value,
            ),
            Insert_note(),

            class_name="justify-center items-center w-[80%]"
        ),

        min_height="100px",
        class_name="""
            w-full gap-5 items-center justify-center
        """
    )
