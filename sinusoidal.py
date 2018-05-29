#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:05:03 2018

@author: tymarking
"""

import csv, math

with open('data.csv', newline='') as csvfile:
    data = []
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    for row in reader:
#        print(', '.join(row))
#        print(row[0])
        data.append([2*math.pi*float(str(row[0]))/360, int(str(row[1]))])

#params Acos(Bx+C)+D
A = -100
B = 2
C = 0
D = 100



def getError(a, b, c, d):
    errorSum = 0
    for row in data:
        estY = a*math.cos(b*row[0]+c)+d
        err = (row[1]-estY)**2
        errorSum += err
    error = errorSum/len(row)
    return error

#print(getError(A,B,C,D))

l = 0.000001

for epoch in range(5000):
    error = getError(A,B,C,D)
    
    dAs = []
    dBs = []
    dCs = []
    dDs = []
    for row in data:
        x = row[0]
        
        estY = A*math.cos(B*x+C)+D
        err = (row[1]-estY)**2
        
        dA = l*err* math.cos(B*x+C)
        dB = l*err* x*A*(-math.sin(B*x+C))
        dC = l*err* A*(-math.sin(B*x+C))
        dD = l*err
        dAs.append(dA)
        dBs.append(dB)
        dCs.append(dC)
        dDs.append(dD)
    
    dA = sum(dAs)/len(dAs)
    dB = sum(dBs)/len(dBs)
    dC = sum(dCs)/len(dCs)
    dD = sum(dDs)/len(dDs)
    
    A -= dA
    B -= dB
    C -= dC
    D -= dD
    
    print(getError(A,B,C,D))
        
print(str(A)+"cos("+str(B)+"x + "+str(C)+") + "+ str(D))