import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

from cleaning import clean_empty
from regression import gradient_descent
from proj1 import runProj1
from proj2 import runProj2

fileName="D3.csv"
alpha=0.05
iterations = 1000
outputFileName = ''
whichProj=0
def help():
    with open("help.txt", "r") as file:
        print(file.read())
    return

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-a":
            if i + 1 < len(sys.argv):
                alpha=float(sys.argv[i+1])
        elif sys.argv[i] == "-i":
            if i + 1 < len(sys.argv):
                iterations = int(sys.argv[i+1])
        elif sys.argv[i] == "-f":
            if i + 1 < len(sys.argv):
                fileName=sys.argv[i+1]
        elif sys.argv[i]=="-o":
            if i + 1 < len(sys.argv):
                outputFileName = sys.argv[i+1]
        elif sys.argv[i]=="-p":
            if i + 1 < len(sys.argv):
                whichProj = int(sys.argv[i+1])

if whichProj==1:
    print("Project 1: ")
    if outputFileName=='':
        outputFileName='project_1_plot'
    runProj1(fileName, outputFileName, alpha, iterations)
elif whichProj==2:
    print("Project 2: ")
    if outputFileName=='':
        outputFileName='project_2_plot'
    runProj2(fileName, outputFileName, alpha, iterations)
else:
    help()