import pygame
from .Dinding import Dinding
from .Peti import Peti

class Maps:
    MAPS = [
        "LAAAAAAAAAAAAAAAAAAAAAAAAL",
        "                         K",
        "K                  P     K",
        "K                        K",
        "L                        K",
        "K                        K",
        "K                        K",
        "L                        K",
        "K                        K",
        "K                        K",
        "L                        K",
        "K                        K",
        "K                        K",
        "L                        K",
        "K                        K",
        "K                        K",
        "K                        K",
        "L                        K",
        "LCBBCBBCBBBBBBBBBBCBBCBBCL",
    ]

    def __init__(self):
        x = 30
        y = 30
        countrow = 0
        countcol = 0
        for row in self.MAPS:
            countrow+=1
            print(countrow)
            for col in row:
                countcol += 1
                if countrow == 1 and col == "L" and countcol == 1:
                    x-= 9
                    Dinding(x + 9, y, "kiri2")
                elif countrow == 19 and col == "L" and countcol == 1:
                    x-= 9
                    Dinding(x + 9, y, "kiri2")
                
                elif col == "A":
                    Dinding(x, y, "atas")
                elif col == "K":
                    if countcol == 26:
                        Dinding(x - 18, y, "kiri")
                    else:
                        Dinding(x, y, "kiri")
                elif col == "L":
                    if countcol == 26:
                        Dinding(x - 9, y, "kiri2")
                    else:
                        Dinding(x, y, "kiri2")
                elif col == "B":
                    Dinding(x, y + 8, "bawah")
                elif col == "C":
                    Dinding(x, y + 8, "bawah2")
                elif col == "P":
                    Peti(x, y)
                x += 30
            countcol= 0
            y += 30
            x = 30