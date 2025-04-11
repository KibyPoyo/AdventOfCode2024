# =|= Jour 13 de l'Advent of Code 2024 =|=

# ========= INITIALIZATION ========== #
import re
import numpy as np

def lecture_fichier(fichier, fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt.read())
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"
    occurrences = re.findall(pattern, fichier)

    result = []
    for occ in occurrences:
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = map(int, occ)
        result.append([button_a_x, button_a_y,button_b_x,button_b_y,prize_x,prize_y])

    return result

# ============= PART 1 ============= #
def solve_system(ax,ay,bx,by,rx,ry):
    return np.linalg.solve([[ax, bx], [ay, by]], [rx, ry])

def part_1(contenu):
    tab = fichier_to_tab(contenu)
    result = 0
    for ax,ay,bx,by,rx,ry in tab:
        x,y = solve_system(ax,ay,bx,by,rx,ry)
        x,y = round(x),round(y)
        if x*ax + y*bx == rx and x*ay + y*by == ry: #Equation valide
            result += x*3+y*1
        
    print("Part 1:", result)

# ============= PART 2 ============= #
def part_2(contenu):
    tab = fichier_to_tab(contenu)
    result = 0
    for ax,ay,bx,by,rx,ry in tab:
        rx,ry = rx+10000000000000,ry+10000000000000
        x,y = solve_system(ax,ay,bx,by,rx,ry)
        x,y = round(x),round(y)
        if x*ax + y*bx == rx and x*ay + y*by == ry: #Equation valide
            result += x*3+y*1
        
    print("Part 2:", result)

lecture_fichier("jour13/jour13.txt", part_2)
# Part 1 : 38839 en 0.9 sec
# Part 2 : 75200131617108 en 0.7 sec