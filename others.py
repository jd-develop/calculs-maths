#!/usr/bin/env python3
import math


def circle_calc():
    print("Veuillez entrer le rayon de votre cercle ou votre disque :")
    r = int(input())
    d = r * 2
    perimetre = math.pi * d
    aire = math.pi * r * r
    if perimetre == math.pi:
        perimetre = "π"
    if aire == math.pi:
        aire = "π"
    print("Pour un cercle ou un disque de rayon", r, "centimètres, le périmètre sera de",
          perimetre, "centimètres et l'aire de", aire, "centimètres carrés.")
