import random
from enum import Enum
from string import Template

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

def get_random_color(colorz: list) -> str:
    return random.choice(colorz)


def color():
    colorz = list()
    colorz.append("RED")
    colorz.append("GREEN")
    colorz.append("BLUE")
    colorz.append("ORANGE")

    return get_random_color(list(colorz))

colors = ColorsClient(COLORS.substitute(colorMade=color()))

print(colors.get_color_name())