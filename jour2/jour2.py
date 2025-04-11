#=|=# Jour 2 de l'Advent of Code 2024 #=|=#

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
    
    for ligne in fichier:
        ligne = ligne.strip()
        nombres = ligne.split()
        tab.append(nombres)
    
    return tab

# ============= PART 1 ============= #
def safe(tab):
    result = 0
    direction = 0
    for report in tab:
        for i in range(len(report)-1):
            difference = int(report[i+1]) - int(report[i])
            if abs(difference) > 3:
                break
            if difference < 0:
                direction -= 1
            elif difference > 0:
                direction += 1
            else:
                break
        if abs(direction) == len(report)-1:
            result += 1
        direction = 0

    print(result)

    return result

# ============= PART 2 ============= #
def correct(tab):
    tabDifference = []
    for i in range(len(tab)):
        reportDifference = []
        for j in range(len(tab[i])-1):
            reportDifference.append(int(tab[i][j+1])-int(tab[i][j]))
        tabDifference.append(reportDifference)
    
    result = len(tab)
    for report in tabDifference:
        isIncreasing = 0
        for difference in report:
            if difference > 0:
                isIncreasing += 1
            else:
                isIncreasing -= 1
        
        print(report)
        tolerable = 1
        for i in range(len(report)):
            if abs(report[i]) > 3:
                tolerable -= 1
                if tolerable < 0:
                    result -= 1
                    break
                if i+1 < len(report):
                    report[i+1] += report[i]
            
            if (isIncreasing > 0 and report[i] <= 0) or (isIncreasing < 0 and report[i] >= 0):
                tolerable -= 1
                if tolerable < 0:
                    result -= 1
                    break
                if i+1 < len(report):
                    report[i+1] += report[i]

    print(result)

    return result


lecture_fichier("jour2/jour2.txt",correct)
#VALEUR A TROUVER POUR CORRECT : 404