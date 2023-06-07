import random
import csv

def generate_dyck_path(n):
    path = []
    level = 0
    while len(path) < 2 * n:
        if level == 0:
            path.append("U")
            level += 1
        else:
            step = random.choice(["U", "D"])
            if step == "U":
                path.append("U")
                level += 1
            else:
                path.append("D")
                level -= 1
    return path

def path_to_edges(path):
    edge_set = [[0,0,1,1]]
    for i in range(len(path)-1):
        if path[i+1] == 'U':
            edge_set.append([i+1,edge_set[i][3],i+2,edge_set[i][3]+1])
        elif path[i+1] == 'D':
            edge_set.append([i+1,edge_set[i][3],i+2,edge_set[i][3]-1])
    return edge_set

def convert_dyck(path):
    new_path = []
    edges = path_to_edges(path)
    last_edge = edges[-1]
    steps = []
    if last_edge[3] == 0:
        return edges
    elif last_edge[3] > 0:
        for i in range(1,len(path)):
            if path[i] == 'U':
                steps.append(i)
        changes = random.sample(steps,last_edge[3]//2)
        changes.sort()
        for i in range(len(path)):
            if (i in changes):
                new_path.append('D')
            else:
                new_path.append(path[i])
        return path_to_edges(new_path)
    elif last_edge[3] < 0:
        for i in range(1,len(path)):
            if path[i] == 'D':
                steps.append(i)
        changes = random.sample(steps,last_edge[3]//2)
        changes.sort()
        for i in range(len(path)):
            if (i in changes):
                new_path.append('U')
            else:
                new_path.append(path[i])
        return path_to_edges(new_path)
    
path = generate_dyck_path(5000)
edges = convert_dyck(path)

t = open("dataedges.txt", "w")
for i in edges:
    t.writelines(",".join(list(map(str, i)))+"\n")
print("Succesfully written in file")