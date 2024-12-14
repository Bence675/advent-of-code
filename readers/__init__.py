
def read_input(file_name, sep = " ", transform = None):
    file = open(file_name, "r")
    res = []
    data = file.read().split("\n")
    for line in data:
        if transform:
            res.append([transform(x) for x in line.split(sep)])
        else:
            res.append(line.split(sep))
    
    if len(res[-1]) == 1 and res[-1][0] == "":
        res.pop()
    
    if len(res) == 1:
        res = res[0]
    
    return res
    