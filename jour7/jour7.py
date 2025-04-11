#=|=# Jour 7 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaire sur l'exo      #=|=#
''' :) '''

# ========= INITIALIZATION ========== #
from itertools import product

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tabs(fichier):
    tabResults = []
    tabEquations = []
    for line in fichier:
        line = line.strip()
        line = line.split(':')
        tabResults.append(int(line[0]))
        
        equation = line[1].strip().split()
        tabEquations.append(list(map(int, equation)))
    return tabResults, tabEquations

# ============= PART 1 ============= #
def operators_possibilities_manual(lengthTab):
    length = lengthTab - 1 # Si il y a n nombre il y a n-1 opérateurs
    result = []
    tabPlus = ['+'] * length
    
    result.append(tabPlus)
    for i in range(length):
        base = tabPlus[:]
        for j in range(i,length):
            base[j] = '*'
            element = base[:]
            result.append(element)

    return result

def operators_possibilities(tabPossibilities,lengthNumbers):
    return product(tabPossibilities, repeat=lengthNumbers-1)

def evaluate_expression(expectedResult,numbers,operatorsPossibilities):
    for operators in operators_possibilities(operatorsPossibilities,len(numbers)):
        result = numbers[0]
        for i, operator in enumerate(operators):
            if operator == '+':
                result += numbers[i+1]
            elif operator == '*':
                result *= numbers[i+1]
            elif operator == '||': # PART 2
                length = len(str(numbers[i+1]))
                result = result * (10 ** length) + numbers[i+1]
            else:
                raise ValueError(f"Opérateur inconnu : {operator}")
        if result == expectedResult:
            return True
    return False

def part_1(fichier):
    tabResults,tabEquations = fichier_to_tabs(fichier)
    assert len(tabResults) == len(tabEquations)

    resultSum = 0
    for i in range(len(tabResults)):
        if evaluate_expression(tabResults[i],tabEquations[i],['+','*']):
            resultSum += tabResults[i]
    
    print("Part 1 :",resultSum)
        
# ============= PART 2 ============= #
def part_2(fichier):
    tabResults,tabEquations = fichier_to_tabs(fichier)
    assert len(tabResults) == len(tabEquations)

    resultSum = 0
    for i in range(len(tabResults)):
        if evaluate_expression(tabResults[i],tabEquations[i],['+','*','||']):
            resultSum += tabResults[i]
    
    print("Part 2 :",resultSum)

lecture_fichier("jour7/jour7.txt",part_1)