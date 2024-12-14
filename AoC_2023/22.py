import tqdm

class SandStone:
    def __init__(self, corner1, corner2, id):
        self.corner1 = corner1
        self.corner2 = corner2
        self.upper_sandstones = set()
        self.lower_sandstones = set()
        self.id = id
        self.name = "Sandstone" + str(id)

    def fall(self):
        self.corner1[2] -= 1
        self.corner2[2] -= 1

    def min_x(self):
        return min(self.corner1[0], self.corner2[0])
    
    def max_x(self):
        return max(self.corner1[0], self.corner2[0])
    
    def min_y(self):
        return min(self.corner1[1], self.corner2[1])
    
    def max_y(self):
        return max(self.corner1[1], self.corner2[1])
    
    def min_z(self):
        return min(self.corner1[2], self.corner2[2])
    
    def max_z(self):
        return max(self.corner1[2], self.corner2[2])

    def __str__(self):
        return f"{self.name, self.corner1, self.corner2}"
    
    def __repr__(self):
        return self.__str__()
    
    def copy(self):
        return SandStone(self.corner1.copy(), self.corner2.copy(), self.id)
    


def read_input():
    file = open("22.txt", 'r')
    lines = []
    while True:
        line = file.readline()
        if not line:
            break
        begin, end = line.split('~')
        end = end[:-1]
        print(begin, end)
        lines.append(SandStone(list(map(int, begin.split(','))), list(map(int, end.split(','))), len(lines)))
    return lines




class Space:
    def __init__(self, sandstones):
        self.sandstones = sandstones
        max_x = 0
        max_y = 0
        max_z = 0
        for sandstone in sandstones:
            max_x = max(max_x, sandstone.max_x())
            max_y = max(max_y, sandstone.max_y())
            max_z = max(max_z, sandstone.max_z())
        self.matrix = [[[None for _ in range(max_z+1)] for _ in range(max_y+1)] for _ in range(max_x+1)]
        for sandstone in sandstones:
            for x in range(sandstone.min_x(), sandstone.max_x()+1):
                for y in range(sandstone.min_y(), sandstone.max_y()+1):
                    for z in range(sandstone.min_z(), sandstone.max_z()+1):
                        self.matrix[x][y][z] = sandstone

    def __eq__(self, value):
        if len(self.sandstones) != len(value.sandstones):
            return False
        for i in range(len(self.sandstones)):
            if self.sandstones[i] != value.sandstones[i]:
                return False
        return True

    def sandstones_under_sandstone(self, sandstone):
        min_x, max_x = sandstone.min_x(), sandstone.max_x()
        min_y, max_y = sandstone.min_y(), sandstone.max_y()
        min_z, max_z = sandstone.min_z(), sandstone.max_z()
        sandstones = set()
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                if self.matrix[x][y][min_z-1] is not None:
                    sandstones.add(self.matrix[x][y][min_z-1])

        return sandstones

    def fall(self):
        fall = True
        fallen = set()
        while fall:
            fall = False
            for sandstone in self.sandstones:
                min_x, max_x = sandstone.min_x(), sandstone.max_x()
                min_y, max_y = sandstone.min_y(), sandstone.max_y()
                min_z, max_z = sandstone.min_z(), sandstone.max_z()
                #print(sandstone.name, min_x, max_x, min_y, max_y, min_z, max_z)
                if min_z == 1:
                    continue
                if not self.sandstones_under_sandstone(sandstone):
                    # print("Falling")
                    """
                    print(sandstone)
                    for x in range(min_x, max_x+1):
                        for y in range(min_y, max_y+1):
                            print(x, y, min_z-1)
                            print(self.matrix[x][y][min_z-1])
                            print()
                    """
                    fall = True
                    fallen.add(sandstone.name)
                    #print("MAtrix update")
                    for x in range(min_x, max_x+1):
                        for y in range(min_y, max_y+1):
                            #print(x, y, min_z-1)
                            self.matrix[x][y][min_z-1] = sandstone
                            self.matrix[x][y][max_z] = None
                    
                    sandstone.corner1[2] -= 1
                    sandstone.corner2[2] -= 1
    
        return fallen
    
    def set_and_get_disintegratable_sandstones(self):
        
        for i in range(len(self.sandstones)):
            min_x, max_x = self.sandstones[i].min_x(), self.sandstones[i].max_x()
            min_y, max_y = self.sandstones[i].min_y(), self.sandstones[i].max_y()
            min_z, max_z = self.sandstones[i].min_z(), self.sandstones[i].max_z()
            for x in range(min_x, max_x+1):
                for y in range(min_y, max_y+1):
                    if self.matrix[x][y][min_z-1] is not None:
                        self.sandstones[i].lower_sandstones.add(self.matrix[x][y][min_z-1])
                    #print(x, y, max_z+1)
                    if max_z + 1 < len(self.matrix[x][y]) and self.matrix[x][y][max_z+1] is not None:
                        self.sandstones[i].upper_sandstones.add(self.matrix[x][y][max_z+1])

            #print(self.sandstones[i].name, self.sandstones[i].upper_sandstones, self.sandstones[i].lower_sandstones)

        disintegratable_sandstones = set()
        for sandstone in self.sandstones:
            if not sandstone.upper_sandstones:
                #print(sandstone.name)
                disintegratable_sandstones.add(sandstone)
                continue
            is_disintegratable = True
            for upper_sandstone in sandstone.upper_sandstones:
                if len(upper_sandstone.lower_sandstones) == 1:
                    is_disintegratable = False
                    break
            if is_disintegratable:
                disintegratable_sandstones.add(sandstone)
            
        return disintegratable_sandstones
    
    def remove_sandstone(self, sandstone):
        self.sandstones.remove(sandstone)
        min_x, max_x = sandstone.min_x(), sandstone.max_x()
        min_y, max_y = sandstone.min_y(), sandstone.max_y()
        min_z, max_z = sandstone.min_z(), sandstone.max_z()
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                for z in range(min_z, max_z+1):
                    self.matrix[x][y][z] = None

    def copy(self):
        s = Space([sandstone.copy() for sandstone in self.sandstones])
        s.set_and_get_disintegratable_sandstones()
        return s
    
    def get_sandstone(self, id):
        for sandstone in self.sandstones:
            if sandstone.id == id:
                return sandstone
        return None

def part1():
    # init 
    sandstones = read_input()
    counter = 0
    space = Space(sandstones)
    space.fall()

    disig_sandstones = space.set_and_get_disintegratable_sandstones()
    # print(space.set_and_get_disintegratable_sandstones())
    # print(len(disig_sandstones))

def part2():
    print("Part 2")
    sandstones = read_input()
    space = Space(sandstones)
    space.fall()

    disig_sandstones = space.set_and_get_disintegratable_sandstones()
    sum = 0
    for sandstone in tqdm.tqdm(space.sandstones):
        if sandstone not in disig_sandstones:
            orignal_space = space.copy()
            sandstone = space.get_sandstone(sandstone.id)

            space.remove_sandstone(sandstone)
            fallen_sandstones = space.fall()
            #print(fallen_sandstones)
            sum += len(fallen_sandstones)
            
            space = orignal_space

    print(sum)
        
part1()
part2()