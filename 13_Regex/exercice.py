# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:59:51 2019

Printer une phrase tant que l'utilisateur le demande - Code

@author: guillaume
"""

i = 0
continuer = "o"
 
while continuer == "o":
	print(f"Le compteur est maintenant à {i}")
	continuer = input("Voulez-vous continuer ? o/n ")
	i += 1