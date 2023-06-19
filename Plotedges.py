# fichier de donnee en entree xi, yi, xf, yf
# usage python3 Python_Plot.py filename1 ... filenamek  sans extension
# ou  python3 Python_Plot.py et dans ce cas, utilisation de la liste par défaut
# specifiée au début du fichier

import  random, math, time, itertools
import numpy as np
from array import *
from pylab import *
import csv
import sys
import matplotlib.pyplot as plt
import subprocess

print("ARG"+str(sys.argv))

Edges = 0  # 1 if edges
           # 0 if vertices

DataFiles=["dir_animal_sim_unif.txt"]
#DataFiles=["datadots.txt"]
ExportFiles =["dir_animal_sim_unif.pdf"]
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

if(Edges == 1):
    for NB in range(len(DataFiles)):
        G = ParseFile(DataFiles[NB])
        print("wait !")
        print(ExportFiles[NB])
        for g in G:
            plt.plot( [g[0], g[2]],[g[1], g[3]],'r',lw =1 )
            #xticks(np.arange(0, 21, step=10))
            #yticks(np.arange(0, 21, step=10))
        plt.axhline(0)
        plt.savefig(ExportFiles[NB])
        plt.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Voila, j'ai exporté ",ExportFiles[NB], " sir! ")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
else:
    for NB in range(len(DataFiles)):
        G = ParseFile(DataFiles[NB])
        print(G)
        print("wait !")
        print(ExportFiles[NB])
        print("je fais ça ")
        for g in G:
            
            plt.plot( g[0], g[1],color='green', marker='o', linestyle='dashed', linewidth=2, markersize=5 )
            #xticks(np.arange(0, 21, step=10))
            #yticks(np.arange(0, 21, step=10))
        plt.grid()
        plt.xticks(range(20))
        plt.yticks(range(20))
        plt.savefig(ExportFiles[NB])
        plt.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Voila, j'ai exporté ",ExportFiles[NB], " sir! ")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    
