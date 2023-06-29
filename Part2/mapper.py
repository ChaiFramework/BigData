#!/usr/bin/env python
# -*-coding:utf-8 -*
import sys

def keypair(kp):
	key, value = kp.rstrip().split("\t")
	return key

#get distance from node n to node m
def distCalc(n,m):
    return 1

#get dictionary whose key is node and value is distance from source
def mapping(filename):
    distance = {}

    with open(filename) as fp:
        line = fp.readline()
        while line:
            if line:
                try:
                    key, distance_value = line.split(":")
                    distance[key] = int(distance_value.strip())
                except:
                    break
            else:
                break
            line = fp.readline()

    fp.close()
 
    return distance

#Node, distance pair for reducer

def node_dist(map_dist):
    DataForEmit = []
    for line in sys.stdin:
        node, noderef = line.split(":")
        adjList = noderef.strip().split(" ")
        distance = map_dist[node]
        data = "{}\t{}"
        str_node = str(node)
        str_distance = str(distance)
        formated_data = data.format(str_node, str_distance)
        DataForEmit.append(formated_data)
        
        #traverse adjacent list
        for neighbor in adjList:
            if neighbor == "none":
                continue
            distance_neighbor = distance + distCalc(node, neighbor)
            data = "{}\t{}"
            str_neighbor = str(neighbor)
            str_distance_neighbor = str(distance_neighbor)
            formated_data = data.format(str_neighbor, str_distance_neighbor)
            DataForEmit.append(formated_data)

    return DataForEmit

if __name__ == "__main__":
    map_dist = mapping("distance.txt")
    mapped = node_dist(map_dist)
    
    #key pair sorting

    mapped.sort(key = keypair)
    #temp code for test
    for item in mapped:
        node, distance = item.rstrip().split("\t")
        print("%s\t%s"%(node, distance))