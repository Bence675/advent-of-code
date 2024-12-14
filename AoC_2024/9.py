
def read_input():
    file = open("9.txt", "r")
    return file.read()

def build_memory(pattern):
    memory = []
    free = False
    counter = 0
    for char in pattern:
        n = int(char)
        if free:
            memory += [None] * n
            free = False
        else:
            memory += [counter] * n
            counter += 1
            free = True

    return memory


def part1():
    text = read_input()
    sum = 0
    memory = build_memory(text)
    start = 0
    end = len(memory) - 1

    while start < end:
        if memory[end] is None:
            end -= 1
            continue
        else:
            while memory[start] is not None:
                start += 1
            if start >= end:
                break
            memory[start], memory[end] = memory[end], None
    print(memory)

    for i in range(len(memory)):
        if memory[i] is not None:
            sum += i * memory[i]

    print(sum)

def part2():
    text = read_input()
    sum = 0
    memory = build_memory(text)
    end = len(memory) - 1
    print(memory)
    
    while 0 < end:
        print(end)
        if memory[end] is None:
            end -= 1
            continue
        else:
            length = 0
            fileID = memory[end]
            while memory[end] == fileID:
                length += 1
                end -= 1
            # print(fileID, length)


            begin = 0
            while memory[begin:begin+length] != [None] * length and begin < end:
                begin += 1

            if memory[begin:begin+length] == [None] * length:
                memory[begin:begin+length] = [fileID] * length
                memory[end+1:end+1+length] = [None] * length
                # print(memory)

                

    print(memory)

    for i in range(len(memory)):
        if memory[i] is not None:
            sum += i * memory[i]

    print(sum)


part2()