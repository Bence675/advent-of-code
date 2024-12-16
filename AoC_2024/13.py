
from fractions import Fraction
from base import *

class ClawMachine:
    def __init__(self, data):
        print(data)
        data[0] = ' '.join(data[0])
        a = data[0].split(": ")[1]
        self.button_a = (Fraction(a.split(", ")[0].split("X+")[1]), Fraction(a.split(", ")[1].split("Y+")[1]))
        data[1] = ' '.join(data[1])
        b = data[1].split(": ")[1]
        self.button_b = (Fraction(b.split(", ")[0].split("X+")[1]), Fraction(b.split(", ")[1].split("Y+")[1]))
        data[2] = ' '.join(data[2])
        prize = data[2].split(": ")[1]
        self.prize = (Fraction(prize.split(", ")[0].split("X=")[1]), Fraction(prize.split(", ")[1].split("Y=")[1]))

    def solve(self):
        a = self.button_a
        b = self.button_b
        prize = self.prize

        result_b = (prize[1] - a[1] * prize[0] / a[0]) / (b[1] - a[1] * b[0] / a[0])
        result_a = (prize[0] - b[0] * result_b) / a[0]

        return result_a, result_b
    
class ClawMachine2(ClawMachine):
    def __init__(self, data):
        super().__init__(data)
        self.prize = (self.prize[0] + 10000000000000, self.prize[1] + 10000000000000)
    
def part1():
    data = readers.read_input("13.txt")

    claw_machines = []
    for i in range(0, len(data), 4):
        claw_machines.append(ClawMachine(data[i:i+3]))

    sum = 0
    for claw_machine in claw_machines:
        res = claw_machine.solve()
        print(res)
        if res[0].denominator == 1 and res[1].denominator == 1:
            if res[0].numerator > 100 or res[1].numerator > 100:
                continue
            sum += res[0].numerator * 3 + res[1].numerator

        
    print(sum)

part1()

def part2():
    data = readers.read_input("13.txt")

    claw_machines = []
    for i in range(0, len(data), 4):
        claw_machines.append(ClawMachine2(data[i:i+3]))

    sum = 0
    for claw_machine in claw_machines:
        res = claw_machine.solve()
        print(res)
        if res[0].denominator == 1 and res[1].denominator == 1:
            sum += res[0].numerator * 3 + res[1].numerator

        
    print(sum)

part2()