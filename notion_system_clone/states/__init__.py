import reflex as rx


class State(rx.State):
    title: str = "Hola"

    def change(self):
        self.title = "chau"
