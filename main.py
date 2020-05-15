#!/usr/bin/env python3
# Dev by Jean Dubois
# This program is in the public domain.

import quadrilateres
import triangles
import others
import trad
import os
import locale
import ctypes

windll = ctypes.windll.kernel32

try:
    if 'FR' in os.getenv('LANG'):
        lang = 'french'
    else:
        lang = 'english'
except TypeError:
    if 'fr' in locale.windows_locale[windll.GetUserDefaultUILanguage()]:
        lang = 'french'
    else:
        lang = 'english'

is_first_time = True


def welcome():
    global is_first_time
    if is_first_time:
        print(trad.Translations.get('1'+lang))
        print("")
        is_first_time = False
    print(trad.Translations.get('2'+lang))
    print("")
    print("=====FIGURES=====")
    print("")
    print("1 - Carré")
    print("2 - Rectangle")
    print("3 - Triangle quelconque")
    print("    31 - Triangle rectangle")
    print("    32 - Triangle isocèle")
    print("    33 - Triangle isocèle rectangle")
    print("    34 - Triangle équilatéral")
    print("4 - Cercle / disque")
    print("")
    print("=====SOLIDES=====")
    print("====COMMANDES====")
    print("")
    print("99 - Quitter")
    print("")
    figure = int(input())
    return figure


def verify():
    figure = welcome()
    if figure == 1:
        quadrilateres.square_calc()
        verify()
    elif figure == 2:
        quadrilateres.rect_calc()
        verify()
    elif figure == 3:
        triangles.triangle_calc()
        verify()
    elif figure == 31:
        triangles.tri_rect_calc()
        verify()
    elif figure == 32:
        triangles.tri_isocele_calc()
        verify()
    elif figure == 33:
        triangles.tri_isocele_rect_calc()
        verify()
    elif figure == 34:
        triangles.tri_equilateral_calc()
        verify()
    elif figure == 4:
        others.circle_calc()
        verify()
    elif figure == 99:
        quit()


verify()
