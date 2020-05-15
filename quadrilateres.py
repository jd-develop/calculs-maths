#!/usr/bin/env python3
# Nothing to import
# Rien à importer

def square_calc():
    print("Veuillez entrer la longueur du côté c en centimètres :")
    c = int(input())
    perimetre = c * 4
    aire = c * c
    print("Pour pour un carre de côté", c, "centimètres, le périmètre sera", perimetre,
          "centimètres et l'aire sera de", aire, "centimètres carrés .")


def rect_calc():
    print("Veuillez entrer la longueur l en centimètres :")
    longueur = int(input())
    print("Veuillez entrer la largeur L en centimètres :")
    largeur = int(input())
    perimetre = longueur * 2 + largeur * 2
    aire = longueur * largeur
    print("Pour pour un rectangle de longueur ", longueur, "centimètres et de largeur, le périmètre sera",
          perimetre, "centimètres et l'aire sera de", aire, "centimètres carrés .")
