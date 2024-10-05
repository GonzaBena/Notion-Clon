import reflex as rx

config = rx.Config(
    app_name="notion_system_clone",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    }
)
