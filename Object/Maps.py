import pygame
from .Dinding import Dinding
from .Peti import Peti
from .Background import Background
from .Kunci import Kunci

class Maps:
    MAPS = [
        "MAAAAAAAAAAAAAAAAAAAAAAN",
        "     K L   PL          K",
        "L    AAA    L      P   N",
        "M           AAA        K",
        "L    VVV               N",
        "MVVVVK LV  VV          K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M                      K",
        "L                      N",
        "M              Z  Z    K",
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
        countrow = 0
        for row in self.MAPS:
            countrow += 1
            countcol = 0
            for col in row:
                countcol += 1
                if not countrow == 1 and not countrow == 18 and not countcol == 1 and not countcol == 24:
                    Background(x, y)
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
                elif col == "V":
                    Dinding(x, y + 9, "bawah")
                elif col == "C":
                    Dinding(x, y - 9, "bawah2")
                elif col == "G":
                    Dinding(x + 9, y - 10, "penghubung")
                elif col == "H":
                    Dinding(x - 9, y - 10, "penghubung")
                elif col == "P":
                    Peti(x, y)
                elif col == "Z":
                    Background(x, y)
                    Kunci(x, y, "")
                elif col == " ":
                    Background(x , y)
                x += 32
            y += 32
            x = 30