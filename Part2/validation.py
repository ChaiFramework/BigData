#!/usr/bin/env python3
from mapper import mapping
 
# Print 1 when distances remain same
def validate(map_dist, map_dist1):
    for node in map_dist:
        if(map_dist[node] != map_dist1[node]):
            print(0)
            return
        
    print(1)

if __name__ == "__main__":
    map_dist = mapping("distance.txt")
    map_dist1 = mapping("distance1.txt")
    validate(map_dist, map_dist1)