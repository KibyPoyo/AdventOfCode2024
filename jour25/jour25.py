#=|=# Jour 25 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' J'ai pas accès à la partie 2 youhou '''

# ========= INITIALIZATION ========== #
PATTERN_MATCHING = [5,5,5,5,5]

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    tab = []
    pattern = []

    for line in fichier:
        line = line.strip()
        if line == '':
            tab.append(pattern)
            pattern = []
        else:
            pattern.append([char for char in line])

    if pattern != []:
        tab.append(pattern)
    
    return tab

# ============= PART 1 ============= #
def determine_pattern(patterns):
    keys = []
    locks = []
    for pattern in patterns:
        if pattern[0][0] == '#':
            locks.append(pattern)
        else:
            keys.append(pattern)
    return locks,keys

def get_heights(tab):
    heights = []
    for pattern in tab:
        subHeights = [-1] * len(tab[0][0])
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                if pattern[i][j] == '#':
                    subHeights[j] += 1
        heights.append(subHeights)
    return heights

def add_tab_content(baseTab,addTab):
    assert len(baseTab) == len(addTab), 'Tabs lengths'
    result = baseTab[:]
    for i in range(len(baseTab)):
        result[i] += addTab[i]
    return result

def is_pattern_matching(pattern1,pattern2,reference=PATTERN_MATCHING):
    assert len(pattern1) == len(pattern2) == len(reference), 'Tabs lengths'
    matchTab = add_tab_content(pattern1,pattern2)
    for i in range(len(matchTab)):
        if matchTab[i] > reference[i]:
            return False
    return True

def find_key_in_lock(locks,keys):
    matchs = []
    for lock in locks:
        for key in keys:
            if is_pattern_matching(lock,key):
                matchs.append((lock,key))
    return matchs

def part_1(fichier):
    tab = fichier_to_tab(fichier)
    locks,keys = determine_pattern(tab)
    locksHeights = get_heights(locks)
    keysHeights = get_heights(keys)
    matchs = find_key_in_lock(locksHeights,keysHeights)

    print("Part 1 :",len(matchs))

lecture_fichier("jour25/jour25.txt",part_1)
# Part 1 : 3107 en 0.35 sec