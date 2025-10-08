import random
from enum import Enum
from string import Template
from typing import TypeAlias

class Color(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    ORANGE = "ORANGE"

class ColorsClient:
    def __init__(self, colorz: str):
        self.color = colorz
    def get_color_name(self):
        return self.color

COLORS: Template = Template("$colorMade")


def get_color():

    if color == Color.RED:
        print(Color["RED"])
    elif color == Color.BLUE:
        print(Color["BLUE"])
    elif color == Color.GREEN:
        print(Color["GREEN"])
    elif color == Color.ORANGE:
        print(Color["ORANGE"])

TypedColor: TypeAlias = list[tuple[str]]

def get_random_color(colorz: TypedColor) -> TypedColor:
    return random.choice(colorz)


def color() -> TypedColor:
    colorz = list()
    colorz.append("RED")
    colorz.append("GREEN")
    colorz.append("BLUE")
    colorz.append("ORANGE")

    return get_random_color(TypedColor(colorz))

colors = ColorsClient(COLORS.substitute(colorMade=color()))

print(colors.get_color_name())