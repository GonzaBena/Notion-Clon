"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .routes import routes

app = rx.App()

for route in routes:
    # print(f"Adding route: {route}")

    # Call add_page with the dynamically constructed arguments
    app.add_page(route)
