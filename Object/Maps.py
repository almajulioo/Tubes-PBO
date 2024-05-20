import pygame
from .Dinding import Dinding
from .Peti import Peti
from .Background import Background
from .Kunci import Kunci

class Maps:
    MAPS = [
        "MAAFFAAAAAAAFFAAAAAAAAAAAAFFAAFAN",
        "   FF       FF            FF  F  ",            
        "M  FF FFFF  FF  FFFFFFFF  FF FF K",
        "M  AA AAFF PFF  FFFFFFFF ZFF FF K",
        "L       FFFFFF  FF   PFFFFFF FF K",
        "M       FFAAFF  FF  FFFAAAAA AA K",
        "LFFFFF  FF  FF  FF  FFF         K",
        "MAAAAA  FF  AA  FF  FFF         K",
        "L       FF      FF  FFF  FF  FF K",
        "M FF FFFFFFFFF  FF  FFF  FF  FF K",
        "L FF AAAAAAAFF  FF  AAA  FF  FF K",
        "M FF        FF  FF       FF  FFFK",
        "L FF        FF  FF       FF  AAAK",
        "M FFFFFFFF  FF  FFFFFFF  FF     K",
        "L AAAAAAAA  AA  AAAAAAA  FF     K",
        "M                        FF FF  K",
        "L                    FFFFFF AA  K",
        "MFFFFFFFFFFFF        FFAAAA     K",
        "LAAAAAAAAAAAA    P   FF     FFFFK",
        "M                    FF FF  AAFFK",
        "L                    FF FF    FFK",
        "M  FFFFF  FFF        FF PF    FFK",
        "L  FFFFF  FFFFFFFF  FFFFFF    FFK",
        "M  FFZFF  AAAAAAFF  AAAAFF    FFK",
        "L  FF AA        FF      FF    FFK",
        "M  AA    FFFFF  FF  FFFFFF    FFK",
        "L     FF AAAAF  FF  AAAAFF    FFK",
        "MFF   FF     F PFF      FF    AAK",
        "LFF   FF     FFFFF      FF     ZK",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",
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
                elif col == "F":
                    Dinding(x, y, "dinding_full")
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