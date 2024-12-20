import reflex as rx


def dashboard() -> rx.Component:
    return rx.container(
        rx.hstack(
            # The logo.
            rx.icon("clock-8", stroke_width=1, size=25, color=rx.color("crimson", 10)),
            rx.text("Quit Clock", size="6", color_scheme="crimson"),
            rx.spacer(),
            align="center",
            width="100%",
            padding_y="1.25em",
            padding_x=["1em", "1em", "1em"],
        ),
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.card("summary"),
            justify="center",
            min_height="85vh",
        ),
        bg=rx.color("crimson", 2),
        height="100vh",
    )
