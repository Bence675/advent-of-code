
from fractions import Fraction
import sympy
import numpy as np

class Hail:
    def __init__(self, data):
        data = data.split(" @ ")
        self.x, self.y, self.z = map(Fraction, data[0].split(", "))
        self.vel_x, self.vel_y, self.vel_z = map(Fraction, data[1].split(", "))

        self.pos = np.array([self.x, self.y, self.z])
        self.vel = np.array([self.vel_x, self.vel_y, self.vel_z])

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z}), ({self.vel_x}, {self.vel_y}, {self.vel_z})"
    
    def __repr__(self):
        return self.__str__()
    


def read_input():
    file = open("24.txt", "r")
    res = []
    while True:
        line = file.readline()[:-1]
        if not line:
            break

        res.append(Hail(line))
    return res

def time_to_cross_2d(hail1, hail2):
    # time2 = (hail1.x - hail2.x) / (hail2.vel_x - hail1.vel_x)
    try:
        step2 = (hail1.y - hail2.y + (hail2.x - hail1.x) * hail1.vel_y / hail1.vel_x) / (hail2.vel_y - hail2.vel_x * hail1.vel_y / hail1.vel_x)
        step1 = (hail2.x - hail1.x + hail2.vel_x * step2 ) / hail1.vel_x
    except:
        return None, None

    return step1, step2

def get_pos_after_time(hail, time):
    return hail.x + hail.vel_x * time, hail.y + hail.vel_y * time

def get_pos_after_time_3d(hail, time):
    return hail.x + hail.vel_x * time, hail.y + hail.vel_y * time, hail.z + hail.vel_z * time

def part1():
    hails = read_input()
    counter = 0
    for i in range(len(hails)-1):
        for j in range(i+1, len(hails)):
            # (hails[i], hails[j])
            time1, time2 = time_to_cross_2d(hails[i], hails[j])
            print(time1, time2)
            if time1 is None or time2 is None or time1 < 0 or time2 < 0:
                continue
            # print(time1, time2)
            # if time1 is not None and time2 is not None:
            #     print([float(x) for x in get_pos_after_time(hails[i], time1)], get_pos_after_time(hails[j], time2))

            cross = get_pos_after_time(hails[i], time1)
            assert cross == get_pos_after_time(hails[j], time2)
            
            if all([200000000000000 <= cross[i] <= 400000000000000 for i in range(2)]):
                counter += 1

    print(counter)

def get_step_to_cross_by_the_rock(hail1, hail2, n):
    return Fraction( np.dot((hail1.pos - hail2.pos + hail1.vel * n), hail1.vel)) / Fraction(np.dot(hail1.vel, hail1.vel))



def part2():
    hails = read_input()
    x,y,z,vx,vy,vz = (sympy.Symbol(x) for x in "x y z vx vy vz".split())
    p = [x, y, z]
    v = [vx, vy, vz]
    vars = [*p, *v]
    eqs = []
    for i, h in enumerate(hails[:3]):
        t = sympy.Symbol(f"t{i}")
        for j in range(3):
            eqs.append(p[j] + v[j] * t - h.pos[j] - h.vel[j] * t)

        vars.append(t)

    res = sympy.solve(eqs, vars)
    print(res)

def get_prime_factors(n):
    res = []
    for i in range(2, n+1):
        if n % i == 0:
            while n % i == 0:
                n //= i
                res.append(i)
                print(i, n)
        if sympy.isprime(n):
            res.append(n)
            break
        if n == 1 or n == -1:
            break
    return res

factors1 = get_prime_factors(109486731858000)

factors2 = get_prime_factors(131384078229600)

factors3 = get_prime_factors(35037768555790)

factors4 = get_prime_factors(1925152118450)

print(get_prime_factors(5*7*11*2606826949+1))



part2()