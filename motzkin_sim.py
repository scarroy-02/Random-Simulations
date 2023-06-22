import random
import sys
sys.setrecursionlimit(10000000)

def motzkin_path(length):
    w = []
    for i in range(length+1):
        A = 0
        B = 0
        move = random.choice(['a','b','c'])
        w.append(move)
        if move == 'a':
            A = A + 1
        elif move == 'b':
            B = B + 1
        if A < B:
            motzkin_path(length)
    return w

print(motzkin_path(10))    