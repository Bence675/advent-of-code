LIST1 = []
LIST2 = []
FILENAME = "input1.txt"


def read_input():
    global LIST1, LIST2
    LIST1 = []
    LIST2 = []
    file = open(FILENAME, "r")
    while True:
        line = file.readline()
        if not line:
            break
        nums = line.split()
        LIST1.append(int(nums[0]))
        LIST2.append(int(nums[1]))

def part1():
    sum = 0
    read_input()
    LIST1.sort()
    LIST2.sort()

    for i in range(len(LIST1)):
        sum += abs(LIST1[i] - LIST2[i])

    print(sum)

def part2():
    read_input()
    dict1 = {}
    dict2 = {} 

    for l1 in LIST1:
        if l1 in dict1:
            dict1[l1] += 1
        else:
            dict1[l1] = 1

    for l2 in LIST2:
        if l2 in dict2:
            dict2[l2] += 1
        else:
            dict2[l2] = 1

    sum = 0
    for key in dict1:
        if key in dict2:
            sum += key * dict1[key] * dict2[key]
            print(key, dict1[key], dict2[key])


    print(sum)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()