"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .routes import routes
from .styles.globals import styles

app = rx.App(style=styles)

for route in routes:
    # print(f"Adding route: {route}")

    # Call add_page with the dynamically constructed arguments
    app.add_page(route)
