import reflex as rx

from .dynamic_icon import dynamic_icon as Dynamic_icon
from .dialog import dialog as Dialog
from .input import input as Input
from notion.constant import Icons


class NoteState(rx.State):
    title: str = ""
    description: str = ""
    status: bool = False
    icon: str = Icons.EARTH.value

    def change_description(self, content: str):
        """Handle the editor value change."""
        self.description = content

    def save_note(self):
        """Save the note."""
        print(
            f"Title: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nIcon: {self.icon}"
        )


def insert_note():
    icons = {i.name: i.value for i in Icons}.values()
    return rx.flex(
        Dialog(
            Input(label="Title", placeholder="Enter title here..."),

            rx.editor(
                height="100px",
                set_contents=NoteState.description,
                set_options=rx.EditorOptions(
                    button_list=[
                        ["undo", "redo"],
                        [
                            "bold",
                            "underline",
                            "italic",
                            "strike",
                            "subscript",
                            "superscript",
                        ],
                        ["removeFormat"],
                        ["outdent", "indent"],
                        ["fullScreen", "showBlocks", "codeView"],
                    ],
                ),
                on_change=NoteState.change_description,
            ),

            rx.grid(
                rx.flex(
                    "Status",
                    rx.switch(
                        default_checked=NoteState.status,
                        name="status",
                        on_change=NoteState.set_status,
                    ),
                    spacing="2",
                    justify="start",
                    class_name="w-full items-center justify-center",
                ),
                rx.flex(
                    rx.heading("Icon"),
                    rx.select(
                        icons,
                        default_value=NoteState.icon,
                        on_change=NoteState.set_icon,
                        placeholder="Select an icon",
                        label="Icon",
                        width="100px",
                        variant="soft",
                        radius="full",
                        size="2",
                    ),
                    Dynamic_icon(NoteState.icon),

                    spacing="2",
                    justify="between",
                    class_name="w-full items-center justify-center",
                ),
                class_name="w-full",
                columns="2",
            ),

            rx.button(
                "Save",
                on_click=NoteState.save_note,
                variant="soft",
                width="full",
                class_name="mt-5",
            ),

            title="Add a new note",
            description="",
            class_name="flex flex-col gap-5",
        ),
        direction="column",
        spacing="3",
    )
