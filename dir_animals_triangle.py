import random
import itertools

def simulate_animals(size):
    list_vertices = [(0,0)]
    for i in range(size):
        eligible_moves = []
        for j in list_vertices:
            moves = [(j[0],j[1]+1),(j[0]+1,j[1]),(j[0]+1,j[1]+1)]
            for k in moves:
                if (k not in list_vertices):
                    eligible_moves.append(k)
        list_vertices.append(random.choice(eligible_moves))
    return list_vertices

#vert = simulate_animals(100)
#print(vert)

def set_animals(size):
    if size == 1:
        A = [[(0,0)]]
        return A
    else:
        A1 = []
        A2 = []
        for a in set_animals(size-1):
            eligible_moves = []
            for j in a:
                moves = [(j[0],j[1]+1),(j[0]+1,j[1]),(j[0]+1,j[1]+1)]
                for k in moves:
                    if (k not in a):
                        eligible_moves.append(k)
            for m in eligible_moves:
                A1.append(a+[m])
        for b in A1:
            A2.append(sorted(b))
        res = []
        [res.append(x) for x in A2 if x not in res]
        return res

def num_increasing(size):
    label_DA = []
    output = [i for i in range(1, size+1)]
    perm = list(itertools.permutations(output[1:]))
    count = 0
    for A in set_animals(size):
        #print(perm)
        for j in perm:
            label_DA = [[(0,0),1]]
            for vert in A[1:]:
                label_DA.append([vert,j[A.index(vert)-1]])
            #print(label_DA)
            if check_if_increasing(label_DA):
                count = count + 1
                #print(label_DA)
    print(count)
       
def check_if_increasing(label_DA):
    for i in label_DA:
        neighbours = []
        for j in label_DA:
            if (tuple(map(lambda a, b: a - b, j[0], i[0])) == (0,1)) or (tuple(map(lambda a, b: a - b, j[0], i[0])) == (1,0)) or (tuple(map(lambda a, b: a - b, j[0], i[0])) == (1,1)):
                neighbours.append(j)
        for k in neighbours:
            if i[1] > k[1]:
                return False
        if len(neighbours)==2:
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (-1,1) and neighbours[0][1]>neighbours[1][1]):
                return False
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (1,-1) and neighbours[0][1]<neighbours[1][1]):
                return False
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (-1,0) and neighbours[0][1]>neighbours[1][1]):
                return False
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (1,0) and neighbours[0][1]<neighbours[1][1]):
                return False
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (0,1) and neighbours[0][1]>neighbours[1][1]):
                return False
            if (tuple(map(lambda a, b: a - b, neighbours[0][0], neighbours[1][0])) == (0,-1) and neighbours[0][1]<neighbours[1][1]):
                return False
        if len(neighbours)==3:
            neighbours.sort()
            a = [neighbours[0][1],neighbours[2][1],neighbours[1][1]]
            b = a
            if a != b.sort():
                return False
    return True

for i in range(1,11):
    num_increasing(i)

def re_set_animals(size,per):
    A = set_animals(size)
    A1 = []
    for a in A:
        adj_vert = []
        for j in a:
            moves = [(j[0],j[1]+1),(j[0]+1,j[1])]
            for k in moves:
                if (k not in a):
                    adj_vert.append(k)
        res = []
        [res.append(x) for x in adj_vert if x not in res]
        if len(res)==per:
            A1.append(a)
    return A1

#print(set_animals(3))

#for i in range(1,11):
#    print(len(set_animals(i)))

#for i in range(8,9):
#    for j in range(1,30):
#        DA = re_set_animals(i,j)
#        print(len(DA),i+1,j)

#t = open("dir_animal_sim.txt", "w")
#for i in vert:
#    t.writelines(",".join(list(map(str, i)))+"\n")
#print("Succesfully written in file")
