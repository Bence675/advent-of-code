
from base import *
import numpy as np
import time

SHAPE = (101, 103)

class Robot:
    def __init__(self, data):
        p = data[0].split("=")[1].split(",")
        self.position = (int(p[0]), int(p[1]))
        v = data[1].split("=")[1].split(",")
        self.velocity = (int(v[0]), int(v[1]))
        
    def __repr__(self):
        return f"Robot at {self.position} with velocity {self.velocity}"
    
    def move(self, steps = 1):
        self.position = ((self.position[0] + steps * self.velocity[0]) % SHAPE[0], (self.position[1] + steps * self.velocity[1]) % SHAPE[1])

def part1():
    data = readers.read_input("14.txt")
    robots = []
    for d in data:
        robots.append(Robot(d))

    for r in robots:
        r.move(100)

    m = np.zeros((SHAPE[1], SHAPE[0]), dtype=int)
    for r in robots:
        m[r.position[1], r.position[0]] += 1

    s = [0, 0, 0, 0]
    for i in range(SHAPE[1]):
        for j in range(SHAPE[0]):
            if i == SHAPE[1] // 2 or j == SHAPE[0] // 2:
                continue
            if i < SHAPE[1] // 2 and j < SHAPE[0] // 2:
                s[0] += m[i, j]
            elif i < SHAPE[1] // 2 and j > SHAPE[0] // 2:
                s[1] += m[i, j]
            elif i > SHAPE[1] // 2 and j < SHAPE[0] // 2:
                s[2] += m[i, j]
            elif i > SHAPE[1] // 2 and j > SHAPE[0] // 2:
                s[3] += m[i, j]

    print(utils.product(s))
    
part1()

def part2():
    data = readers.read_input("14.txt")
    robots = []
    for d in data:
        robots.append(Robot(d))

    counter = 0
    
    while True:
        counter += 1
        print("Counter:", counter)
        for r in robots:
            r.move()
        m = np.zeros((SHAPE[1], SHAPE[0]), dtype=int)
        for r in robots:
            m[r.position[1], r.position[0]] += 1

        for i in range(SHAPE[1]):
            for j in range(SHAPE[0]):
                print('#' if m[i, j] > 0 else '.', end = "")
            print()
        
        time.sleep(0.001)

part2()