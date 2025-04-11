#=|=# Jour 9 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaire sur l'exo      #=|=#
''' Sûrement optimisable avec une file '''

# ========= INITIALIZATION ========== #
EMPTY_VALUE = -1

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
        tab.extend(map(int,ligne))
    
    return tab

# ============= PART 1 ============= #
def get_disk_tab(tab):
    diskTab = []
    convertToSpace = False
    j = 0
    for i in range(len(tab)):
        if convertToSpace:
            for _ in range(tab[i]):
                diskTab.append(EMPTY_VALUE)
            convertToSpace = False
        else:
            for _ in range(tab[i]):
                diskTab.append(j)
            j += 1
            convertToSpace = True
    return diskTab

def reorganize_tab(tab):
    i,j = 0,len(tab)-1
    while i<j:
        if tab[i] == EMPTY_VALUE:
            tab[i] = tab[j]
            j -= 1
            while tab[j] == EMPTY_VALUE:
                j -= 1
        i += 1
    return tab[0:j+1]

def checksum(tab):
    checkSum = 0
    for i in range(len(tab)):
        if tab[i] == EMPTY_VALUE: #Pour la partie 2
            continue
        checkSum += i*tab[i]
    return checkSum

def part_1(fichier):
    tab = fichier_to_tab(fichier)

    diskTab = get_disk_tab(tab)
    diskTab = reorganize_tab(diskTab)
    result = checksum(diskTab)

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def find_group_before_index(tab,index):
    if index < 0:
        return None, 0, 0
    groupLength = 0
    groupValue = tab[index]
    while index >= 0 and tab[index] == groupValue:
        index -= 1
        groupLength += 1
    return groupValue,groupLength,index

def find_group_after_index(tab,index):
    if index >= len(tab):
        return None, 0, len(tab)
    groupLength = 0
    groupValue = tab[index]
    while index < len(tab) and tab[index] == groupValue:
        index += 1
        groupLength += 1
    return groupValue,groupLength,index

def reorganize_tab_group(tab):
    i,j = 0,len(tab)-1

    while j > 0:
        group1Value,group1Length,i1 = find_group_after_index(tab,i)
        group2Value,group2Length,j2 = find_group_before_index(tab,j)
        if group1Value == group2Value and group1Value != EMPTY_VALUE:
        # On est remonté jusqu'à l'ID cherchée <=> il n'existe pas de place
            j = j2
            i = 0
            continue
        if group2Value == EMPTY_VALUE: # On cherche des ID valides
            j = j2
            continue
        if group1Value != EMPTY_VALUE: # On cherche des espaces libres
            i = i1
            continue
        if group1Length < group2Length: # L'ID ne rentre pas
            i = i1
            continue

        for k in range(group2Length): # L'ID rentre, on permute le groupe
            tab[i+k] = group2Value
            tab[j-k] = EMPTY_VALUE
        i = 0
        j = j2
    return tab

def part_2(fichier):
    tab = fichier_to_tab(fichier)

    diskTab = get_disk_tab(tab)
    diskTab = reorganize_tab_group(diskTab)
    result = checksum(diskTab)

    print("Part 2 :",result)
    return result

lecture_fichier("jour9/jour9.txt",part_2)
# Part 1 : 6356833654075 en 0.25 sec
# Part 2 : 6389911791746 en 199 sec