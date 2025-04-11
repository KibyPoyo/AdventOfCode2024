#=|=# Jour 8 de l'Advent of Code 2024 #=|=#

# ========= INITIALIZATION ========== #
from collections import defaultdict

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
        tab.append(list(ligne))
    
    return tab

# ============= PART 1 ============= #
def find_antennas(tab):
    antennas = defaultdict(list)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != '.':
                antennas[tab[i][j]].append((i, j))
    return antennas

def find_antinodes_positions(pos1,pos2):
    diff = (pos2[0] - pos1[0],pos2[1] - pos1[1])
    return (pos1[0]-diff[0],pos1[1]-diff[1]),(pos2[0]+diff[0],pos2[1]+diff[1])

def is_inside_tab(tab,i,j):
    return 0 <= i < len(tab) and 0 <= j < len(tab[0])

def part_1(fichier):
    tab = fichier_to_tab(fichier)

    antennas = find_antennas(tab)
    antinodes = set()
    for _,positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                pos1,pos2 = find_antinodes_positions(positions[i],positions[j])
                antinodes.add(pos1)
                antinodes.add(pos2)
    
    result = 0
    for antinode in antinodes:
        if is_inside_tab(tab,antinode[0],antinode[1]):
            result += 1

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def find_antinodes_positions_in_line(tab,pos1,pos2):
    diff = (pos2[0] - pos1[0],pos2[1] - pos1[1])
    antinodes = set()
    coef = 0
    while True:
        antinode = (pos1[0]-coef*diff[0],pos1[1]-coef*diff[1])
        if not is_inside_tab(tab,pos1[0]-coef*diff[0],pos1[1]-coef*diff[1]):
            break
        antinodes.add(antinode)
        coef += 1
    coef = 0
    while True:
        antinode = (pos2[0]+coef*diff[0],pos2[1]+coef*diff[1])
        if not is_inside_tab(tab,antinode[0],antinode[1]):
            break
        antinodes.add(antinode)
        coef += 1
    print(antinodes)
    return antinodes

def part_2(fichier):
    tab = fichier_to_tab(fichier)

    antennas = find_antennas(tab)
    antinodes = set()
    for _,positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i+1, len(positions)):
                newAntinodes = find_antinodes_positions_in_line(tab,positions[i],positions[j])
                for newAntinode in newAntinodes:
                    antinodes.add(newAntinode)
    
    result = len(antinodes)

    print("Part 2 :",result)
    return result

lecture_fichier("jour8/jour8.txt",part_2)