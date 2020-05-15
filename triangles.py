#!/usr/bin/env python3
import math


def triangle_calc():
    print("Veuillez entrer la longueur du premier côté :")
    c = int(input())
    print("Veillez entrer la longueur du deuxième côté :")
    c2 = int(input())
    print("Veuillez entrer la longueur du troisième côté :")
    c3 = int(input())
    print("Veuillez entrer la hauteur perpendiculaire au premier côté :")
    h = int(input())
    perimetre = c + c2 + c3
    aire1 = c * h
    aire = aire1 / 2
    print("Pour un triangle dont les longueurs des côtés sont", str(c) + ",", c2, "et", c3,
          "centimètres, et dont la hauteur est de", h, "centimètres, le périmètre sera de", perimetre,
          "centimètres, et l'aire de", aire, "centimètres carrés.")


def tri_rect_calc():
    print("Veuillez entrer la longueur du plus petit côté :")
    c = int(input())
    print("Veillez entrer la longueur du côté moyen :")
    c2 = int(input())
    c3 = math.sqrt(c * c + c2 * c2)
    perimetre = c + c2 + c3
    aire1 = c * c3
    aire = aire1 / 2
    print("Pour un triangle dont les longueurs des côtés sont", c, "et", c2,
          "centimètres, et dont l'hypothénuse / hauteur est de", c3, "centimètres, le périmètre sera de",
          perimetre, "centimètres, et l'aire de", aire, "centimètres carrés")


def tri_isocele_calc():
    print("Veuillez entrer la longueur d'un des côtés égaux :")
    c = int(input())
    print("Veillez entrer la longueur du deuxième côté :")
    c2 = int(input())
    print("Veuillez entrer la hauteur perpendiculaire au dexième côté :")
    h = int(input())
    perimetre = c * 2 + c2
    aire1 = c2 * h
    aire = aire1 / 2
    print("Pour un triangle dont les longueurs des côtés sont", str(c) + ",", c, "et", c2,
          "centimètres, et dont la hauteur est de", h, "centimètres, le périmètre sera de", perimetre,
          "centimètres, et l'aire de", aire, "centimètres carrés.")


def tri_isocele_rect_calc():
    print("Veuillez entrer la longueur d'un des deux côtés égaux :")
    c = int(input())
    c2 = math.sqrt(c * c + c * c)
    perimetre = c * 2 + c2
    aire1 = c * c
    aire = aire1 / 2
    print("Pour un triangle dont les longueurs des côtés est de", c,
          "centimètres, et dont l'hypothénuse / hauteur est de", c2,
          "centimètres, le périmètre sera de", perimetre, "centimètres, et l'aire de",
          aire, "centimètres carrés")


def tri_equilateral_calc():
    print("Veuillez entrer la longueur d'un des côtés :")
    c = int(input())
    h = c * math.sqrt(3) / 2
    perimetre = c * 3
    aire1 = c * c
    aire = aire1 / 2
    print("Pour un triangle dont les longueurs des côtés est de", c,
          "centimètres, et dont la hauteur est de", h, "centimètres, le périmètre sera de",
          perimetre, "centimètres, et l'aire de", aire, "centimètres carrés")
