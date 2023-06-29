#!/usr/bin/env python3

import sys

nd = None
distance_list = []
distMin= 100000000000000

for line in sys.stdin:
    #split input into node and distance
    node, distance = line.rstrip().split("\t")
    distance = int(distance)
    
    if nd == node:
        #Add all distance to list
        distance_list.append(distance)
    else:
        #print node and minimun distance
        if nd:
            for dist in distance_list:
                if dist < distMin:
                    distMin= dist
                             
            print("%s:%s"%(nd, distMin))

        nd = node
        distMin= 100000000000000
        distance_list = [distance]

    #Display Node and least distance
if nd == node:
    for dist in distance_list:
        if dist < distMin:
            distMin = dist
                             
    print("%s:%s"%(nd, distMin))