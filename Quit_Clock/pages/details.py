import reflex as rx


def details() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.text("Details"),
            justify="center",
            min_height="85vh",
        ),
        bg=rx.color("crimson", 2),
        height="100vh",
    )
