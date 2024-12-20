import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.hstack(
                rx.icon(
                    "clock-8", stroke_width=1, size=80, color=rx.color("crimson", 10)
                ),
                rx.vstack(
                    rx.box(
                        rx.heading(
                            "Quit Clock",
                            size="9",
                            color_scheme="crimson",
                            weight="medium",
                        ),
                        rx.text(
                            "Saying goodbye to bad habits one day at a time!",
                            size="5",
                            weight="light",
                        ),
                    ),
                    rx.button("Login"),
                ),
            ),
            justify="center",
            min_height="85vh",
        ),
        bg=rx.color("crimson", 2),
        height="100vh",
    )
