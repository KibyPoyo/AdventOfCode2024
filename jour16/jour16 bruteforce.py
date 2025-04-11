#=|=# Jour 16 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Seulement la Part 1, avec un algo récursif assez lent '''

# ========= INITIALIZATION ========== #
import sys
import numpy as np

INFINITY = np.inf
EDGE = -1 # Ne doit pas être positif, ou bien positif "proche" de l'infini
END = -2 # Ne doit pas être positif, ou bien positif "proche" de l'infini
SIT = -3 # Part 2
sys.setrecursionlimit(5000)

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
        tab.append([char for char in ligne])
    
    return tab

# ============= PART 1 ============= #
def draw_tab(nomFichier,tab):
    with open(f"jour16/{nomFichier}.txt", "w") as txt:
        for row in tab:
            formattedRow = "".join(f"{x:>6}" for x in row)
            txt.write(formattedRow + '\n')

def format_tab(tab):
    newTab = [[0] * len(tab[0]) for _ in range(len(tab))]
    si,sj = None,None
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            match tab[i][j]:
                case '.':
                    newTab[i][j] = INFINITY
                case '#':
                    newTab[i][j] = EDGE
                case 'S':
                    newTab[i][j] = 0
                    si,sj = i,j
                case 'E':
                    newTab[i][j] = END
    return newTab,si,sj

def is_inside_tab(tab,i,j):
    return 0 <= i < len(tab) and 0 <= j < len(tab[0])

def shortest_path_finding_direction(tab,i,j,direction=None,score=0):
    if not is_inside_tab(tab,i,j):
        return INFINITY
    num = tab[i][j]
    if num == EDGE:
        return INFINITY
    if num == END:
        return score
    if num < score:
        return INFINITY
    
    tab[i][j] = score
    down = shortest_path_finding_direction(tab,i+1,j,'v',score+(1001 if direction == 'h' else 1))
    up = shortest_path_finding_direction(tab,i-1,j,'v',score+(1001 if direction == 'h' else 1))
    right = shortest_path_finding_direction(tab,i,j+1,'h',score+(1001 if direction == 'v' else 1))
    left = shortest_path_finding_direction(tab,i,j-1,'h',score+(1001 if direction == 'v' else 1))
    
    return min(down,up,right,left)


def part_1(fichier):
    tab = fichier_to_tab(fichier)
    tab,i,j = format_tab(tab)
    result = shortest_path_finding_direction(tab,i,j,'h',0)
    draw_tab("debug/pic",tab)

    print("Part 1 :",result)
    return result

lecture_fichier("jour16/ex.txt",part_1)
# Part 1 : 83432 en 22.8 sec


