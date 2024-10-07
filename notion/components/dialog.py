import reflex as rx
from notion.constant import ColorScheme
from notion.states import State
from .dynamic_icon import dynamic_icon as Dynamic_icon

class DialogState(State):
    opened: bool = False

    def count_opens(self, e):
        self.opened = not self.opened

def dialog(*args, **kwargs):
    title = kwargs.get("title")
    description = kwargs.get("description")
    button_content = kwargs.get("button_content")
    on_click = kwargs.get("on_click")
    to_clear = kwargs.get("to_clear")

    if button_content is None:
        button_content = rx.icon(tag="plus", color_scheme=ColorScheme.ADD.value)

    return rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(button_content, class_name="w-10 h-10 p-2 rounded-xl", on_click=on_click),
            ),

            rx.dialog.content(
                rx.box(
                    rx.cond(kwargs.get("icon"),
                        Dynamic_icon(kwargs.get("icon")),
                        None
                    ),
                    rx.dialog.title(title, class_name="capitalize m-0"),

                    class_name="flex items-center gap-3 mb-5",
                ),
                rx.dialog.description(
                    description,
                ),
                args,
                rx.box(
                    rx.dialog.close(
                        rx.button(rx.icon(tag="x"), size="3", color_scheme="red", class_name="w-10 h-10 p-2 rounded-xl mt-5", on_click=to_clear),
                    ),

                    class_name="flex w-full justify-end",
                ),
            ),
            on_open_change=DialogState.count_opens,
        ),
        direction="column",
        spacing="3",
    )
