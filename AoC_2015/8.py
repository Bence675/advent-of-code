
from base import *

def part1():
    data = readers.read_input("8.txt")

    count = 0
    for line in data:
        count += len(line)
        count -= len(eval(line))

    print(count)

part1()

def part2():
    data = readers.read_input("8.txt")

    count = 0
    for line in data:
        count += 2
        count += line.count("\\")
        count += line.count("\"")

    print(count)

part2()