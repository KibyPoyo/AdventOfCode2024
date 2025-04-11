#=|=# Jour 4 de l'Advent of Code 2024 #=|=#

# ========= INITIALIZATION ========== #
def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            tab = fichier_to_tab(txt)
            fonction(tab)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    tab = []
    
    for line in fichier:
        line = line.strip()
        tab.append(list(line))

    return tab

# ============= PART 1 ============= #
def find_xmas(tab):
    result = 0
    tabHeight = len(tab)
    tabLength = len(tab[0])
    for i in range(tabHeight):
        for j in range(tabLength):
            if tab[i][j] == 'X':
                #Vérification des dimentions
                up = i+3 < tabHeight
                down = i-3 >= 0
                right = j+3 < tabLength
                left = j-3 >= 0

                #Check des XMAS dans toutes les directions
                if (up and tab[i+1][j] == 'M' and tab[i+2][j] == 'A' and tab[i+3][j] == 'S'):
                    result += 1 #Haut
                if (down and tab[i-1][j] == 'M' and tab[i-2][j] == 'A' and tab[i-3][j] == 'S'):
                    result += 1 #Bas
                if (right and tab[i][j+1] == 'M' and tab[i][j+2] == 'A' and tab[i][j+3] == 'S'):
                    result += 1 #Droite
                if (left and tab[i][j-1] == 'M' and tab[i][j-2] == 'A' and tab[i][j-3] == 'S'):
                    result += 1 #Gauche

                if (up and right and tab[i+1][j+1] == 'M' and tab[i+2][j+2] == 'A' and tab[i+3][j+3] == 'S'):
                    result += 1 #Diag Haut-Droite
                if (up and left and tab[i+1][j-1] == 'M' and tab[i+2][j-2] == 'A' and tab[i+3][j-3] == 'S'):
                    result += 1 #Diag Haut-Gauche
                if (down and right and tab[i-1][j+1] == 'M' and tab[i-2][j+2] == 'A' and tab[i-3][j+3] == 'S'):
                    result += 1 #Diag Bas-Droite
                if (down and left and tab[i-1][j-1] == 'M' and tab[i-2][j-2] == 'A' and tab[i-3][j-3] == 'S'):
                    result += 1 #Diag Bas-Gauche

    print(result)

    return result       

# ============= PART 2 ============= #
def find_mas_in_cross(tab):
    result = 0
    tabHeight = len(tab)
    tabLength = len(tab[0])
    for i in range(1,tabHeight-1):
        for j in range(1,tabLength-1):
            if tab[i][j] == 'A':
                #Check des MAS en croix dans toutes les directions
                countM = 0
                countS = 0

                if tab[i+1][j+1] == 'M':
                    countM += 1
                elif tab[i+1][j+1] == 'S':
                    countS += 1
                
                if tab[i+1][j-1] == 'M':
                    countM += 1
                elif tab[i+1][j-1] == 'S':
                    countS += 1
                
                if tab[i-1][j+1] == 'M':
                    countM += 1
                elif tab[i-1][j+1] == 'S':
                    countS += 1
                
                if tab[i-1][j-1] == 'M':
                    countM += 1
                elif tab[i-1][j-1] == 'S':
                    countS += 1

                if countM == 2 and countS == 2 and tab[i-1][j-1] != tab[i+1][j+1]:
                    result += 1

    print(result)

    return result       

lecture_fichier("jour4/jour4.txt",find_mas_in_cross)