
import hashlib
from base import *

def part1():
    data = readers.read_input("4.txt")

    counter = 0
    while True:
        counter += 1
        if hashlib.md5((data + str(counter)).encode()).hexdigest().startswith("00000"):
            break

    print(counter)

part1()

def part2():
    data = readers.read_input("4.txt")

    counter = 0
    while True:
        counter += 1
        if hashlib.md5((data + str(counter)).encode()).hexdigest().startswith("000000"):
            break

    print(counter)

part2()