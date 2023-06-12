import random
from collections import Counter
count = 0 

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
        A = [[(0,0),(1,0)],[(0,0),(0,1)],[(0,0),(1,1)]]
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

def re_set_animals(size,per):
    A = set_animals(size)
    A1 = []
    for a in A:
        adj_vert = []
        for j in a:
            moves = [(j[0],j[1]+1),(j[0]+1,j[1]),(j[0]+1,j[1]+1)]
            for k in moves:
                if (k not in a):
                    adj_vert.append(k)
        res = []
        [res.append(x) for x in adj_vert if x not in res]
        if len(res)==per:
            A1.append(a)
    return A1

print(re_set_animals(7,7))

for i in range(9,10):
    for j in range(1,30):
        DA = re_set_animals(i,j)
        print(len(DA),i+1,j)

#t = open("dir_animal_sim.txt", "w")
#for i in vert:
#    t.writelines(",".join(list(map(str, i)))+"\n")
#print("Succesfully written in file")
