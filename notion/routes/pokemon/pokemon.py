import reflex as rx


@rx.page("/pokemon")
def pokemon():
    return rx.text("A Beautiful App")
