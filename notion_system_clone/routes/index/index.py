import reflex as rx
from ...states import State
from ...components.navbar import navbar as Navbar


@rx.page('/', title="Inicio")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        Navbar(),
        rx.vstack(
            rx.heading(State.title, class_name="text-4xl"),
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
