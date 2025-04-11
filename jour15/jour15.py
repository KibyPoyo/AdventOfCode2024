#=|=# Jour 15 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Surement factorisable + optimisable pour la partie 2
car je fais 20000 copies de la grille = pas ouf, il faudrait vérifier 
si le déplacement est possible avant de le faire '''

# ========= INITIALIZATION ========== #
import copy

EMPTY_SYMBOL = '.'
ROBOT_SYMBOL = '@'
BOX_SYMBOL_SIMPLE = 'O'
BOX_SYMBOL_1 = '['
BOX_SYMBOL_2 = ']'
EDGE_SYMBOL = '#'

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tabs(fichier):
    scene = []
    movements = []
    
    for line in fichier:
        line = line.strip()
        if not line:
            continue
        elif line[0] == EDGE_SYMBOL:
            scene.append([chiffre for chiffre in line])
        else:
            for movement in line:
                movements.append(movement)
    
    return scene,movements

# ============= PART 1 ============= #
def search_robot(scene):
    for i in range(len(scene)):
        for j in range(len(scene[0])):
            if scene[i][j] == ROBOT_SYMBOL:
                return i,j
    return None

def get_direction(char):
    match char:
        case '^':
            return (-1,0)
        case 'v':
            return (1,0)
        case '<':
            return (0,-1)
        case '>':
            return (0,1)
        case _:
            return (0,0)

def scene_score(scene,symbol):
    score = 0
    for i in range(len(scene)):
        for j in range(len(scene[0])):
            if scene[i][j] == symbol:
                score += i*100 + j
    return score

def draw_scene(nomFichier,scene):
    with open(f"jour15/{nomFichier}.txt", "w") as txt:
        for row in scene:
            txt.write("".join(row) + '\n')

def part_1(fichier):
    scene,movements = fichier_to_tabs(fichier)
    iRobot,jRobot = search_robot(scene)
    draw_scene("before",scene)

    for k in range(len(movements)):
        i,j = get_direction(movements[k])
        nextSymbol = scene[iRobot+i][jRobot+j]
        if nextSymbol == EDGE_SYMBOL:
            continue
        elif nextSymbol == EMPTY_SYMBOL:
            scene[iRobot][jRobot] = EMPTY_SYMBOL
            scene[iRobot+i][jRobot+j] = ROBOT_SYMBOL
        elif nextSymbol == BOX_SYMBOL_SIMPLE:
            coef = 1
            while nextSymbol == BOX_SYMBOL_SIMPLE:
                coef += 1
                nextSymbol = scene[iRobot+(i*coef)][jRobot+(j*coef)]
            if nextSymbol == EDGE_SYMBOL:
                continue
            else: # nextSymbol == EMPTY_SYMBOL
                scene[iRobot][jRobot] = EMPTY_SYMBOL
                scene[iRobot+i][jRobot+j] = ROBOT_SYMBOL
                scene[iRobot+(i*coef)][jRobot+(j*coef)] = BOX_SYMBOL_SIMPLE
        iRobot,jRobot = iRobot+i,jRobot+j
    
    draw_scene("after",scene)

    result = scene_score(scene,BOX_SYMBOL_SIMPLE)
    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def switch_symbol(scene,pos1,symbol1,pos2,symbol2):
    i1,j1 = pos1
    i2,j2 = pos2
    scene[i1][j1] = symbol2
    scene[i2][j2] = symbol1
    return scene

def go_horizontal(scene,position,dj):
    i,j = position
    lastSymbol = scene[i][j]
    scene[i][j] = EMPTY_SYMBOL
    coef = 1
    while lastSymbol != EMPTY_SYMBOL:
        nextSymbol = scene[i][j+(coef*dj)]
        if nextSymbol == EDGE_SYMBOL:
            return False
        scene[i][j+(coef*dj)] = lastSymbol
        lastSymbol = nextSymbol
        coef += 1
    return True

def go_vertical(scene,position,di):
    i,j = position
    currentSymbol = scene[i][j]
    nextSymbol = scene[i+di][j]

    if nextSymbol == EDGE_SYMBOL:
        return False
    if nextSymbol == EMPTY_SYMBOL:
        switch_symbol(scene,(i,j),currentSymbol,(i+di,j),nextSymbol)
        return True

    if nextSymbol == currentSymbol:
        if not go_vertical(scene,(i+di,j),di):
            return False
    elif nextSymbol == BOX_SYMBOL_1:
        if not go_vertical(scene,(i+di,j),di) or not go_vertical(scene,(i+di,j+1),di):
            return False
    elif nextSymbol == BOX_SYMBOL_2:
        if not go_vertical(scene,(i+di,j),di) or not go_vertical(scene,(i+di,j-1),di):
            return False
    # nextSymbol a change pendant le parcours, on le recalcule
    switch_symbol(scene,(i,j),currentSymbol,(i+di,j),scene[i+di][j])
    return True

def translate_scene(scene):
    newScene = []
    for i in range(len(scene)):
        line = []
        for j in range(len(scene[0])):
            if scene[i][j] == EDGE_SYMBOL:
                line.append(EDGE_SYMBOL)
                line.append(EDGE_SYMBOL)
            elif scene[i][j] == BOX_SYMBOL_SIMPLE:
                line.append(BOX_SYMBOL_1)
                line.append(BOX_SYMBOL_2)
            elif scene[i][j] == EMPTY_SYMBOL:
                line.append(EMPTY_SYMBOL)
                line.append(EMPTY_SYMBOL)
            elif scene[i][j] == ROBOT_SYMBOL:
                line.append(ROBOT_SYMBOL)
                line.append(EMPTY_SYMBOL)
        newScene.append(line)
    return newScene

def part_2(fichier):
    scene,movements = fichier_to_tabs(fichier)
    scene = translate_scene(scene)
    i,j = search_robot(scene)

    draw_scene("begin",scene)
    for k in range(len(movements)):
        isMovementPossible = False
        di,dj = get_direction(movements[k])
        nextScene = copy.deepcopy(scene)
        match movements[k]:
            case '^' | 'v':
                if go_vertical(nextScene,(i,j),di):
                    isMovementPossible = True
            case '<' | '>':
                if go_horizontal(nextScene,(i,j),dj):
                    isMovementPossible = True
        if isMovementPossible:
            scene = nextScene
            i,j = i+di,j+dj
    draw_scene("after",scene)

    result = scene_score(scene,BOX_SYMBOL_1)
    print("Part 2 :",result)
    return result

lecture_fichier("jour15/jour15.txt",part_2)
# Part 1 : 1514353 en 0.29 sec
# Part 2 : 1533076 en 60 sec