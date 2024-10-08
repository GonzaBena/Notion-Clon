import reflex as rx
from notion.constant import ColorScheme, Icons
from notion.states import State
from .dynamic_icon import dynamic_icon as Dynamic_icon

class DialogState(rx.State):
    opened: bool = False

    def count_opens(self, e):
        self.opened = not self.opened

def dialog(*args, **kwargs):
    title = kwargs.pop("title", "Dialog")
    description = kwargs.pop("description", "")
    button_content = kwargs.pop("button_content", None)
    on_click = kwargs.pop("on_click", None)
    to_clear = kwargs.pop("to_clear", None)
    icon = kwargs.pop("icon", Icons.EARTH.value)

    if button_content is None:
        button_content = rx.icon(tag="plus", color_scheme=ColorScheme.ADD.value)

    return rx.flex(
        rx.dialog.root(
            rx.dialog.trigger(
                rx.button(button_content, class_name="w-10 h-10 p-2 rounded-xl", on_click=on_click),
            ),

            rx.dialog.content(
                rx.box(
                    Dynamic_icon(icon),
                    rx.dialog.title(title, class_name="capitalize m-0"),

                    class_name="flex items-center gap-3 mb-5",
                ),
                rx.dialog.description(
                    description,
                ),
                rx.box(
                    args,
                    **kwargs,
                ),
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
