#=|=# Jour 19 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' J'ai fais au pif c'était ça, on est au jour 3 ouuuuuu '''

# ========= INITIALIZATION ========== #
def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    lines = fichier.readlines()
    towels = lines[0].strip().split(', ')
    combinaisons = []
    for line in lines[2:]:
        combinaisons.append(line.strip())
    
    return towels,combinaisons

# ============= PART 1 ============= #
def find_valid_combinaisons(towels, combinaison, seen):
    if combinaison in seen:
        return seen[combinaison]

    for towel in towels:
        if combinaison.startswith(towel):
            cut = combinaison[len(towel):]

            if cut == '' or find_valid_combinaisons(towels, cut, seen):
                seen[combinaison] = 1
                return 1

    seen[combinaison] = 0 
    return 0

def part_1(fichier):
    towels,combinaisons = fichier_to_tab(fichier)
    result = 0
    seen = {}
    for combinaison in combinaisons:
        result += find_valid_combinaisons(towels,combinaison,seen)

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def find_all_combinaisons(towels, combinaison, seen):
    if combinaison in seen:
        return seen[combinaison]

    if combinaison == '':
        return 1
    
    possibilities = 0
    for towel in towels:
        if combinaison.startswith(towel):
            cut = combinaison[len(towel):]
            possibilities += find_all_combinaisons(towels, cut, seen)
    seen[combinaison] = possibilities
    return seen[combinaison]

def part_2(fichier):
    towels,combinaisons = fichier_to_tab(fichier)
    result = 0
    seen = {}
    for combinaison in combinaisons:
        result += find_all_combinaisons(towels,combinaison,seen)

    print("Part 2 :",result)
    return result

lecture_fichier("jour19/jour19.txt",part_1)
# Part 1 : 278 en 1.25 sec
# Part 2 : 569808947758890 en 2.28 sec