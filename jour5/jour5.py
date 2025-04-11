#=|=# Jour 5 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaire sur l'exo      #=|=#
''' VERSION ANCIENNE A REMPLACER '''

# ========= INITIALIZATION ========== #
def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tabs(fichier):
    tabRules = []
    tabVerifs = []
    for line in fichier:
        line = line.strip()
        if line == '':
            continue
        elif '|' in line:
            tabRules.append((int(line[0:2]),int(line[3:5])))
        else:
            row = [int(num) for num in line.split(',')]
            tabVerifs.append(row)

    return tabRules,tabVerifs

# ============= PART 1 ============= #
def find_middle(tab):
    if len(tab) == 0:
        return 0
    return tab[len(tab) // 2]

def is_valid_update(update,tabRules):
    for x, y in tabRules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def order_score_1(fichier):
    tabRules,tabUpdate = fichier_to_tabs(fichier)
    result = 0
    for update in tabUpdate:
        if is_valid_update(update, tabRules):
            result += find_middle(update)
    print(result)
    return result

# ============= PART 2 ============= #
from itertools import permutations

def get_permutations(tab):
    return [list(p) for p in permutations(tab)]

#Solution infinie en temps...
def order_score_2(fichier):
    tabRules,tabUpdate = fichier_to_tabs(fichier)
    result = 0
    for update in tabUpdate:
        for updateCombinaison in get_permutations(update):
            if is_valid_update(updateCombinaison, tabRules):
                result += find_middle(update)
                break
        print(f"Check {update.index()}/{len(tabUpdate)}")

    print(result)
    return result

lecture_fichier("jour5/jour5.txt",order_score_2)