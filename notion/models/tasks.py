import reflex as rx


class Tasks(rx.Base):
    title: str
    description: str
    status: bool
