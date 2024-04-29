import pygame
from .Dinding import Dinding
from .Peti import Peti
from .Background import Background

class Maps:
    MAPS = [
        "LAAAAAAAAAAAAAAAAAAAAAAAAL",
        "                         K",
        "K                  P     K",
        "K                        K",
        "L                        L",
        "K                        K",
        "K                        K",
        "L                        L",
        "K                        K",
        "K                        K",
        "L                        L",
        "K                        K",
        "K                        K",
        "L                        L",
        "K                        K",
        "K                        K",
        "K                        K",
        "L                        L",
        "LCBBCBBCBBCBBBBCBBCBBCBBCL",
    ]

    def __init__(self):
        x = 30
        y = 30

        countrow = 0
        countcol = 0
        for row in self.MAPS:
            countrow+=1
            for col in row:
                countcol += 1
                if countrow == 1 and col == "L":
                    x-= 9
                    if countcol == 1:
                        Dinding(x + 9, y, "kiri2")
                    else:
                        Dinding(x, y, "kiri2")
                elif countrow == 19 and col == "L":
                    x-= 9
                    if countcol == 1:
                        Dinding(x + 9, y, "kiri2")
                    else:
                        Dinding(x, y, "kiri2")

                
                elif col == "A":
                    Dinding(x, y, "atas")
                elif col == "K":
                    if countcol == 26:
                        Dinding(x - 18, y, "kiri")
                    else:
                        Dinding(x, y, "kiri")
                elif col == "L":
                    if countcol == 26:
                        Dinding(x - 18, y, "kiri2")
                    else:
                        Dinding(x, y, "kiri2")
                elif col == "B":
                    Dinding(x, y + 8, "bawah")
                elif col == "C":
                    Dinding(x, y + 8, "bawah2")
                elif col == "G":
                    pass
                elif col == "P":
                    Background(x - 24, y)
                    Peti(x, y)
                elif col == " ":
                    Background(x - 24, y)
                x += 30
            countcol= 0
            y += 30
            x = 30