#=|=# Jour 24 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' La partie 2 est omega dure, aucune idée de comment faire sans partir
sur du O(n!!!!) dégueulasse '''

# ========= INITIALIZATION ========== #
import re

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_data(fichier):
    known = {}
    operations = []
    
    for line in fichier:
        line = line.strip()
        if re.match(r"[xy][0-9]{2}:", line):  # Les valeurs de x ou y
            key, value = line.split(':')
            known[key.strip()] = int(value.strip())
        elif line == '':
            continue
        else:  # Les opérations logiques
            line = line.split()
            operations.append([line[0],line[1],line[2],line[4]])
    
    return known, operations
    
# ============= PART 1 ============= #
def apply_operator(num1,op,num2):
    match op:
        case 'OR':
            return num1 or num2
        case 'AND':
            return num1 and num2
        case 'XOR':
            return num1 ^ num2
        case _:
            return None

def get_z_number(dict):
    z = 0
    for key,value in dict.items():
        if key[0] == 'z' and value == 1:
            z += 2**int(key[1:3])
    return z

def part_1(fichier):
    known, operations = fichier_to_data(fichier)
    seenI = []

    while len(seenI) != len(operations):
        for i in range(len(operations)):
            if i in seenI:
                continue
            if operations[i][0] in known and operations[i][2] in known:
                known[operations[i][3]] = apply_operator(known[operations[i][0]],operations[i][1],known[operations[i][2]])
                seenI.append(i)
    
    result = get_z_number(known)

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def expected_z_number(dict):
    z = 0
    for key,value in dict.items():
        if key[0] == 'x' and value == 1:
            z += 2**int(key[1:3])
        elif key[0] == 'y' and value == 1:
            z += 2**int(key[1:3])
    return z

def is_correct_z(z,expectedZ):
    pass

def part_2(fichier):
    known, operations = fichier_to_data(fichier)
    seenI = []

    while len(seenI) != len(operations):
        for i in range(len(operations)):
            if i in seenI:
                continue
            if operations[i][0] in known and operations[i][2] in known:
                known[operations[i][3]] = apply_operator(known[operations[i][0]],operations[i][1],known[operations[i][2]])
                seenI.append(i)
    
    result = get_z_number(known)

    print("Part 2 :",result)
    return result


lecture_fichier("jour24/jour24.txt",part_1)