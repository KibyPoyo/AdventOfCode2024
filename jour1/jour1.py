#=|=# Jour 1 de l'Advent of Code 2024 #=|=#

def lecture_fichier(fichier,fonction):
    try:
        import os
        print("Dossier courant :", os.getcwd())
        with open(fichier, "r") as f:
            fonction(f)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def distance(fichier):
    tab1 = []
    tab2 = []
    
    for ligne in fichier:
        ligne = ligne.strip()
        nombres = ligne.split()
        tab1.append(int(nombres[0]))
        tab2.append(int(nombres[1]))
    
    tab1.sort()
    tab2.sort()

    somme = 0
    for i in range(len(tab1)):
        somme += abs(tab1[i] - tab2[i])
    
    print(somme)
    
def similarity(fichier):
    tab1 = []
    tab2 = []
    
    for ligne in fichier:
        ligne = ligne.strip()
        nombres = ligne.split()
        tab1.append(int(nombres[0]))
        tab2.append(int(nombres[1]))

    somme = 0
    for i in range(len(tab1)):
        for j in range(len(tab2)):
            if tab1[i] == tab2[j]:
                somme += tab1[i]

    print(somme)

lecture_fichier("jour1/jour1.txt",similarity)