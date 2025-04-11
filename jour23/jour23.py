#=|=# Jour 23 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Ultra satisfaisant avec NetworkX, implémentation vraiment clean '''

# ========= INITIALIZATION ========== #
import networkx as nx

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
        tab.append([line[0:2], line[3:5]])
    
    return tab

# ============= PART 1 ============= #
def generate_graph(fichier):
    tab = fichier_to_tab(fichier)
    graph = nx.Graph() # Graphe uni-directionnel

    for i in range(len(tab)):
        graph.add_node(tab[i][0])
        graph.add_node(tab[i][1])
        graph.add_edge(tab[i][0],tab[i][1])

    return graph

def part_1(fichier):
    graph = generate_graph(fichier)
    paths = set()

    for node in graph.nodes:
        if node[0] != 't':
            continue
        for target in graph.nodes:
            if node == target:
                continue
            if not graph.has_edge(node, target):
                continue
            for neighboor in nx.common_neighbors(graph,node,target):
                paths.add(tuple(sorted([node,neighboor,target])))

    #print(paths)
    print("Part 1 :",len(paths))
    return len(paths)

# ============= PART 2 ============= #
def is_complete_subgraph(graph, nodes):
    if nodes == None:
        return False
    subgraph = graph.subgraph(nodes)
    subgraphEdges = subgraph.number_of_edges()
    completeGraphEdges = (len(nodes) * (len(nodes) - 1)) // 2
    return subgraphEdges == completeGraphEdges

def part_2(fichier):
    graph = generate_graph(fichier)
    lan = None
    degree = 0

    for node in graph.nodes:
        for target in graph.nodes:
            if node == target:
                continue
            if not graph.has_edge(node, target): # Elimine la plupart des cas
                continue
            subgraphNodes = [node,target]
            for neighboor in nx.common_neighbors(graph,node,target):
                subgraphNodes.append(neighboor)
            if len(subgraphNodes) <= degree:
                continue
            if is_complete_subgraph(graph,subgraphNodes):
                degree = len(subgraphNodes)
                lan = ','.join(sorted(subgraphNodes))

    print("Degree :",degree)
    print("Part 2 :",lan)
    return lan

lecture_fichier("jour23/jour23.txt",part_1)
# Part 1 : 1215 en 1.24 sec
# Part 2 : bm,by,dv,ep,ia,ja,jb,ks,lv,ol,oy,uz,yt en 1.36 sec