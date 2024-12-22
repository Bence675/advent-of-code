
from base import *

def is_nice(string):
    vowels = "aeiou"
    naughty = ["ab", "cd", "pq", "xy"]
    vowel_count = 0
    double_letter = False
    for i in range(len(string)):
        if string[i] in vowels:
            vowel_count += 1
        if i > 0 and string[i] == string[i-1]:
            double_letter = True
        if i > 0 and string[i-1:i+1] in naughty:
            return False
    return vowel_count >= 3 and double_letter

def part1():
    data = readers.read_input("5.txt")
    count = 0
    for string in data:
        if is_nice(string):
            count += 1
    print(count)

part1()

def is_nice2(string):
    double_letter = False
    same_after_two = False
    for i in range(len(string) - 1):
        if string[i:i+2] in string[i+2:]:
            double_letter = True
        if i < len(string) - 2 and string[i] == string[i+2]:
            same_after_two = True
    return double_letter and same_after_two

def part2():
    data = readers.read_input("5.txt")
    count = 0
    for string in data:
        if is_nice2(string):
            count += 1
    print(count)

part2()