
from base import *


NUM = 75


def get_next_states(number):
    if number == "0":
        return ["1"]
    elif len(number) % 2 == 0:
        return [str(int(number[:len(number)//2])), str(int(number[len(number)//2:]))]
    else:
        return [str(int(number)*2024)]

def part1(print_debug = False):
    next_states = {}
    numbers = readers.read_input("11.txt")

    
    for blink in range(NUM):
        new_numbers = []
        for i in range(len(numbers)):
            if numbers[i] not in next_states:
                next_states[numbers[i]] = get_next_states(numbers[i])
                
            new_numbers += next_states[numbers[i]]       

        numbers = new_numbers
        
        if print_debug:
            print("------------")
            print("blink", blink)
            print(numbers)


    print(len(numbers))

def rec_call(number, visited, t):
    if t == NUM:
        return 1, visited
    if (number, t) in visited:
        return visited[(number, t)], visited
    res = 0
    for next_number in get_next_states(number):
        x, visited = rec_call(next_number, visited, t+1)
        res += x
    visited[(number, t)] = res
    return res, visited

def part2():
    numbers = readers.read_input("11.txt")
    res = []

    visited = {}
    sum = 0
    for number in numbers:
        x, visited = rec_call(number, visited, 0)
        sum += x
    print(sum)
                

part2()