import reflex as rx
from notion.constant import ColorScheme

def input(*args, **kwargs):
    placeholder = kwargs.pop("placeholder")
    variant = kwargs.pop("variant","soft")
    color_scheme = kwargs.pop("color_scheme", ColorScheme.INPUTS.value)
    size = kwargs.pop("size", "3")
    width = kwargs.pop("width", "100%")
    label = kwargs.pop("label", "")

    return rx.box(
        rx.heading(label, size="3"),
        rx.input(
            args,
            placeholder=rx.cond(placeholder, placeholder, "Search here..."), max_length=20,
            **kwargs,
            variant=rx.cond(variant, variant, "soft"),
            color_scheme=rx.cond(color_scheme, color_scheme, ColorScheme.INPUTS.value),
            size=rx.cond(size, size, "3"),
            width=width,
        ),
        width=width,
    )
