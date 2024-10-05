import reflex as rx


def clipboard(text: str):
    return rx.button(
        rx.icon(tag="copy"),
        color_scheme="gray",
        on_click=rx.set_clipboard(text)
    )
