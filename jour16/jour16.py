#=|=# Jour 16 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Compliké mention dijkstra, inspiré d'internet car trop dur
la structure de l'algo est que chaque '.' est un noeud, et on trace les
arêtes du graphes en fonction de la direction (poids différent) 
Attention : le noeud d'arrivée pointe sur un noeud 'end' qui fait arrêter
la recherche (ce n'est pas le noeud final qui doit arrêter le programme)'''

# ========= INITIALIZATION ========== #
import networkx as nx
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

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
        tab.append([char for char in ligne])
    
    return tab

# ============= PART 1 ============= #
def generate_graph(fichier):
    tab = fichier_to_tab(fichier)
    graph = nx.DiGraph()
    start,end = None,None

    for i, line in enumerate(tab):
        for j, symbol in enumerate(line):
            if symbol == "#":
                continue
            node = (i, j)
            if symbol == "S":
                start = (node, (0, 1))  # Orienté vers la droite
            if symbol == "E":
                end = node
            for direction in DIRECTIONS:
                graph.add_node((node, direction))

    for node, direction in graph.nodes:
        i,j = node
        di,dj = direction
        if ((i+di,j+dj), direction) in graph.nodes:
            graph.add_edge(((i,j), direction), ((i+di,j+dj), direction), weight=1)
        for rotation in DIRECTIONS:
            graph.add_edge(((i,j), direction), ((i,j), rotation), weight=1000)

    for direction in DIRECTIONS:
        graph.add_edge((end, direction), "end", weight=0)

    return graph,start

def part_1(fichier):
    graph, start = generate_graph(fichier)
    result = nx.shortest_path_length(graph, start, "end", weight="weight")

    print("part 1 :",result)
    return result

# ============= PART 2 ============= #
def part_2(fichier):
    graph, start = generate_graph(fichier)
    paths = nx.all_shortest_paths(graph, start, "end", weight="weight")
    uniqueNodes = set()
    for path in paths:
        for node, _ in path[:-1]: # Le noeud 'end' génère une erreur
            uniqueNodes.add(node)
    result = len(uniqueNodes)
    print("Part 2 :",result)
    return result

lecture_fichier("jour16/jour16.txt",part_2)
# Part 1 : 83432 en 2.9 sec
# Part 2 : 467 en 3.2 sec
