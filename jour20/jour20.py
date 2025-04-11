#=|=# Jour 20 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Dijkstra c'est bien mais là ça fait beaucoup
Abandonné la partie 2 trop difficile, qui est une généralisation de la partie 1'''

# ========= INITIALIZATION ========== #
import networkx as nx
from copy import deepcopy
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
CHEAT_TIME_WORTH_IT = 100

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier):
    fichier.seek(0)
    tab = []
    
    for ligne in fichier:
        ligne = ligne.strip()
        tab.append([char for char in ligne])
    
    return tab

# ============= PART 1 ============= #
def generate_graph(fichier):
    tab = fichier_to_tab(fichier)
    graph = nx.Graph() # Graphe uni-directionnel
    start,end = None,None

    for i, line in enumerate(tab):
        for j, symbol in enumerate(line):
            if symbol == "#":
                continue
            if symbol == "S":
                start = (i,j)
            if symbol == "E":
                end = (i,j)
            graph.add_node((i,j))

    for node in graph.nodes:
        i,j = node
        for direction in DIRECTIONS:
            di,dj = direction
            if (i+di,j+dj) in graph.nodes:
                graph.add_edge((i,j),(i+di,j+dj), weight=1)

    graph.add_node(start)
    graph.add_node(end)

    return graph,start,end

def part_1(fichier):
    graph, start, end = generate_graph(fichier)
    legitTime = nx.shortest_path_length(graph, start, end, weight="weight")

    tab = fichier_to_tab(fichier)
    cheatTime = legitTime
    result = 0
    for i in range(1,len(tab)-1): # On ne prends pas les bords + di et dj sont dans le tableau ci-après
        for j in range(1,len(tab[0])-1):
            if tab[i][j] == '#':
                # Ajout du cheat
                graph.add_node((i,j))
                for direction in DIRECTIONS:
                    di,dj = direction
                    if (i+di,j+dj) in graph.nodes:
                        graph.add_edge((i,j),(i+di,j+dj), weight=1)

                # Calcul du chemin avec le cheat
                cheatTime = nx.shortest_path_length(graph, start, end, weight="weight")
                if legitTime >= cheatTime + CHEAT_TIME_WORTH_IT:
                    result += 1

                # Retrait du cheat pour la prochaine boucle
                for direction in DIRECTIONS:
                    di,dj = direction
                    if (i+di,j+dj) in graph.nodes:
                        graph.remove_edge((i,j),(i+di,j+dj))
                graph.remove_node((i,j))
        print(f"Ligne {i} faite, result actuel : {result}")

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
CHEAT_DURATION = 20 # 2 pour la part1 et 20 pour la part2

def create_hole(graph,position,length):
    pass

def part_2(fichier):
    graph, start, end = generate_graph(fichier)
    legitTime = nx.shortest_path_length(graph, start, end, weight="weight")

    tab = fichier_to_tab(fichier)
    cheatTime = legitTime
    result = 0
    for i in range(1,len(tab)-1): # On ne prends pas les bords + di et dj sont dans le tableau ci-après
        for j in range(1,len(tab[0])-1):
            if tab[i][j] == '#':
                cheatGraph = deepcopy(graph)
                # Ajout du cheat
                create_hole(cheatGraph,(i,j),CHEAT_DURATION)

                # Calcul du chemin avec le cheat
                cheatTime = nx.shortest_path_length(cheatGraph, start, end, weight="weight")
                if legitTime >= cheatTime + CHEAT_TIME_WORTH_IT:
                    result += 1
        print(f"Ligne {i} faite, result actuel : {result}")

    print("Part 2 :",result)
    return result

lecture_fichier("jour20/jour20.txt",part_2)
# Part 1 : 1490 en 327 sec
# Part 2 : XXX en XXX sec