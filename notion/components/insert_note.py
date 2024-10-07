import reflex as rx
from notion.constant import ColorScheme
from .dialog import dialog as Dialog


def insert_note():
    return rx.flex(
        Dialog(
            rx.heading("This is a dialog", size="3"),
            title="Welcome to Reflex!",
            description="This is a dialog component. You can render anything you want in here.",
        ),
        direction="column",
        spacing="3",
    )
