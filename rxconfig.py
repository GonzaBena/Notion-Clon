import reflex as rx

config = rx.Config(
    app_name="notion",
    tailwind={
        "theme": {
            "extend": {},
        },
        "plugins": ["@tailwindcss/typography"],
    }
)
