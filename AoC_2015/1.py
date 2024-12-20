
from base import *

def part1():
    data = readers.read_input("1.txt")
    print(data.count("(") - data.count(")"))

part1()

def part2():
    data = readers.read_input("1.txt")
    floor = 0
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            print(i+1)
            break

part2()