#=|=# Jour 10 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Factorisable + récursion ! '''

# ========= INITIALIZATION ========== #
def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    tab = []
    
    for ligne in fichier:
        ligne = ligne.strip()
        tab.append([int(chiffre) for chiffre in ligne])
    
    return tab

# ============= PART 1 ============= #
def find_path_score(tab,i,j,value,seen):
    if tab[i][j] != value:
        return seen
    if value == 9 and (i,j) not in seen:
        seen.add((i,j))
        return seen
    if i-1 >= 0:
        seen = find_path_score(tab,i-1,j,value+1,seen)
    if i+1 < len(tab):
        seen = find_path_score(tab,i+1,j,value+1,seen)
    if j-1 >= 0:
        seen = find_path_score(tab,i,j-1,value+1,seen)
    if j+1 < len(tab[i]):
        seen = find_path_score(tab,i,j+1,value+1,seen)
    return seen

def part_1(fichier):
    score = 0
    tab = fichier_to_tab(fichier)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 0:
                score += len(find_path_score(tab,i,j,0,set()))

    print("Part 1 :",score)
    return score

# ============= PART 2 ============= #
def find_path_score(tab,i,j,value):
    if tab[i][j] != value:
        return 0
    if value == 9:
        return 1
    score = 0
    if i-1 >= 0:
        score += find_path_score(tab,i-1,j,value+1)
    if i+1 < len(tab):
        score += find_path_score(tab,i+1,j,value+1)
    if j-1 >= 0:
        score += find_path_score(tab,i,j-1,value+1)
    if j+1 < len(tab[i]):
        score += find_path_score(tab,i,j+1,value+1)
    return score

def part_2(fichier):
    score = 0
    tab = fichier_to_tab(fichier)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 0:
                score += find_path_score(tab,i,j,0)

    print("Part 2 :",score)
    return score
lecture_fichier("jour10/jour10.txt",part_2)
# Part 1 : 574 en 0.26 sec
# Part 2 : 1238 en 0.31 sec