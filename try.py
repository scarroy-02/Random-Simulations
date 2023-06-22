import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(500)
y = np.random.rand(500)

plt.scatter(x,y,s=0.5)

plt.savefig("try.pdf")
plt.close()

import  random, math, time, itertools
from array import *
from pylab import *
import csv
import sys
import subprocess

print("ARG"+str(sys.argv))

Edges = 0  # 1 if edges
           # 0 if vertices

DataFiles=["dir_animal_sim_unif.txt"]
#DataFiles=["datadots.txt"]
ExportFiles =["dir_animal_sim_unif_test.pdf"]
c=-1
for arg in sys.argv:
    c +=1
    if(c>0):
        print(arg)
        DataFiles.append(str(arg)+".txt")
        ExportFiles.append(str(arg)+".pdf")

print("les fichiers sources DATAFILE")
print(DataFiles)

couleurs = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'w']

def ParseFile(file):
    global Nb, GG
    f = open(file,'r')
    reader = csv.reader(f)
    GG=[]
    if Edges == 1:
        Size = 4
    if Edges ==0:
        Size = 2
    for line in reader:
        A = line 
        GG.append([ int(A[i]) for i in range(Size)])
    f.close()
    return(GG)

for NB in range(len(DataFiles)):
        G = ParseFile(DataFiles[NB])
        print(G)
        print("wait !")
        print(ExportFiles[NB])
        print("je fais ça ")
        #for g in G:
            
        #    plt.plot( g[0], g[1],color='green', marker='o', linestyle='dashed', linewidth=2, markersize=1)
            #xticks(np.arange(-40, 20, step=5))
            #yticks(np.arange(0, 600, step=10))
        x,y = zip(*G)
        plt.scatter(x,y,s=0.5)
        xticks(np.arange(min(x), max(x), step=1))
        yticks(np.arange(min(y), max(y), step=10))
        #plt.grid()
        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])
        frame1.axes.xaxis.set_ticklabels([])
        #plt.xticks(range(20))
        #plt.yticks(range(20))
        plt.savefig(ExportFiles[NB])
        plt.close()
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
print("Voila, j'ai exporté ",ExportFiles[NB], " sir! ")
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")