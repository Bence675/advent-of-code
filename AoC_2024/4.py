

def read_input():
    file = open("4.txt", "r")
    lines = file.readlines()
    return lines

def part1():
    lines = read_input()
    
    word = "XMAS"
    sum = 0
    
    north_transform = lambda x, y: (x, y-1)
    south_transform = lambda x, y: (x, y+1)
    east_transform = lambda x, y: (x+1, y)
    west_transform = lambda x, y: (x-1, y)
    northeast_transform = lambda x, y: (x+1, y-1)
    northwest_transform = lambda x, y: (x-1, y-1)
    southeast_transform = lambda x, y: (x+1, y+1)
    southwest_transform = lambda x, y: (x-1, y+1)

    transforms = [
        north_transform,
        south_transform,
        east_transform,
        west_transform,
        northeast_transform,
        northwest_transform,
        southeast_transform,
        southwest_transform
    ]



    for row in range(len(lines)):
        for col in range(len(lines[row])):
            for transform in transforms:
                x = col
                y = row
                word_index = 0
                while y >= 0 and y < len(lines) and x >= 0 and x < len(lines[y]):
                    if lines[y][x] != word[word_index]:
                        break
                    word_index += 1
                    if word_index == len(word):
                        sum += 1
                        break
                    x, y = transform(x, y)

    
    print(sum)

def part2():
    def check_x_mas(three_by_three):
        if three_by_three[1][1] != "A":
            return False
        corners = [three_by_three[0][0], three_by_three[0][2], three_by_three[2][2], three_by_three[2][0]]
        corners = "".join(corners)

        m_count = 0
        s_count = 0
        for corner in corners:
            if corner == "M":
                m_count += 1
            elif corner == "S":
                s_count += 1

        if m_count != 2 or s_count != 2:
            return False

        if "MM" in corners or "SS" in corners:
            return True
        
        return False
    lines = read_input()

    word = "MAS"
    sum = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if j + 2 < len(lines[i]) and i + 2 < len(lines):
                three_by_three = [lines[i][j:j+3], lines[i+1][j:j+3], lines[i+2][j:j+3]]
                if check_x_mas(three_by_three):
                    sum += 1
    print(sum)
            
part1()
part2()