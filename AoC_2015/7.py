
from base import *

def part1():
    data = readers.read_input("7.txt")
    wires = {}
    for line in data:
        wires[line[-1]] = line[:-2]

    def get_value(wire):
        value = None
        print(wire)
        if type(wire) == int:
            return wire
        if type(wire) == str and wire.isnumeric():
            return int(wire)
        if type(wires[wire]) == int:
            return wires[wire]
        if len(wires[wire]) == 1:
            if wires[wire][0].isnumeric():
                wires[wire] = int(wires[wire][0])
            else:
                wires[wire] = get_value(wires[wire][0])
            return wires[wire]
        if len(wires[wire]) == 2:
            value = ~get_value(wires[wire][1])
        if len(wires[wire]) == 3:
            if wires[wire][1] == "AND":
                value = get_value(wires[wire][0]) & get_value(wires[wire][2])
            if wires[wire][1] == "OR":
                value = get_value(wires[wire][0]) | get_value(wires[wire][2])
            if wires[wire][1] == "LSHIFT":
                value = get_value(wires[wire][0]) << get_value(wires[wire][2])
            if wires[wire][1] == "RSHIFT":
                value = get_value(wires[wire][0]) >> get_value(wires[wire][2])

        wires[wire] = value % 2**16
        return wires[wire]
    
    print(get_value("a"))

part1()