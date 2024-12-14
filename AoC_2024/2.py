

def read_input():
    reports = []
    file = open("2.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        reports.append(line.split())

    return reports


def part1():
    reports = read_input()
    counter = 0
    for report in reports:
        inc = dec = True
        safe = True
        last = int(report[0])
        for i in range(1, len(report)):
            current = int(report[i])
            if current <= last:
                inc = False
            if current >= last:
                dec = False
            if abs(current - last) > 3:
                safe = False
            last = current
        if (inc or dec) and safe:
            print(report)
            counter += 1
    print(counter)
    
def part2():
    reports = read_input()
    counter = 0
    for raw_report in reports:
        for skip in range(len(raw_report) + 1):
            report = raw_report[:skip] + raw_report[skip + 1:]
            inc = dec = True
            safe = True
            last = int(report[0])
            for i in range(1, len(report)):
                current = int(report[i])
                if current <= last:
                    inc = False
                if current >= last:
                    dec = False
                if abs(current - last) > 3:
                    safe = False
                last = current
            if (inc or dec) and safe:
                counter += 1
                print(report)
                break

    print(counter)

part2()
                