
from base import *


def part1():
    data = readers.read_input("2.txt", sep="x", transform=int)
    sum = 0
    for x, y, z in data:
        sum += 2*x*y + 2*y*z + 2*z*x + min(x*y, y*z, z*x)

    print(sum)

part1()

def part2():
    data = readers.read_input("2.txt", sep="x", transform=int)
    sum = 0
    for x, y, z in data:
        d = [x, y, z]
        d.sort()

        sum += 2*d[0] + 2*d[1] + x*y*z

    print(sum)

part2()