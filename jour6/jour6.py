#=|=# Jour 6 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaire sur l'exo      #=|=#
''' Bien envie de factoriser le code parce que c'est pas très clean '''

# ========= INITIALIZATION ========== #
import time

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    tab = []
    for line in fichier:
        line = line.strip()
        tab.append(list(line))
    return tab

# ============= PART 1 ============= #
def find_start(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == '^':
                return i,j
    print("ERREUR - Comportement imprevu dans find_start")
    return -1,-1

def count_score(tab):
    score = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 'X':
                score += 1
    return score

def patrol(fichier):
    tab = fichier_to_tab(fichier)
    i,j = find_start(tab)
    direction = 'up'

    while 0 <= i < len(tab) and 0 <= j < len(tab[0]):
        tab[i][j] = 'X'

        if direction == 'up':
            if i == 0:
                break
            if tab[i-1][j] == '#':
                direction = 'right'
            else:
                i -= 1
        elif direction == 'down':
            if i == len(tab)-1:
                break
            if tab[i+1][j] == '#':
                direction = 'left'
            else:
                i += 1
        elif direction == 'right':
            if j == len(tab[i])-1:
                break
            if tab[i][j+1] == '#':
                direction = 'down'
            else:
                j += 1
        elif direction == 'left':
            if j == 0:
                break
            if tab[i][j-1] == '#':
                direction = 'up'
            else:
                j -= 1
        else:
            print(f"Wrong direction ({direction}), expected up down right left")
            break
    
    score = count_score(tab)
    print(score)
    return tab

# ============= PART 2 ============= #
def is_patrol_infinite(i, j, direction, tab):
    historique = set()

    while 0 <= i < len(tab) and 0 <= j < len(tab[0]):
        etat = (i, j, direction)
        if etat in historique:
            return 1
        historique.add(etat)

        if direction == 'up':
            if i == 0:
                break
            if tab[i-1][j] == '#':
                direction = 'right'
            else:
                i -= 1
        elif direction == 'down':
            if i == len(tab)-1:
                break
            if tab[i+1][j] == '#':
                direction = 'left'
            else:
                i += 1
        elif direction == 'right':
            if j == len(tab[i])-1:
                break
            if tab[i][j+1] == '#':
                direction = 'down'
            else:
                j += 1
        elif direction == 'left':
            if j == 0:
                break
            if tab[i][j-1] == '#':
                direction = 'up'
            else:
                j -= 1
        else:
            print(f"Wrong direction ({direction}), expected up down right left")
            break

    return 0

def guard_surronded_of_walls(tab,i,j):
    if i != 0 and j != 0 and i != len(tab) and j != len(tab[i]) \
    and tab[i+1][j] == '#' and tab[i-1][j] == '#' and tab[i][j+1] == '#' and tab[i][j] == '#':
        return True
    return False

# Execution sur le txt : 14 secondes
def patrol_blocking_guard(fichier):
    tab = fichier_to_tab(fichier)
    iStart,jStart = find_start(tab)
    fichier.seek(0)
    tab = patrol(fichier)
    result = 0

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == '#':
                continue
            if tab[i][j] == 'X':
                tab[i][j] = '#'
                if is_patrol_infinite(iStart,jStart,'up',tab):
                    result += 1
                tab[i][j] = '.'
    print("Part 2 result :",result)
    return result

# Execution sur le txt : 68 secondes
def patrol_blocking_guard_bruteforce(fichier):
    tab = fichier_to_tab(fichier)
    iStart,jStart = find_start(tab)
    result = 0

    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == '#':
                continue
            tab[i][j] = '#'
            if is_patrol_infinite(iStart,jStart,'up',tab):
                result += 1
            tab[i][j] = '.'

    print("Part 2 result :",result)
    return result

lecture_fichier("jour6/jour6.txt",patrol_blocking_guard)