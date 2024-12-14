
from enum import Enum
from copy import deepcopy
import math
import time



class ModuleType(Enum):
    NoneType = 0
    Broadcast = 1
    FlipFlop = 2
    Conjunction = 3

class Signal:
    LOW = 0
    HIGH = 1

class SignalQueue:
    def __init__(self):
        self.signal_queue = []
        self.low_counter = 0
        self.high_counter = 0
        self.modules = {}
        self.tick = 0

    def append(self, signal):
        self.signal_queue.append(signal)

    def add_module(self, name, module):
        self.modules[name] = module

    def step(self):
        name, dest, signal = self.signal_queue.pop(0)
        if signal == Signal.LOW:
            self.low_counter += 1
        else:
            self.high_counter += 1
        # print(name, " -", "low" if signal == Signal.LOW else "high", "-> ", dest, sep="")
        if (name == "lt") and signal == Signal.HIGH:
            raise ValueError("Signal is low")
        self.modules[dest](name, signal)
    

class Module:
    def __init__(self, name, signal_queue):
        self.name = name
        self.roots = []
        self.destinations = []
        self.signal_queue = signal_queue
        self.type = ModuleType.NoneType
        self.states = []
        self.cycle_size = 0

    def add_root(self, root):
        self.roots.append(root)

    def add_destination(self, destination):
        self.destinations.append(destination)

    def __call__(self, signal, sender=None):
        for destination in self.destinations:
            self.signal_queue.append((self.name, destination, signal))

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type


class Broadcast(Module):
    def __init__(self, name, signal_queue):
        super().__init__(name, signal_queue)
        self.type = ModuleType.Broadcast

    def __call__(self, sender, signal):
        super().__call__(signal)
    
    
class FlipFlop(Module):
    def __init__(self, name, signal_queue):
        super().__init__(name, signal_queue)
        self.type = ModuleType.FlipFlop
        self.state = Signal.LOW

    def flip(self):
        self.state = Signal.HIGH if self.state == Signal.LOW else Signal.LOW

    def __call__(self, sender, signal):
        if signal == Signal.LOW:
            self.flip()
            super().__call__(self.state)

    def __eq__(self, other):
        if self.name == other.name and self.type == other.type and self.state == other.state:
            for i in range(len(self.roots)):
                if self.roots[i] != other.roots[i]:
                    return False
            return True
        return False
    
    def reset(self):
        self.state = Signal.LOW
    

class Conjunction(Module):
    def __init__(self, name, signal_queue):
        super().__init__(name, signal_queue)
        self.type = ModuleType.Conjunction
        self.memory = {}

    def add_root(self, root):
        self.memory[root] = Signal.LOW
        return super().add_root(root)
    
    def __call__(self, sender, signal):
        if self.name == "ft":
            pass
            # print(self.memory)
        self.memory[sender] = signal
        if all([value == Signal.HIGH for value in self.memory.values()]):
            super().__call__(Signal.LOW)
        else:
            super().__call__(Signal.HIGH)

    def __eq__(self, other):
        if self.name == other.name and self.type == other.type and self.memory == other.memory:
            for i in range(len(self.roots)):
                if self.roots[i] != other.roots[i]:
                    return False
            return True
        return False
    

def main():
    signal_queue = SignalQueue()
    file = open("20.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        parts = line.split(" -> ")
        name = parts[0]
        dests = parts[1].split(", ")
        if name == "broadcaster":
            module = Broadcast(name, signal_queue)
        elif name.startswith("%"):
            name = name[1:]
            module = FlipFlop(name, signal_queue)
        elif name.startswith("&"):
            name = name[1:]
            module = Conjunction(name, signal_queue)
        else:
            raise ValueError("Invalid module type")
        
        signal_queue.add_module(name, module)

    file.close()

    file = open("20.txt", "r")
    while True:
        line = file.readline()[:-1]
        if not line:
            break
        parts = line.split(" -> ")
        name = parts[0]
        if name != "broadcaster":
            name = name[1:]

        dests = parts[1].split(", ")
        for dest in dests:
            if dest in signal_queue.modules:
                signal_queue.modules[dest].add_root(name)
                signal_queue.modules[name].add_destination(dest)
            else:
                print("Adding", name, "to", dest)
                module = Module(dest, signal_queue)
                signal_queue.add_module(dest, module)
                signal_queue.modules[dest].add_root(name)
                signal_queue.modules[name].add_destination(dest)
            
    file.close()

    # for module in signal_queue.modules.values():
    #     if module.type == ModuleType.FlipFlop:
    #         module.cycle_size()

    original_signal_queue = deepcopy(signal_queue)
    steps = 0
    try:
        while True:
            steps += 1
            signal_queue.append(("button", "broadcaster", Signal.LOW))
            while signal_queue.signal_queue:
                try:
                    signal_queue.step()
                except ValueError:
                    print(steps)

            equal = True
            for i in range(len(signal_queue.modules)):
                name = list(signal_queue.modules.keys())[i]
                if signal_queue.modules[name] != original_signal_queue.modules[name]:
                    equal = False
                    break

            if equal:
                break


        print(signal_queue.low_counter)
        print(signal_queue.high_counter)
        print(steps)

        print(signal_queue.low_counter * signal_queue.high_counter)
    except:
        print(steps)


if __name__ == "__main__":
    main()


