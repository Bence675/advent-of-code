
from base import *

class Keypad:
    def __init__(self, is_robot = False):
        if is_robot:
            self.keys = [["", "^", "A"], ["<", "v", ">"]]
        else:
            self.keys = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]
        self.x = 2
        self.y = 3
        self.controller = None

    def get_coordinates_of_key(self, key):
        for y in range(len(self.keys)):
            for x in range(len(self.keys[y])):
                if self.keys[y][x] == key:
                    return (y, x)
        raise ValueError("Invalid key")
    
    def get_paths_from_key_to_key(self, start, end):
        # print(start, end)
        if start == end:
            return [[]]
        start_y, start_x = self.get_coordinates_of_key(start)
        end_y, end_x = self.get_coordinates_of_key(end)
        paths = []
        if start_x < end_x and self.keys[start_y][start_x + 1] != "":
            for p in self.get_paths_from_key_to_key(self.keys[start_y][start_x + 1], end):
                paths.append([">"] + p)
        elif start_x > end_x and self.keys[start_y][start_x - 1] != "":
            for p in self.get_paths_from_key_to_key(self.keys[start_y][start_x - 1], end):
                paths.append(["<"] + p)
        if start_y < end_y and self.keys[start_y + 1][start_x] != "":
            for p in self.get_paths_from_key_to_key(self.keys[start_y + 1][start_x], end):
                paths.append(["v"] + p)
        elif start_y > end_y and self.keys[start_y - 1][start_x] != "":
            for p in self.get_paths_from_key_to_key(self.keys[start_y - 1][start_x], end):
                paths.append(["^"] + p)
        return paths

    def get_all_possible_paths(self, path):
        if len(path) == 0:
            return []
        current = "A"
        paths = []
        for key in path:
            x = self.get_paths_from_key_to_key(current, key)
            x = [a + ['A'] for a in x]
            if self.controller:
                res = []
                for p in x:
                    res.append(self.controller.get_all_possible_paths(p))
                x = res
            paths += min(x, key= len)
            current = key

        return paths

def part1():
    data = readers.read_input("21.txt")
    
    keypad = Keypad()
    robot1 = Keypad(True)
    keypad.controller = robot1

    robot2 = Keypad(True)
    robot1.controller = robot2

    s = 0
    for line in data:
        s += len(keypad.get_all_possible_paths(line)) * int(line[:-1])
        print(len(keypad.get_all_possible_paths(line)))
    print(s)

# part1()

import sympy as sp

def get_way(y1, x1, y2, x2):
    if y1 == y2:
        if x1 < x2:
            return ">"
        else:
            return "<"
    if x1 == x2:
        if y1 < y2:
            return "v"
        else:
            return "^"
    raise ValueError("Invalid input")


class Graph:
    def __init__(self, keys):
        self.keys = keys
        self.nodes = []
        self.edges = []
        self.paths = {}
        self.memory = {}
        
        for y in range(len(keys)):
            for x in range(len(keys[y])):
                if keys[y][x] != "":
                    self.set_edges_from_key(y, x)
                    self.nodes.append(keys[y][x])
        
        for node1 in self.nodes:
            for node2 in self.nodes:
                start = node1
                end = node2
                paths = self.get_all_paths(start, end)
                self.paths[start, end] = paths

    def set_edges_from_key(self, y, x):
        if self.keys[y][x] == "":
            return
        for edge in utils.run_function_on_neighbors(self.keys, y, x, lambda y, x: (y, x)):
            if self.keys[edge[0]][edge[1]] == "":
                continue
            self.edges.append((self.keys[y][x], self.keys[edge[0]][edge[1]], get_way(y, x, edge[0], edge[1])))
                



    def get_all_paths(self, start, end, path = []):
        if start == end:
            if end == "A":
                return
            return [[(start, end, 'A')]]
        paths = []
        for edge in self.edges:
            if edge[0] == start:
                print(path)
                if edge[1] not in path:
                    for p in self.get_all_paths(edge[1], end, path + [start]):
                        paths.append([edge] + p)

        return paths
    
    def get_minimum_press_count(self, paths, depth = 0):
        if depth == DEPTH:
            print(paths)
            print(depth)
            print(min([len(path) for path in paths]))
            return min([len(path) for path in paths])
        minumum = float("inf")
        for path in paths:
            minumum = min(minumum, self.get_press_count(path, depth))
        
        print(paths)
        print(depth)
        print(minumum) 
        return minumum

    def get_press_count(self, path, depth = 0):
        if depth == 0:
            print(path)
        if len(path) == 0:
            return 0
        if depth == DEPTH:
            return 1
        if str(path) + str(depth) in self.memory:
            return self.memory[str(path) + str(depth)]
        count = 0
        prev = "A"
        for edge in path:
            if edge[2] == prev:
                continue
            count += self.get_minimum_press_count(self.paths[prev, edge[2]], depth + 1)
            prev = edge[0]

        self.memory[str(path) + str(depth)] = count
        return count
        

DEPTH = 1

def part2():
    data = readers.read_input("21.txt")
    
    keys = [['', '^', 'A'], ['<', 'v', '>']]
    
    graph = Graph(keys)

    # print(graph.edges)
    # print("PATH")
    # print(graph.paths)
    # x = graph.paths['A', '<']
    x = graph.paths['<', 'A']
    print(x)
    print(len(x))
    print("-----------------")
    print(graph.get_minimum_press_count(x))
    print(graph.memory)



part2()