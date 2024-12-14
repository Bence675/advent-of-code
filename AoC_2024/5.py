

def read_input():
    file = open("5.txt", "r")
    rules = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        rules.append(tuple(line.split("|")))

    uodates = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        uodates.append(line.split(","))

    return rules, uodates

def match_rules(rules, num1, num2):
    for rule in rules:
        if num1 == rule[0] and num2 == rule[1]:
            return True
    return False


def part1():
    rules, updates = read_input()
    sum = 0
    for update in updates:
        valid = True
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if not match_rules(rules, update[i], update[j]):
                    valid = False
                    break
            if not valid:
                break

        if valid:
            sum += int(update[len(update)//2])
    print(sum)

def fix(update, rules):
    for i in range(len(update)-1):
        for j in range(i+1, len(update)):
            if not match_rules(rules, update[i], update[j]):
                update[j], update[i] = update[i], update[j]
                return fix(update, rules)
    
    return update


def part2():
    rules, updates = read_input()
    sum = 0
    for update in updates:
        valid = True
        for i in range(len(update)-1):
            for j in range(i+1, len(update)):
                if not match_rules(rules, update[i], update[j]):
                    valid = False
                    break
            if not valid:
                break
        
        if not valid:
            x = fix(update, rules)
            sum += int(x[len(x)//2])
    
    print(sum)
                

part1()
part2()