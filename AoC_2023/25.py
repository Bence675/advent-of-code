

import copy
import scipy
import tqdm
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

def read_input():
    file = open("25.txt", "r")
    data = file.read().split("\n")
    nodes = {}
    for i in range(len(data)):
        x = data[i].split(": ")
        nodes[x[0]] = []
        for j in x[1].split(" "):
            nodes[j] = []

    for i in range(len(data)):
        x = data[i].split(": ")
        for j in x[1].split(" "):
            nodes[x[0]].append(j)
            nodes[j].append(x[0])

    edges = set()
    for i in nodes:
        for j in nodes[i]:
            edges.add((i, j))

    return nodes, edges

def is_graph_in_one_part(nodes, edges, edge_to_remove):
    # remove the edges
    edges = edges - set(edge_to_remove)
    # remove the nodes
    for i in edge_to_remove:
        nodes[i[0]].remove(i[1])
        nodes[i[1]].remove(i[0])

    visited = set()
    stack = [list(nodes.keys())[0]]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        stack += nodes[node]

    return len(visited) == len(nodes)

def shortest_path_between_two_nodes(nodes, start, end):
    visited = set()
    stack = [(start, [])]
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return path
        for i in nodes[node]:
            stack.append((i, path + [(node, i)]))

    return None

def remove_edge_from_nodes(nodes, edges, edge):
    res = {}
    for node1 in nodes:
        for node2 in nodes[node1]:
            if (node1, node2) == edge or (node2, node1) == edge:
                continue
            if node1 not in res:
                res[node1] = []
            res[node1].append(node2)

    return res

def reconstruct_path(predecessors, start, end):
    path = []
    node = end
    while node != start:
        path.append((predecessors[node][start], node))
        node = predecessors[node][start]
        if predecessors[node][start] == node:
            path.append((node, start))
            break
        

    return path

def to_scipy_graph(nodes, edges):
    res = np.zeros((len(nodes), len(nodes)))
    node_keys = list(nodes.keys())
    for edge in edges:
        ind1, ind2 = node_keys.index(edge[0]), node_keys.index(edge[1])
        if ind1 < ind2:
            res[ind1][ind2] = 1
        if ind2 < ind1:
            res[ind2][ind1] = 1

    return res

def from_scipy_graph(graph, nodes):
    new_nodes = {}
    new_edges = set()
    for i in range(graph.shape[0]):
        node_name1 = list(nodes.keys())[i]
        if node_name1 not in new_nodes:
            new_nodes[node_name1] = []
        for j in range(graph.shape[1]):
            node_name2 = list(nodes.keys())[j]
            if node_name2 not in new_nodes:
                new_nodes[node_name2] = []
            if graph[i][j] == 1:
                new_nodes[node_name1].append(node_name2)
                new_nodes[node_name2].append(node_name1)
                new_edges.add((node_name1, node_name2))
                new_edges.add((node_name2, node_name1))

    return new_nodes, new_edges

def part1():
    nodes, edges = read_input()
    for node in nodes:
        print(node, nodes[node])

    print()
    print(edges)
    

    edges.remove(("vfx", "bgl"))
    edges.remove(("bgl", "vfx"))

    edges.remove(("qxr", "btp"))
    edges.remove(("btp", "qxr"))

    edges.remove(("rxt", "bqq"))
    edges.remove(("bqq", "rxt"))

    nodes["vfx"].remove("bgl")
    nodes["bgl"].remove("vfx")

    nodes["qxr"].remove("btp")
    nodes["btp"].remove("qxr")

    nodes["rxt"].remove("bqq")
    nodes["bqq"].remove("rxt")

    """
    G = nx.Graph()
    for node in nodes:
        G.add_node(node)

    for edge in edges:
        G.add_edge(edge[0], edge[1])

    # plot the graph
    nx.draw(G, with_labels=True)
    plt.show()
    """

    counter1 = 0
    current = list(nodes.keys())[0]

    visitied = set()
    stack = [current]
    while stack:
        node = stack.pop()
        if node in visitied:
            continue
        visitied.add(node)
        stack += nodes[node]
        counter1 += 1

    counter2 = 0
    current = list(nodes.keys())[1]
    for node in nodes:
        if node in visitied:
            continue
        stack = [current]
        break

    visitied = set()
    while stack:
        node = stack.pop()
        if node in visitied:
            continue
        visitied.add(node)
        stack += nodes[node]
        counter2 += 1

    print(counter1, counter2)
    print(counter1 * (len(nodes) - counter1))


    return 
    scipy_graph = to_scipy_graph(nodes, edges)
    print(scipy_graph)
    print()
    mst = scipy.sparse.csgraph.minimum_spanning_tree(scipy_graph)
    
    print(mst.toarray())
    print("DIJSTRA")
    dijstra, predecessors = scipy.sparse.csgraph.dijkstra(mst, directed=False, return_predecessors=True)
    print(dijstra)
    print(predecessors)
    counts = {}
    s = 0
    for i in range(len(dijstra)):
        for j in range(len(dijstra)):
            if i == j:
                continue
            path = reconstruct_path(predecessors, i, j)
            s += len(path)
            print("----------------")
            print(path)
            for edge in path:
                if edge not in counts:
                    counts[edge] = 0
                counts[edge] += 1
    print(s)
    for n1, n2 in counts:
        n1 = int(n1)
        n2 = int(n2)
        if n1 < n2:
            print(n1, n2, counts.get((n1, n2), 0) + counts.get((n2, n1), 0))
        else:
            print(n2, n1, counts.get((n1, n2), 0)+ counts.get((n2, n1), 0))

    print()
    print("MST")
    mst_nodes, mst_edges = from_scipy_graph(mst.toarray(), nodes)
    print(len(edges), len(mst_edges))
    


    return 
    print(len(edges))
    s = 0
    for edge in tqdm.tqdm(edges):
        nodes_ = remove_edge_from_nodes(nodes, edges, edge)
        """
        print(nodes)
        print()
        print(edge)
        print()
        print(nodes_)
        print()
        """
        path = shortest_path_between_two_nodes(nodes_, edge[0], edge[1])
        if path is not None:
            s += len(path)
        # print(path)
        #print(len(path))
        #print()
        #print()

    print(s)
        

    
part1()