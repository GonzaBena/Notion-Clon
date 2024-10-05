import reflex as rx
from notion.states import State
from notion.constant import COLOR_SCHEME
from .card import card as Card


class NoteState(State):
    text: str = ""
    color_scheme: str = COLOR_SCHEME

    def def_text(self, string: str):
        self.text = string


def note_insert():
    return Card(
        rx.hstack(
            rx.input(
                placeholder="Search here...", max_length=20,
                value=NoteState.text,
                on_change=NoteState.set_text,
                variant="soft",
                color_scheme=NoteState.color_scheme,
                size="3",
                width="100%",
            ),
            rx.button("Erase", on_click=lambda: NoteState.def_text(
                ""), color_scheme=NoteState.color_scheme),

            class_name="justify-center items-center w-[80%]"
        ),

        min_height="100px",
        class_name="""
            w-full gap-5 items-center justify-center
        """
    )
