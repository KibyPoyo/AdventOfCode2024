#=|=# Jour 22 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' BANANANA + SINJE = CASSAI SERVO '''

# ========= INITIALIZATION ========== #
from collections import Counter

SECRET_NUMBER_SEARCHED = 2000

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    return [int(line.strip()) for line in fichier]

# ============= PART 1 ============= #
def mix_and_prune(secret,value):
    secret ^= value
    secret %= 16777216
    return secret

def next_secret(secret):
    secret = mix_and_prune(secret, secret * 64)
    secret = mix_and_prune(secret, secret // 32)
    secret = mix_and_prune(secret, secret * 2048)
    return secret

def part_1(fichier):
    tab = fichier_to_tab(fichier)
    result = 0

    for num in tab:
        for _ in range(SECRET_NUMBER_SEARCHED):
            num = next_secret(num)
        result += num

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def get_prices_tab(tab):
    prices = []
    for num in tab:
        line = []
        for _ in range(SECRET_NUMBER_SEARCHED):
            num = next_secret(num)
            line.append(num%10)
        prices.append(line)
    return prices

def get_differences_tab(prices):
    diffrences = []
    for i in range(len(prices)):
        line = [0]
        for j in range(1,len(prices[i])):
            line.append(prices[i][j] - prices[i][j-1])
        diffrences.append(line)
    return diffrences

def bananas_score_dict(differences, prices):
    bananasDict = {}
    for i in range(len(differences)):
        currectDict = {}
        for j in range(1, len(differences[i]) - 4):
            sequence = tuple(differences[i][j:j+4])  # Convertir en tuple
            if sequence not in currectDict:
                currectDict[sequence] = prices[i][j+3]
        bananasDict = union_dict(bananasDict,currectDict)
    return bananasDict

def union_dict(dict1,dict2):
    return dict(Counter(dict1) + Counter(dict2))

def part_2(fichier):
    tab = fichier_to_tab(fichier)
    prices = get_prices_tab(tab)
    differences = get_differences_tab(prices)

    bananasDict = bananas_score_dict(differences, prices)

    bestSequence = max(bananasDict, key=bananasDict.get)
    maxBananas = bananasDict[bestSequence]

    print("Best Sequence :", bestSequence)
    print("Part 2 :", maxBananas)

lecture_fichier("jour22/jour22.txt",part_2)
# Part 1 : 13234715490 en 4 sec
# Part 1 : 1490 en 78 sec