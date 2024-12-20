import reflex as rx


def settings() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.text("Settings"),
            justify="center",
            min_height="85vh",
        ),
        bg=rx.color("crimson", 2),
        height="100vh",
    )
