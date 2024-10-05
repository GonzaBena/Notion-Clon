"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .routes import routes

from rxconfig import config
from .states import State


@rx.page('/', title="Inicio")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.title, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.button("Hola", on_click=State.change),
        rx.link("Reflex Home Page.", href="https://reflex.dev/"),
        rx.link("Reflex Home Page.", href="/pokemon"),
        rx.logo(),
    )


app = rx.App()

for route in routes:
    # print(f"Adding route: {route}")

    # Call add_page with the dynamically constructed arguments
    app.add_page(route)
