#=|=# Jour 18 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Dijkstra le retooooouuuur ! Exo pas trop fun même si y'a pire'''

# ========= INITIALIZATION ========== #
import networkx as nx
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

def lecture_fichier(fichier,fonction,dimensions,corruptedBytes):
    try:
        with open(fichier, "r") as txt:
            fonction(txt,dimensions,corruptedBytes)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

def fichier_to_tab(fichier, dimensions, corruptedBytes):
    tab = [['.'] * dimensions[1] for _ in range(dimensions[0])]
    
    for line in fichier:
        line = line.strip()
        line = line.split(',')
        j,i = map(int, line)  # axes x y retournés dans un tableau
        if 0 <= i < dimensions[0] and 0 <= j < dimensions[1]:
            tab[i][j] = '#'

        corruptedBytes -= 1
        if corruptedBytes <= 0:
            break
    
    return tab

# ============= PART 1 ============= #
def generate_graph(fichier,dimensions,corruptedBytes):
    tab = fichier_to_tab(fichier,dimensions,corruptedBytes)
    graph = nx.DiGraph()
    start,end = (0,0),(dimensions[0]-1,dimensions[1]-1)

    graph.add_node(start)
    graph.add_node(end)
    for i, line in enumerate(tab):
        for j, symbol in enumerate(line):
            if symbol == "#":
                continue
            graph.add_node((i,j))

    for node in graph.nodes:
        i,j = node
        for direction in DIRECTIONS:
            di,dj = direction
            if (i+di,j+dj) in graph.nodes:
                graph.add_edge((i,j),(i+di,j+dj), weight=1)

    return graph,start,end

def write_tab(fichier,dimensions,corruptedBytes):
    tab = fichier_to_tab(fichier,dimensions,corruptedBytes)
    with open(f"jour18/debug.txt", "w") as txt:
        for row in tab:
            txt.write("".join(row) + '\n')

def part_1(fichier,dimensions,corruptedBytes):
    graph, start, end = generate_graph(fichier,dimensions,corruptedBytes)
    try:
        result = nx.shortest_path_length(graph, start, end, weight="weight")
    except nx.exception.NetworkXNoPath:
        print(f"Pas de chemin valide pour {corruptedBytes}")
        return None

    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
def read_line(txt, num):
    txt.seek(0)
    for line in txt:
        if num != 0:
            num -= 1
            continue
        return line.strip()
    return None

def part_2(fichier,dimensions,corruptedBytesStart):
    corruptedBytes = corruptedBytesStart
    graph, start, end = generate_graph(fichier,dimensions,corruptedBytes)
    while True:
        line = read_line(fichier,corruptedBytes)
        j,i = map(int,line.split(','))
        graph.remove_node((i,j))
        try:
            result = nx.shortest_path_length(graph, start, end, weight="weight")
        except nx.exception.NetworkXNoPath:
            break
        corruptedBytes += 1

    print(f"Part 2 : {j},{i}")
    return result

lecture_fichier("jour18/jour18.txt",part_2,(71,71),1024) # attention dimensions 0 est compris (tab) -> +(1,1)
# Part 1 : 282 en 1.7 sec
# Part 2 : 64,29 en 20.6 sec [début à 1024]