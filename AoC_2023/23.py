import sys

import time 
import random

sys.setrecursionlimit(10000)

GLOBAL_MAX = 0

def read_input():
    file = open("23.txt", "r")
    lines = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        lines.append(line)

    return lines


class Maze1:
    def __init__(self, maze):
        self.nodes = {}
        self.edges = {}
        self.maze = maze
        self.build_graph()

    def find_edges(self, current):
        edges = []
        queue = [current]
        visited = {}
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited[current] = True
            if current in self.nodes:
                edges.append(current)
            else:
                queue += self.edges[current]

    def build_graph(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] in ['>', '<', '^', 'v']:
                    self.nodes[(i, j)] = self.maze[i][j]
                if self.maze[i][j] == '.' and i == 0:
                    self.nodes[(i, j)] = '.'
                if self.maze[i][j] == '.' and i == len(self.maze) - 1:
                    self.nodes[(i, j)] = '.'
                    
        for node in self.nodes:
            self.edges[node] = []
            i, j = node
            queue = []
            if self.maze[i][j] == '>':
                queue = [((i, j+1), 1)]
            elif self.maze[i][j] == '<':
                queue = [((i, j-1), 1)]
            elif self.maze[i][j] == '^':
                queue = [((i-1, j), 1)]
            elif self.maze[i][j] == 'v':
                queue = [((i+1, j), 1)]
            elif self.maze[i][j] == '.':
                queue = [((i, j), 0)]

            visited = {}

            while queue:
                current, path_length = queue.pop(0)
                i, j = current
                if current in visited or i < 0 or i >= len(self.maze) or j < 0 or j >= len(self.maze[0]) or self.maze[i][j] == '#':
                    continue
                visited[current] = True

                if current in self.nodes and current != node:
                    self.edges[node].append((current, path_length))
                else:
                    if self.maze[i][j] == '>':
                        queue.append(((i, j+1), path_length+1))
                    elif self.maze[i][j] == '<':
                        queue.append(((i, j-1), path_length+1))
                    elif self.maze[i][j] == '^':
                        queue.append(((i-1, j), path_length+1))
                    elif self.maze[i][j] == 'v':
                        queue.append(((i+1, j), path_length+1))
                    elif self.maze[i][j] == '.':
                        if i + 1 < len(self.maze) and self.maze[i+1][j] != "^":
                            queue.append(((i+1, j), path_length+1))
                        if i - 1 >= 0 and self.maze[i-1][j] != "v":
                            queue.append(((i-1, j), path_length+1))
                        if j + 1 < len(self.maze[0]) and self.maze[i][j+1] != "<":
                            queue.append(((i, j+1), path_length+1))
                        if j - 1 >= 0 and self.maze[i][j-1] != ">":
                            queue.append(((i, j-1), path_length+1))

    def longest_path(self):
        max_path = 0
        start = [node for node in self.nodes if self.nodes[node] == '.'][0]

        queue = [(start, 0)]
        visited = {}
        while queue:
            current_node, current_path = queue.pop(0)
            if current_node in visited:
                if visited[current_node] >= current_path:
                    continue
            visited[current_node] = current_path
            x, y = current_node
            if self.maze[x][y] == '.':
                max_path = max(max_path, current_path)
            for node, path_length in self.edges[current_node]:
                queue.append((node, current_path+path_length))

        return max_path
    
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))


class Maze2:

    def __init__(self, maze):
        self.nodes = {}
        self.edges = {}
        self.maze = maze
        self.build_graph()

    def find_edges(self, current):
        edges = []
        queue = [current]
        visited = {}
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited[current] = True
            if current in self.nodes:
                edges.append(current)
            else:
                queue += self.edges[current]

    def is_crossroad(self, i, j):
        counter = 0
        posible_neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for neighbor in posible_neighbors:
            if neighbor[0] >= 0 and neighbor[0] < len(self.maze) and neighbor[1] >= 0 and neighbor[1] < len(self.maze[0]) and self.maze[neighbor[0]][neighbor[1]] != "#":
                counter += 1
        return counter > 2
            

    def build_graph(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.maze[i][j] != "#":
                    self.nodes[(i, j)] = Node(i, j)
                    

        queue = [node for node in self.nodes if  self.nodes[node].x == 0]
        visited = {}
        while queue:
            current = queue.pop(-1)
            if current in visited:
                continue
            if current not in self.nodes:
                continue

            visited[current] = True
            i, j = current
            if self.edges.get((i, j)) is None:
                self.edges[(i, j)] = []
            if (i, j+1) in self.nodes:
                queue.append((i, j+1))
                self.edges[(i, j)] += [(i, j+1)]
            if (i, j-1) in self.nodes:
                queue.append((i, j-1))
                self.edges[(i, j)] += [(i, j-1)]
            if (i+1, j) in self.nodes:
                queue.append((i+1, j))
                self.edges[(i, j)] += [(i+1, j)]
            if (i-1, j) in self.nodes:
                queue.append((i-1, j))
                self.edges[(i, j)] += [(i-1, j)]



    def longest_path(self):
        def find_path(node):
            path = [node]
            while node.parent:
                node = node.parent
                path.append(node)
            return path
        
        max_path = 0
        start = [node for node in self.nodes if self.maze[node[0]][node[1]] == '.'][0]

        queue = [(start, 0, None)]
        print("start")
        print(start)
        while queue:
            print("queue", len(queue))
            current_node, current_path, parent = queue.pop(0)
            print(current_path)
            if parent:
                path = find_path(parent)
                if self.nodes[current_node] in path:
                    continue
            
            if self.nodes[current_node].parent and len(find_path(self.nodes[current_node].parent)) > len(find_path(parent)):
                continue
            self.nodes[current_node].parent = parent
            x, y = current_node
            if self.maze[x][y] == '.' and x == len(self.maze) - 1:
                if current_path > max_path:
                    max_path = max(max_path, current_path)
                    print("path")
                    print(max_path)
                    x = [['.' for _ in range(len(self.maze))] for _ in range(len(self.maze[0]))]
                    for node in [(node.x, node.y) for node in find_path(self.nodes[current_node])] :
                        x[node[0]][node[1]] = "O"

                    for line in x:
                        print("".join(line))
                        
            for node in self.edges[current_node]:
                if self.nodes[current_node]:
                    path = find_path(self.nodes[current_node])
                    if self.nodes[node] not in path:
                        queue.append((node, current_path+1, self.nodes[current_node]))

        return max_path



def part1():
    lines = read_input()
    maze = Maze1(lines)
    print(maze.nodes)
    for node in maze.nodes:
        print(node, maze.edges[node])

    print(maze.longest_path())

#part1()

print("Part 2")

def longest_path(maze, start, mask, depth=0):
    global GLOBAL_MAX
    r = random.randint(0, 100000)
    length = 0
    if depth < 10:
        print("Depth", depth)
    while True:
        potential_next_cells = [(start[0], start[1]+1), (start[0], start[1]-1), (start[0]+1, start[1]), (start[0]-1, start[1])]
        next_cells = []
        for x, y in potential_next_cells:
            if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
                continue
            if mask[x][y]:
                continue
            if maze[x][y] == "#":
                continue
            next_cells.append((x, y))

        if not next_cells:
            return None, None, None
        
        if len(next_cells) > 1:
            break

        start = next_cells[0]
        mask[start[0]][start[1]] = True
        length += 1

        if start[0] == len(maze) - 1:
            s = sum([sum([int(cell) for cell in line if cell]) for line in mask])-1


            if s > GLOBAL_MAX:
                GLOBAL_MAX = s
                print(GLOBAL_MAX)

            return length, start, mask.copy()

    # for line in mask:
    #     print("".join(["#" if cell else "." for cell in line]))
    max_path = 0
    max_path_cell = None
    max_path_mask = None
    
    tmp_mask = [[cell for cell in line] for line in mask]
    for cell in next_cells:
        mask = [[cell for cell in line] for line in tmp_mask]
        x, y = cell
        """
        if x == 6 and y == 3 or x == 5 and y == 4:
            print("HERE")
            print(r)
            print(next_cells)
            print(cell)
            for line in mask:
                print("".join(["#" if cell else "." for cell in line]))
        """
        mask[x][y] = True
        if x == len(maze) - 1:
            print("Path")
            for line in mask:
                print("".join(["#" if cell else "." for cell in line]))
            print(sum([sum([int(cell) for cell in line if cell]) for line in mask])-1)
            print("CHECK2")
            raise Exception()
            return 1, cell, mask
        
        path, next_cell, next_mask = longest_path(maze, cell, mask.copy(), depth+1)
        if next_mask is None:
            mask[x][y] = False
            continue
        if path is not None and path > max_path:
            max_path = path
            max_path_cell = next_cell
            max_path_mask = next_mask.copy()
            # print(max_path, max_path_cell )
        mask[x][y] = False

    return max_path + length, max_path_cell, max_path_mask

class Maze3:
    def __init__(self, maze):
        self.maze = maze
        self.nodes = {}
        self.edges = {}

    def build_graph(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                if self.maze[row][col] == ".":
                    potential_neighbors = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
                    neighbors = []
                    for x, y in potential_neighbors:
                        if x >= 0 and x < len(self.maze) and y >= 0 and y < len(self.maze[0]) and self.maze[x][y] != "#":
                            neighbors.append((x, y))

                    if len(neighbors) > 2 or row == 0 or row == len(self.maze) - 1:
                        self.nodes[(row, col)] = True

        for node in self.nodes:
            self.edges[node] = []
            queue = [(node, 0)]
            visited = {}
            while queue:
                current, path_length = queue.pop(0)
                x, y = current
                if x < 0 or x >= len(self.maze):
                    continue
                if self.maze[x][y] == "#":
                    continue
                if current in visited:
                    continue
                visited[current] = True
                if current in self.nodes and current != node:
                    self.edges[node].append((current, path_length))
                else:
                    for neighbor in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        queue.append((neighbor, path_length+1))



    def longest_path(self, start, depth=0):


        max_path = 0
        additional_length = 0
        max_path_mask = None
        path_cells = None
        
        queue = [(start, 0, [], [start])]
        while queue:
            """
            print("Queue")
            for node, path_length, mask, path in queue:
                print(node, path_length, path)
            print()
            time.sleep(1)
            """
            current, current_path, seen, current_path_cells = queue.pop()
            x, y = current
            if x == len(self.maze) - 1:
                if current_path > max_path:
                    max_path = current_path
                    path_cells = current_path_cells

                continue
            seen += [current]
            for node, path_length in self.edges[current]:
                if node not in seen:
                    queue.append((node, current_path+path_length, seen.copy(), current_path_cells + [node]))

        return max_path, max_path_mask, path_cells

def part2():
    lines = read_input()
    mask = [[False for y in range(len(lines[0]))] for x in range(len(lines))]
    start = [x for x in range(len(lines[0])) if lines[0][x] == '.'][0]
    mask[0][start] = True
    print(longest_path(lines, (0, start), mask))
    print(GLOBAL_MAX)


def part3():
    lines = read_input()
    maze = Maze3(lines)
    maze.build_graph()
    print(maze.nodes)
    for edge in maze.edges:
        print(edge, maze.edges[edge])

    length, mask, path = maze.longest_path((0, [x for x in range(len(lines[0])) if lines[0][x] == '.'][0]))
    sum = 0
    start = path[0]
    #print(path)
    while len(path) > 1:
        print(start, path[1], [length for edge, length in maze.edges[start] if edge == path[1]][0])
        sum += [length for edge, length in maze.edges[start] if edge == path[1]][0]
        start = path[1]
        path = path[1:]
    print(sum)
    
part3()