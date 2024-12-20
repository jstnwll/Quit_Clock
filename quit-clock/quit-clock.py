from .pages import index, details, settings, dashboard
from .components import login
import reflex as rx

app = rx.App(
    theme=rx.theme(
        appearance="inherit",
        accent_color="crimson",
    )
)


app.add_page(index, route="/")
app.add_page(details, route="/details")
app.add_page(settings, route="/settings")
app.add_page(dashboard, route="/dashboard")
