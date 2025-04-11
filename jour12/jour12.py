#=|=# Jour 12 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Compter les angles, ça ne me fait pas peur '''

# ========= INITIALIZATION ========== #
NEUTRAL_REGION = '.'
INTERMEDIATE_REGION = ':'

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
        tab.append([chiffre for chiffre in ligne])
    
    return tab

# ============= PART 1 ============= #
def is_inside_tab(tab,i,j):
    return 0 <= i < len(tab) and 0 <= j < len(tab[0])

def calculate_region(tab,i,j,letter): # -> (area,perimeter)
    if not is_inside_tab(tab,i,j):
        return 0,1
    if tab[i][j] == INTERMEDIATE_REGION:
        return 0,0
    if tab[i][j] != letter:
        return 0,1
    tab[i][j] = INTERMEDIATE_REGION
    subAreaUp,subPerimeterUp = calculate_region(tab,i-1,j,letter)
    subAreaDown,subPerimeterDown = calculate_region(tab,i+1,j,letter)
    subAreaLeft,subPerimeterLeft = calculate_region(tab,i,j-1,letter)
    subAreaRight,subPerimeterRight = calculate_region(tab,i,j+1,letter)
    area = 1+subAreaUp+subAreaDown+subAreaLeft+subAreaRight
    perimeter = subPerimeterUp+subPerimeterDown+subPerimeterLeft+subPerimeterRight
    return area,perimeter

def color_tab(tab,value,substitute):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == value:
                tab[i][j] = substitute
    return tab

def part_1(fichier):
    tab = fichier_to_tab(fichier)
    result = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            letter = tab[i][j]
            if letter != NEUTRAL_REGION:
                area,perimeter = calculate_region(tab,i,j,letter)
                tab = color_tab(tab,INTERMEDIATE_REGION,NEUTRAL_REGION)
                result += area*perimeter

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def get_region_positions(tab,i,j,letter,positions):
    if not is_inside_tab(tab,i,j):
        return 0
    if tab[i][j] == INTERMEDIATE_REGION:
        return 0
    if tab[i][j] != letter:
        return 0
    tab[i][j] = INTERMEDIATE_REGION
    positions.add((i,j))
    areaUp = get_region_positions(tab,i-1,j,letter,positions)
    areaDown = get_region_positions(tab,i+1,j,letter,positions)
    areaLeft = get_region_positions(tab,i,j-1,letter,positions)
    areaRight = get_region_positions(tab,i,j+1,letter,positions)
    return 1+areaUp+areaDown+areaLeft+areaRight

def calculate_sides_score(tab,sides):
    result = 0
    for i,j in sides:
        connections = 0
        up = False
        right = False
        down = False
        left = False
        if (i-1,j) in sides:
            up = True
            connections += 1
        if (i,j+1) in sides:
            right = True
            connections += 1
        if (i+1,j) in sides:
            down = True
            connections += 1
        if (i,j-1) in sides:
            left = True
            connections += 1
        
        match connections:
            case 0:
                result += 4
            case 1:
                result += 2
            case 2:
                if (up and down) or (left and right):
                    continue
                result += 1
                if down and right:
                    if tab[i+1][j+1] != INTERMEDIATE_REGION:
                        result += 1
                elif down and left:
                    if tab[i+1][j-1] != INTERMEDIATE_REGION:
                        result += 1
                elif up and right:
                    if tab[i-1][j+1] != INTERMEDIATE_REGION:
                        result += 1
                elif up and left:
                    if tab[i-1][j-1] != INTERMEDIATE_REGION:
                        result += 1
            case 3:
                if down and right:
                    if tab[i+1][j+1] != INTERMEDIATE_REGION:
                        result += 1
                if down and left:
                    if tab[i+1][j-1] != INTERMEDIATE_REGION:
                        result += 1
                if up and right:
                    if tab[i-1][j+1] != INTERMEDIATE_REGION:
                        result += 1
                if up and left:
                    if tab[i-1][j-1] != INTERMEDIATE_REGION:
                        result += 1  
            case 4:
                if tab[i+1][j+1] != INTERMEDIATE_REGION:
                    result += 1
                if tab[i+1][j-1] != INTERMEDIATE_REGION:
                    result += 1
                if tab[i-1][j+1] != INTERMEDIATE_REGION:
                    result += 1
                if tab[i-1][j-1] != INTERMEDIATE_REGION:
                    result += 1  

    return result

def part_2(fichier):
    tab = fichier_to_tab(fichier)
    result = 0
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            letter = tab[i][j]
            if letter != NEUTRAL_REGION:
                sides = set()
                area = get_region_positions(tab, i, j, letter, sides)  # Passer l'ensemble partagé
                sidePerimeter = calculate_sides_score(tab,sides)
                tab = color_tab(tab, INTERMEDIATE_REGION, NEUTRAL_REGION)
                result += sidePerimeter*area

    print("Part 2:", result)
    return result

lecture_fichier("jour12/jour12.txt",part_2)
# Part 1 : 1533024 en 1.5 sec
# Part 2 : 910066 en 1.5 sec