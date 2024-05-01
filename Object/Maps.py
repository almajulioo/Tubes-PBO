import pygame
from .Dinding import Dinding
from .Peti import Peti
from .Background import Background

class Maps:
    MAPS = [
        "MAAAAAAAAAAAAAAAAAAAAAAN",
        "                       K",
        "L                  P   N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      K",
        "M                      K",
        "L                      K",
        "GCBBCBBCBBCBBBBCBBCBBCBH",
    ]

    def __init__(self):
        x = 30
        y = 30

        for row in self.MAPS:
            for col in row:
                if col == "A":
                    Dinding(x, y, "atas")
                elif col == "L":
                    Dinding(x + 9, y, "kiri")
                elif col == "M":
                    Dinding(x + 9, y, "kiri2")
                elif col == "K":
                    Dinding(x - 9, y, "kanan")
                elif col == "N":
                    Dinding(x - 9, y, "kanan2")
                elif col == "B":
                    Dinding(x, y - 9, "bawah")
                elif col == "C":
                    Dinding(x, y - 9, "bawah2")
                elif col == "G":
                    Dinding(x + 9, y - 10, "penghubung")
                elif col == "H":
                    Dinding(x - 9, y - 10, "penghubung")
                elif col == "P":
                    Background(x, y)
                    Peti(x, y)
                elif col == " ":
                    Background(x , y)
                x += 32
            y += 32
            x = 30