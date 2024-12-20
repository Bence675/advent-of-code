

def read_file(file_name):
    file = open(file_name, "r")
    data = file.read().split("\n")
    return data

def parse_input(data, sep = " ", transform = None):
    
    res = []
    for line in data:
        if transform:
            res.append([transform(x) for x in line.split(sep)])
        else:
            splited = line.split(sep)
            if len(splited) == 1:
                res.append(splited[0])
            else:
                res.append(line.split(sep))
    
    if len(res[-1]) == 1 and res[-1][0] == "":
        res.pop()
    
    if len(res) == 1:
        res = res[0]
    
    return res

def read_input(file_name, sep = " ", transform = None):
    data = read_file(file_name)
    return parse_input(data, sep, transform)
    