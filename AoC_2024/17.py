
import math
from base import *


def bitwise_XOR(a, b):
    res = ""
    for i in range(max(len(a), len(b))):
        if i < len(a) and i < len(b):
            res = str(int(a[-i-1]) ^ int(b[-i-1])) + res
        elif i < len(a):
            res = a[-i-1] + res
        else:
            res = b[-i-1] + res
    return int(res, 2)

class Machine:
    def __init__(self, instructions, registers):
        self.instructions = instructions
        self.registers = registers
        self.pointer = 0
        self.output = []

    def run(self):
        while self.pointer >= 0 and self.pointer < len(self.instructions):
            self.run_instruction(self.instructions[self.pointer : self.pointer + 2])



    def adv(self, literal):
        denominator = 2 ** literal
        self.registers[0] = math.floor(self.registers[0] / denominator)

    def bxl(self, literal):
        bin1 = bin(self.registers[1])[2:]
        bin2 = bin(literal)[2:]
        self.registers[1] = bitwise_XOR(bin1, bin2)

    def bst(self, literal):
        self.registers[1] = literal % 8

    def jnz(self, literal):
        if self.registers[0] == 0:
            return
        self.pointer = literal

    def bxc(self, literal):
        bin1 = bin(self.registers[1])[2:]
        bin2 = bin(self.registers[2])[2:]

        self.registers[1] = bitwise_XOR(bin1, bin2)

    def out(self, literal):
        self.output.append(str(literal % 8))

    def bdv(self, literal):
        denominator = 2 ** literal
        self.registers[1] = math.floor(self.registers[0] / denominator)

    def cdv(self, literal):
        denominator = 2 ** literal
        self.registers[2] = math.floor(self.registers[0] / denominator)
        

    def run_instruction(self, instruction):
        opcode, operand = instruction
        operand = int(operand)
        literal = (operand if operand < 4 else self.registers[operand - 4])
        self.pointer += 2
        func = None
        if opcode == "0":
            func = self.adv
        elif opcode == "1":
            func = self.bxl
        elif opcode == "2":
            func = self.bst
        elif opcode == "3":
            func = self.jnz
        elif opcode == "4":
            func = self.bxc
        elif opcode == "5":
            func = self.out
        elif opcode == "6":
            func = self.bdv
        elif opcode == "7":
            func = self.cdv
        else:
            raise ValueError("Invalid opcode")
        func(literal)

    def __str__(self):
        return "Registers: " + str(self.registers) + " Output: " + str(self.output)
    
    def __repr__(self):
        return self.__str__()
    
    def copy(self):
        machine = Machine(self.instructions, self.registers.copy())
        machine.pointer = self.pointer
        machine.output = self.output.copy()
        return machine

def part1():
    data = readers.read_input("17.txt")
    registers = [0, 0, 0]
    registers[0] = int(data[0][2])
    registers[1] = int(data[1][2])
    registers[2] = int(data[2][2])

    instructions = data[4][1].split(",")
    
    machine = Machine(instructions, registers)
    machine.run()
    print(machine)
    print(','.join([str(x) for x in machine.output]))

part1()

def solver(solutions, prefix):
    s = solutions[-1]
    for i in range(8):
        a = prefix * 8 + i
        b = i
        b = b ^ 2
        c = math.floor(a // 2 ** b)
        b = b ^ 3
        b = b ^ c
        if b % 8 == s:
            if len(solutions) == 1:
                return a
            res = solver(solutions[:-1], a)
            if res != None:
                return res
    return None


def part2():
    print(solver([2,4,1,2,7,5,1,3,4,3,5,5,0,3,3,0], 0))


part2()
