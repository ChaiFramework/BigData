#!/usr/bin/env python

import sys
from operator import itemgetter

Np = None
Nc = None

#init data structures
eList = []
multi = {}
X = {}
      

for line in sys.stdin:
    Nc, ind, val = line.rstrip().split("\t")

    ind, val = map(int,[ind,val])
    if Nc == Np:
        eList.append((ind,val))
    else:
        if Np:
            eList = sorted(eList,key=itemgetter(0))
            i = 0
            element = 0
            
            while i < len(eList) - 1:
                if eList[i][0] == eList[i + 1][0]:
                    element += eList[i][1]*eList[i + 1][1]
                    i += 2
                else:
                    i += 1
            multi[Np] = element
            X[Np] = eList[len(eList)-1][1]
                                   
        Np = Nc
        eList = [(ind,val)]

if Nc == Np:
    eList = sorted(eList,key=itemgetter(0))
    i = 0
    element = 0
    while i < len(eList) - 1:
        if eList[i][0] == eList[i + 1][0]:
            element += eList[i][1]*eList[i + 1][1]
            i += 2
        else:
            i += 1
    multi[Np] = element
    X[Np] = eList[len(eList)-1][1]



for key in multi:
    value = X[key] - multi[key]
    row, col = key.split(":")
    print("{0}\t{1}\t{2}".format(row, col, value))


    




    
    







