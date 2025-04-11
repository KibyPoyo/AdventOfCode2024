#=|=# Jour 11 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' @functools.cache meilleure chose '''

# ========= INITIALIZATION ========== #
import functools

def lecture_fichier(fichier,fonction,userData):
    try:
        with open(fichier, "r") as txt:
            fonction(txt,userData)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    tab = []
    
    for ligne in fichier:
        ligne = ligne.strip()
        ligne = ligne.split()
        tab = [int(chiffre) for chiffre in ligne]
    
    return tab

# ============= PART 1 ============= #
def has_even_digit_count(n):
    digit_count = len(str(n))  # nb positif forcément ici
    return digit_count % 2 == 0

def brute_force_blink(fichier,nb):
    tab = fichier_to_tab(fichier)
    
    for i in range(nb):
        print(f"Operation {i} terminee !")
        blinkTab = []
        for stone in tab:
            if stone == 0:
                blinkTab.append(1)
            elif has_even_digit_count(stone):
                stoneString = str(stone)
                mid = len(stoneString) // 2
                blinkTab.append(int(stoneString[:mid]))
                blinkTab.append(int(stoneString[mid:]))
            else:
                blinkTab.append(stone*2024)
        tab = blinkTab

    result = len(blinkTab)
    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
@functools.cache
def recursive_blink(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return recursive_blink(1, n-1)
    
    stoneStr = str(stone)
    stoneLen = len(stoneStr)
    if stoneLen % 2 == 0:
        mid = stoneLen // 2
        left = int(stoneStr[:mid])
        right = int(stoneStr[mid:])
        return recursive_blink(left, n-1) + recursive_blink(right, n-1)

    return recursive_blink(stone*2024, n-1)

def smooth_blink(fichier,nb):
    tab = fichier_to_tab(fichier)

    result = 0
    for stone in tab:
        result += recursive_blink(stone, nb)
    print("Part 2 :",result)
    return result

lecture_fichier("jour11/jour11.txt",smooth_blink,25)
lecture_fichier("jour11/jour11.txt",smooth_blink,75)
# Part 1 : 204022 en 0.7 sec
# Part 2 : 241651071960597 1.2 sec