#=|=# Jour 21 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Stylé mais qu'est-ce que c'est galère '''

# ========= INITIALIZATION ========== #
import functools

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
        tab.append([char for char in line])
    
    return tab

# ============= PART 1 ============= #
numeric_keyboard = {
    'A': (3,2),
    '0': (3,1),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '7': (0,0),
    '8': (0,1),
    '9': (0,2)
}

digital_keyboard_from_char = {
    'A': (0,2),
    '^': (0,1),
    '<': (1,0),
    'v': (1,1),
    '>': (1,2)
}

digital_keyboard_from_coord = {
    (0,2) : 'A',
    (0,1) : '^',
    (1,0) : '<',
    (1,1) : 'v',
    (1,2) : '>'
}

digital_paths = {
    ('A', 'A'): ['A'],
    ('^', '^'): ['A'],
    ('>', '>'): ['A'],
    ('<', '<'): ['A'],
    ('v', 'v'): ['A'],

    ('A', '<'): ['v', '<', '<', 'A'],    # De 'A' à '<'
    ('A', '>'): ['v', 'A'],              # De 'A' à '>'
    ('A', '^'): ['<', 'A'],              # De 'A' à '^'
    ('A', 'v'): ['v', '<', 'A'],         # De 'A' à 'v'

    ('^', '<'): ['v', '<', 'A'],         # De '^' à '<'
    ('^', '>'): ['v', '>', 'A'],         # De '^' à '>'
    ('^', 'A'): ['>', 'A'],              # De '^' à 'A'
    ('^', 'v'): ['v', 'A'],              # De '^' à 'v'

    ('<', 'A'): ['>', '>', '^', 'A'],    # De '<' à 'A'
    ('<', '^'): ['>', '^', 'A'],         # De '<' à '^'
    ('<', '>'): ['>', '>', 'A'],         # De '<' à '>'
    ('<', 'v'): ['>', 'A'],              # De '<' à 'v'

    ('>', 'A'): ['^', 'A'],              # De '>' à 'A'
    ('>', '^'): ['<', '^', 'A'],         # De '>' à '^'
    ('>', '<'): ['<', '<', 'A'],         # De '>' à '<'
    ('>', 'v'): ['<', 'A'],              # De '>' à 'v'

    ('v', 'A'): ['>', '^', 'A'],         # De 'v' à 'A'
    ('v', '^'): ['^', 'A'],              # De 'v' à '^'
    ('v', '<'): ['<', 'A'],              # De 'v' à '<'
    ('v', '>'): ['>', 'A']               # De 'v' à '>'
}

move = {
    'A': (0,0),
    '^': (-1,0),
    'v': (1,0),
    '<': (0,-1),
    '>': (0,1)
}

@functools.cache
def optimized_path_numeric(start,target):
    i,j = start
    ti,tj = target
    path = []
    while (i,j) != (ti,tj):
        if tj < j:
            if (i == 3) and (tj == 0):    # Bouton manquant
                path.extend(['^'] * (i - ti))
                i = ti
            else:
                path.append('<')
                j -= 1
        elif ti < i:
            path.append('^')
            i -= 1
        elif ti > i:
            if (j == 0) and (ti == 3):    # if would move to missing button
                path.extend(['>'] * (tj - j))   # move right instead
                j = tj
            else:
                path.append('v')   # move down
                i += 1
        elif tj > j:        # lowest priority is right
            path.append('>')
            j += 1
    path.append('A')
    return path

def get_numeric_path(tab):
    i,j = numeric_keyboard['A']
    result = []
    for k in range(len(tab)):
        ti,tj = numeric_keyboard[tab[k]]
        step = optimized_path_numeric((i,j),(ti,tj))
        for deplacement in step:
            result.append(deplacement)
            di,dj = move[deplacement]
            i,j = (i+di,j+dj)
    return result

def get_digital_path(tab):
    i,j = digital_keyboard_from_char['A']
    result = []
    for k in range(len(tab)):
        step = digital_paths[(digital_keyboard_from_coord[(i,j)],tab[k])]
        for deplacement in step:
            result.append(deplacement)
            di,dj = move[deplacement]
            i,j = (i+di,j+dj)

    return result

def tab_to_string(tab):
    return ''.join(tab)

def get_complexity(line,path):
    print(f"{int(line[0])*100 + int(line[1])*10 + int(line[2])} * {len(path)}")
    return (int(line[0])*100 + int(line[1])*10 + int(line[2])) * len(path)


def part_1(fichier):
    tab = fichier_to_tab(fichier)
    result = 0
    for line in tab:
        numericPath = get_numeric_path(line)
        digitalPath = get_digital_path(numericPath)
        finalPath = get_digital_path(digitalPath)
        print(tab_to_string(finalPath))
        print(tab_to_string(digitalPath))
        print(tab_to_string(numericPath))
        print(tab_to_string(line))
        result += get_complexity(line,finalPath)
        print(result)
        print()

    print("Part 1 :",result)

# ============= PART 2 ============= #
ROBOT_NUMBER = 25

def part_2(fichier):
    tab = fichier_to_tab(fichier)
    result = 0
    for line in tab:
        path = get_numeric_path(line)
        for i in range(ROBOT_NUMBER):
            path = get_digital_path(path)
            print(f"Etape {i} terminee")
        result += get_complexity(line,path)

    print("Part 2 :",result)

lecture_fichier("jour21/jour21.txt",part_2)