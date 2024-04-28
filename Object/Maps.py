import pygame
from .Dinding import Dinding
from .Peti import Peti

class Maps:
    MAPS = [
        " DDDDDDDDDDDDDDDDDDDDDDDDD",
        "                         D",
        "D                  P     D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "D                        D",
        "DDDDDDDDDDDDDDDDDDDDDDDDDD",
    ]

    def __init__(self):
        x = 30
        y = 30
        for row in self.MAPS:
            for col in row:
                if col == "D":
                    Dinding(x, y)
                if col == "P":
                    Peti(x, y)
                x += 30
            y += 30
            x = 30