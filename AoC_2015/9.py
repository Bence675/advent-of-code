
from base import *

def permutations(cities):
    if len(cities) == 1:
        return [list(cities)]
    perms = []
    for city in cities:
        for perm in permutations(cities - {city}):
            perms.append([city] + perm)
    return perms

def part1():
    data = readers.read_input("9.txt")
    distances = {}
    cities = set()
    for line in data:
        city1, _, city2, _, distance = line
        distances[(city1, city2)] = int(distance)
        distances[(city2, city1)] = int(distance)
        cities.add(city1)
        cities.add(city2)
    
    min_distance = float("inf")
    for route in permutations(cities):
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[(route[i], route[i+1])]
        min_distance = min(min_distance, distance)
    
    print(min_distance)

part1()

def part2():
    data = readers.read_input("9.txt")
    distances = {}
    cities = set()
    for line in data:
        city1, _, city2, _, distance = line
        distances[(city1, city2)] = int(distance)
        distances[(city2, city1)] = int(distance)
        cities.add(city1)
        cities.add(city2)
    
    max_distance = 0
    for route in permutations(cities):
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[(route[i], route[i+1])]
        max_distance = max(max_distance, distance)
    
    print(max_distance)

part2()