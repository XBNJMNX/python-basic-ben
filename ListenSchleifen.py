#!/usr/bin/env python3

"""
def doppel_gerade(liste):
    neue_liste = []
    for zahl in liste:
        if zahl % 2 == 0:
            zahl *= 2
            neue_liste.append(zahl)
    return neue_liste
zahlen = [1,2,3,4,5,6]
print(doppel_gerade(zahlen))
"""
def check_number(n):
        if n > 0:
            return "positiv"
        elif n < 0:
            return "negativ"
        else:
            return "zero"
n = int(input("Gib eine Zahl ein:"))
print(check_number(n))
