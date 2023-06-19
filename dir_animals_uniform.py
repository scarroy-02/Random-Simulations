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
        return path
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
        return new_path
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
        return new_path
    
path = generate_dyck_path(20)
new_path = convert_dyck(path)

def convert_path(path):
    sum = 0
    selected = []
    for i in path:
        if i == 'U':
            sum = sum + 1
            if sum > 0:
                selected.append((sum,i))
        elif i == 'D':
            sum = sum - 1
            if sum < 0:
                selected.append((sum,i))
    return selected

def selected_to_dimer(path):
    dimer_list = []
    for i in path:
        if i[1]=='U':
            dimer_list.append((-(2*i[0]-1),-(2*i[0]-3)))
        if i[1]=='D':
            dimer_list.append(((2*-i[0]-1),(2*-i[0]+1)))
    return dimer_list

def dimer_to_heap(dimers):
    heap_dict = [[0,(-1,1)]]
    heap_levels = [0]
    for i in dimers[1:]:
        for j in range(len(heap_dict)-1,-1,-1):
            join_tup = ()
            for k in heap_dict[j][1:]:
                join_tup = join_tup + k
            if (i[0] in  join_tup) or (i[1] in join_tup):
                if j+1 not in heap_levels:
                    heap_dict.append([j+1,i])
                    heap_levels.append(j+1)
                    break
                elif j+1 in heap_levels:
                    heap_dict[j+1].append(i)
                    break
    return heap_dict

def heap_to_animal(heap):
    vert = [(0,0)]
    for i in range(1,len(heap)):
        if (-1,1) in heap[i][1:]:
            if (-1,1) in heap[i-1][1:]:
                vert.append((heap[i][0],heap[i][0]))
            else:
                vert.append((heap[i][0]-1,heap[i][0]-1))
        for j in heap[i][1:]:
            if j != (-1,1):
                a = (j[0]+j[1])//4
                if a < 0:
                    vert.append((heap[i][0]+a,heap[i][0]))
                elif a > 0:
                    vert.append((heap[i][0],heap[i][0]-a))
    return vert

selected = convert_path(new_path)
dimers = selected_to_dimer(selected)
heap = dimer_to_heap(dimers)
vert = heap_to_animal(heap)

print(selected)
print(dimers)
print(heap)
print(vert)

t = open("dir_animal_sim_unif.txt", "w")
for i in vert:
    t.writelines(",".join(list(map(str, i)))+"\n")
print("Succesfully written in file")