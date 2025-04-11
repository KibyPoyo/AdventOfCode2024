#=|=# Jour 14 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Long et dur - Titre '''

# ========= INITIALIZATION ========== #
import re

NEIGHBOORS_POSITIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
INTERESSANT_LEVEL = 500 # ATTENTION A NE PAS METTRE LA VALEUR TROP BASSE (sinon ca peut generer enormement d'images)
STUDY_RANGE = 10000

def lecture_fichier(fichier,fonction,userData):
    try:
        with open(fichier, "r") as txt:
            fonction(txt,userData)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
    occurrences = re.findall(pattern, fichier.read())

    result = []
    for occ in occurrences:
        px,py,vx,vy = map(int, occ)
        result.append([px,py,vx,vy])

    return result

# ============= PART 1 ============= #
def quadrant_score(tab):
    q1,q2,q3,q4 = 0,0,0,0
    for i in range(0,len(tab)//2):
        for j in range(0,len(tab[0])//2):
            q1 += tab[i][j]
        for j in range(1+(len(tab[0])//2),len(tab[0])):
            q2 += tab[i][j]
    for i in range(1+(len(tab)//2),len(tab)):
        for j in range(0,len(tab[0])//2):
            q3 += tab[i][j]
        for j in range(1+(len(tab[0])//2),len(tab[0])):
            q4 += tab[i][j]
    print(q1,q2,q3,q4)
    return q1*q2*q3*q4

def part_1(fichier,dimentions):
    infos = fichier_to_tab(fichier)
    wide,tall = dimentions
    tab = [[0 for _ in range(wide)] for _ in range(tall)]

    for px,py,vx,vy in infos:
        px = (px+vx*100) % wide
        py = (py+vy*100) % tall
        tab[py][px] += 1

    result = quadrant_score(tab)
    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def draw_tab(nomFichier,tab):
    with open(f"jour14/{nomFichier}.txt", "w") as picture:
        for row in tab:
            picture.write("".join('#' if cell != 0 else '.' for cell in row) + "\n")

def get_robot_positions(tab):
    positions = set()
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] != 0:
                positions.add((i,j))
    return positions

def is_interessant_picture(positions):
    score = 0
    for x, y in positions:
        for dx,dy in NEIGHBOORS_POSITIONS:
            if (x+dx, y+dy) in positions:
                score += 1
    if score > INTERESSANT_LEVEL:
        print(score)
    return score > INTERESSANT_LEVEL

def clear_tab(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab[i][j] = 0
    return tab

def part_2(fichier,dimentions):
    infos = fichier_to_tab(fichier)
    wide,tall = dimentions
    tab = [[0 for _ in range(wide)] for _ in range(tall)]
    result = 0

    for i in range(STUDY_RANGE):
        for j in range(len(infos)): # Bouge les robots
            px,py,vx,vy = infos[j]
            px = (px+vx) % wide
            py = (py+vy) % tall
            tab[py][px] += 1
            infos[j] = [px,py,vx,vy]
        if is_interessant_picture(get_robot_positions(tab)):
            draw_tab("pic"+str(i+1),tab) # Il faut verifier l'image generee
        tab = clear_tab(tab)

    return result

lecture_fichier("jour14/jour14.txt",part_2,(101,103))
# Part 1 : 221142636 en 0.43 sec
# Part 1 : 7916 en 30 sec