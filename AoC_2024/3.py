
import regex as re

def read_input():
    file = open("3.txt", "r")
    text = file.read()
    return text

def part1():
    text = read_input()

    pattern = r"mul\(\d{1,3}\,\d{1,3}\)"
    matches = re.findall(pattern, text)
    
    sum = 0
    for match in matches:
        nums = re.findall(r"\d{1,3}", match)
        sum += int(nums[0]) * int(nums[1])
    
    print(sum)
    
def part2():
    text = read_input()

    pattern = r"mul\(\d{1,3}\,\d{1,3}\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, text)

    enabled = True
    sum = 0
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            nums = re.findall(r"\d{1,3}", match)
            sum += int(nums[0]) * int(nums[1])

    print(sum)

part1()
part2()