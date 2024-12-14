

def read_input():
    file = open("7.txt", "r")
    equations = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        line = line.split(":")
        result = line[0]
        components = line[1].split(" ")[1:]
        equations.append((int(result), list(map(int, components))))

    return equations

def options(components):
    if len(components) == 1:
        return components
    results = []
    for comp in options(components[:-1]):
        results.append(comp + components[-1])
        results.append(comp * components[-1])

    return results


def options2(components):
    if len(components) == 1:
        return components
    results = []
    for comp in options2(components[:-1]):
        results.append(comp + components[-1])
        results.append(comp * components[-1])
        results.append(int(str(comp) + str(components[-1])))

    return results

def part1():
    equations = read_input()
    sum = 0
    for result, components in equations:
        if result in options(components):
            sum += result

    print(sum)


def part2():
    equations = read_input()
    sum = 0
    for result, components in equations:
        if result in options2(components):
            sum += result

    print(sum)

part1()
part2()