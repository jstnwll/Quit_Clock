from sqlmodel import Field

import reflex as rx

class User(rx.Model, table=True):
    username: str
    password: str

class Habits(rx.Model, table=True):
    event: str
    date:
